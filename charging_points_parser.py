import json
from random import randint
import time
import requests
from os import getenv
from decimal import Decimal
from datetime import datetime
from typing import Generator, Optional

import pycountry
from dotenv import load_dotenv

import enums
import schemas

load_dotenv()

class BatterFlyParser:
    URL = "https://evapi.qasqir.kz/api/charging/charge-points?lat=53.308192008234826&lon=71.89814008364576&distance=8104740.584412225&size=999"
    API_KEY = getenv('api_key')

    CONNECTORS_MAPPING = {
        "chademo": {
            "standard": enums.ConnectorType.chademo.value,
            "format": enums.ConnectorFormat.cable.value,
            "power_type": enums.PowerType.dc.value,
        },
        "type-2": {
            "standard": enums.ConnectorType.iec_62196_t2.value,
            "format": enums.ConnectorFormat.socket.value,
            "power_type": enums.PowerType.ac_3_phase.value,
        },
        "ccs2-combo": {
            "standard": enums.ConnectorType.iec_62196_t2_combo.value,
            "format": enums.ConnectorFormat.cable.value,
            "power_type": enums.PowerType.dc.value,
        },
        "gbt-dc": {
            "standard": enums.ConnectorType.gbt_dc.value,
            "format": enums.ConnectorFormat.cable.value,
            "power_type": enums.PowerType.dc.value,
        }
    }

    STATUS_MAPPING = {
        "Available": enums.Status.available.value,
        "Charging": enums.Status.charging.value,
        "Finishing": enums.Status.blocked.value,
        None: enums.Status.unknown.value,
    }

    STATION_STATUS_MAPPING = {
        "INACTIVE": False,
        "ACTIVE": True
    }

    def __init__(self):
        self.party_id = "QSR"
        self.operator = {"name": "qasqir"}
        self.headers = {
            "Content-Type": "application/json",
            "apikey": self.API_KEY
        }
        self.is_error_occurred = False
        self.json_data_list = []

    def _extract_data(self) -> Generator[Optional[dict], None, None]:
        try:
            response = requests.get(url=self.URL, headers=self.headers)
            response.raise_for_status()
        except requests.RequestException as err:
            self.is_error_occurred = True
            print("Error in _extract_data:", err)
            return
        data = response.json()
        locations = data.get("items", [])
        if locations:
            location_map = {str(el["id"]): el for el in locations}
            for item in location_map.values():
                yield item

    def _build_tariff(
        self, last_updated: datetime, raw_connector: str, energy_price: Optional[float] = None, currency=enums.Currency.BYN
    ) -> Optional[schemas.Tariff]:
        price_components = []
        if energy_price is not None:
            energy_price_component = schemas.PriceComponent(
                type=enums.TariffDimensionType.energy,
                price=str(float(energy_price)),
                step_size=1,
            )
            price_components.append(energy_price_component)
        if not price_components:
            return None
        tariff_element = schemas.TariffElement(price_components=price_components)
        tariff = schemas.Tariff(
            party_id=self.party_id,
            country_code=enums.CountryCode.BY.value,
            elements=[tariff_element],
            currency=currency,
            last_updated=last_updated
        )
        return tariff

    def _transform_data(self, *, data_to_transform: dict):
        now = datetime.now()
        evses = []
        connectors: dict = data_to_transform.get("connectors", {})
        location_status = self.STATION_STATUS_MAPPING.get(data_to_transform.get("statsus"))
        for connector_key, connector in connectors.items():
            connector_data = self.CONNECTORS_MAPPING.get(connector["type"])
            if connector_data is None:
                continue
            connector_data["max_electric_power"] = connector.get("maxPower")
            connector_data["last_updated"] = now
            connector_string = self.party_id + str(data_to_transform.get('id')) + str(connector_key)
            tariff = connector.get("rate")
            if tariff:
                tariff_data = self._build_tariff(
                    energy_price=tariff, last_updated=now, raw_connector=connector_string
                )
                if tariff_data:
                    connector_data["tariffs"] = [tariff_data]
            connector_schema = schemas.Connector(**connector_data)
            connector['status'] = True if connector['availability'] == 'on' else False
            status = self.STATUS_MAPPING.get(connector.get("status"))
            evse = schemas.EVSE(
                status=status if location_status else enums.Status.outoforder.value,
                connectors=[connector_schema],
                last_updated=now
            )
            evses.append(evse)
        
        location = data_to_transform.get('location', {})
        longitude = str(location.get("lon"))
        latitude = str(location.get("lat"))
        location_coord = schemas.GeoCoordinates(
            longitude=longitude[:11], latitude=latitude[:11]
        )
        city = location.get("city", "")
        country_code = location.get("countryCode", "")
        py_country = pycountry.countries.get(alpha_3=country_code)
        country_name = py_country.name if py_country else '?'
        country_alpha2 = py_country.alpha_2 if py_country else 'BL'
        country_alpha3 = py_country.alpha_3 if py_country else 'BLR'
        postal_code = location.get("postalCode", "")
        name = data_to_transform.get("name", "")
        address = location.get("address", "")
        directions_text = data_to_transform.get("description", "")
        time_zone = location.get("timeZone", "")
        directions = []
        if directions_text:
            directions = [
                {
                    "language": enums.CountryCode.RU,
                    "text": directions_text
                }
            ]
        result_schema = schemas.Location(
            id=str(data_to_transform["id"]),
            country_code=enums.CountryCode(country_alpha2).value,
            country=enums.Country(country_alpha3).value,
            party_id=self.party_id,
            coordinates=location_coord,
            credential=directions_text,
            name=name[:255],
            address=address[:64],
            city=city[:45],
            state=country_name[:128],
            postal_code=postal_code[:10],
            directions=directions,
            time_zone=time_zone,
            evses=evses,
            operator=self.operator,
            last_updated=now,
        )
        return result_schema

    def run(self) -> None:
        for extracted_object_data in self._extract_data() or []:
            try:
                location_id = extracted_object_data.get("id")
            except AttributeError as e:
                continue
            try:
                pydantic_schema = self._transform_data(
                    data_to_transform=extracted_object_data
                )
                json_data = json.loads(pydantic_schema.json(), parse_float=Decimal)
                print('begin: ', end='---->\n')
                print(pydantic_schema.model_dump_json(), end='\n<----')
                print('end. ', end='\n *\n **\n *** \n')
            except Exception as e:
                print("Error transforming data:", e)
                continue


if __name__ == "__main__":
    while True:
        try:
            parser = BatterFlyParser()
            # parser.run()
            print(getenv('VERSION', 'shit'))
        except Exception as e:
            time.sleep(60 * randint(1, 3))
        finally:
            time.sleep(3 * randint(1, 3))
