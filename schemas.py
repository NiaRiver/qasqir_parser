import uuid
from datetime import datetime
from decimal import Decimal

from pydantic import AnyUrl, BaseModel, Field

import enums


class GeoCoordinates(BaseModel):
    latitude: str = Field(max_length=11)
    longitude: str = Field(max_length=11)


class DisplayText(BaseModel):
    language: str = Field(default=enums.CountryCode.RU.value, max_length=2)
    text: str = Field(max_length=512)


class AdditionalGeoCoordinates(GeoCoordinates):
    name: DisplayText = {}


class StatuSchedule(BaseModel):
    period_begin: datetime
    period_end: datetime
    status: enums.Status


class PriceComponent(BaseModel):
    type: enums.TariffDimensionType
    price:  Decimal = Field(decimal_places=4)
    vat: Decimal | None = Field(decimal_places=4)
    step_size: int
Decimal

class TariffElement(BaseModel):
    price_components: list[PriceComponent]


class Tariff(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, max_length=36)
    currency: str = enums.Currency.RUB
    country_code: enums.CountryCode = enums.CountryCode.RU.value
    party_id: str = Field(..., max_length=3)
    elements: list[TariffElement]
    last_updated: datetime


class Connector(BaseModel):
    standard: enums.ConnectorType
    format: enums.ConnectorFormat
    power_type: enums.PowerType
    last_updated: datetime
    id: str = Field(default_factory=uuid.uuid4, max_length=36)
    max_voltage: int | None = Field(default=None, ge=0)
    max_amperage: int | None = Field(default=None, ge=0)
    max_electric_power: int | None = Field(default=None, ge=0)
    terms_and_conditions: AnyUrl = ""
    tariffs: list[Tariff] = []


class EVSE(BaseModel):
    uid: str = Field(default_factory=uuid.uuid4, max_length=36)
    status: enums.Status
    connectors: list[Connector]
    last_updated: datetime
    evse_id: str = Field(default="", max_length=48)
    status_schedule: list[StatuSchedule] = []
    capabilities: list[enums.Capability] = []
    floor_level: str = Field(default="", max_length=4)
    coordinates: GeoCoordinates = {}
    physical_reference: str = Field(default="", max_length=16)
    directions: list[DisplayText] = []
    parking_restrictions: list[enums.ParkingRestriction] = []


class Location(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, max_length=36)
    party_id: str = Field(..., max_length=3)
    coordinates: GeoCoordinates
    address: str = Field(..., max_length=64)
    city: str = Field(..., max_length=45)
    time_zone: str = Field(..., max_length=255)
    last_updated: datetime
    evses: list[EVSE] = []
    publish: bool = True
    name: str = Field(default="", max_length=255)
    country_code: enums.CountryCode = enums.CountryCode.RU.value
    country: enums.Country = enums.Country.RUS.value
    postal_code: str = Field(default="", max_length=10)
    state: str = Field(default="", max_length=128)
    related_locations: list[AdditionalGeoCoordinates] = []
    parking_type: enums.ParkingType = ""
    directions: list[DisplayText] = []
    facilities: list[enums.Facility] = []
    charging_when_closed: bool = False
    operator: dict | None = None
    suboperator: dict | None = None
    owner: dict | None = None
    credential: str | None = None



input_json = """
{
    "latitude": "1234567898",
    "longitude": "8998764321"
}
"""

cords = GeoCoordinates.model_validate_json(input_json)
print('to json: \n' + cords.model_dump_json())

print('python: \n' + cords.latitude + ' ' + cords.longitude)