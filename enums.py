from enum import Enum

from django.db.models import TextChoices


class BaseEnum(str, Enum):
    @classmethod
    def choice_for_model(cls) -> list[tuple[str, str]]:
        return [(i.value, i.name.upper()) for i in cls]

    @classmethod
    def value_list(cls) -> list[str]:
        return [i.value for i in cls]


class Currency(BaseEnum):
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYN = "BYN"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHE = "CHE"
    CHF = "CHF"
    CHW = "CHW"
    CLF = "CLF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    COU = "COU"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRU = "MRU"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MXV = "MXV"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLE = "SLE"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    SSP = "SSP"
    STN = "STN"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    USN = "USN"
    UYI = "UYI"
    UYU = "UYU"
    UYW = "UYW"
    UZS = "UZS"
    VED = "VED"
    VES = "VES"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XAG = "XAG"
    XAU = "XAU"
    XBA = "XBA"
    XBB = "XBB"
    XBC = "XBC"
    XBD = "XBD"
    XCD = "XCD"
    XDR = "XDR"
    XOF = "XOF"
    XPD = "XPD"
    XPF = "XPF"
    XPT = "XPT"
    XSU = "XSU"
    XTS = "XTS"
    XUA = "XUA"
    XXX = "XXX"
    YER = "YER"
    ZAR = "ZAR"
    ZMW = "ZMW"
    ZWL = "ZWL"


class Country(BaseEnum):
    AFG = "AFG"
    ALA = "ALA"
    ALB = "ALB"
    DZA = "DZA"
    ASM = "ASM"
    AND = "AND"
    AGO = "AGO"
    AIA = "AIA"
    ATA = "ATA"
    ATG = "ATG"
    ARG = "ARG"
    ARM = "ARM"
    ABW = "ABW"
    AUS = "AUS"
    AUT = "AUT"
    AZE = "AZE"
    BHS = "BHS"
    BHR = "BHR"
    BGD = "BGD"
    BRB = "BRB"
    BLR = "BLR"
    BEL = "BEL"
    BLZ = "BLZ"
    BEN = "BEN"
    BMU = "BMU"
    BTN = "BTN"
    BOL = "BOL"
    BES = "BES"
    BIH = "BIH"
    BWA = "BWA"
    BVT = "BVT"
    BRA = "BRA"
    IOT = "IOT"
    BRN = "BRN"
    BGR = "BGR"
    BFA = "BFA"
    BDI = "BDI"
    KHM = "KHM"
    CMR = "CMR"
    CAN = "CAN"
    CPV = "CPV"
    CYM = "CYM"
    CAF = "CAF"
    TCD = "TCD"
    CHL = "CHL"
    CHN = "CHN"
    CXR = "CXR"
    CCK = "CCK"
    COL = "COL"
    COM = "COM"
    COG = "COG"
    COD = "COD"
    COK = "COK"
    CRI = "CRI"
    CIV = "CIV"
    HRV = "HRV"
    CUB = "CUB"
    CUW = "CUW"
    CYP = "CYP"
    CZE = "CZE"
    DNK = "DNK"
    DJI = "DJI"
    DMA = "DMA"
    DOM = "DOM"
    ECU = "ECU"
    EGY = "EGY"
    SLV = "SLV"
    GNQ = "GNQ"
    ERI = "ERI"
    EST = "EST"
    ETH = "ETH"
    FLK = "FLK"
    FRO = "FRO"
    FJI = "FJI"
    FIN = "FIN"
    FRA = "FRA"
    GUF = "GUF"
    PYF = "PYF"
    ATF = "ATF"
    GAB = "GAB"
    GMB = "GMB"
    GEO = "GEO"
    DEU = "DEU"
    GHA = "GHA"
    GIB = "GIB"
    GRC = "GRC"
    GRL = "GRL"
    GRD = "GRD"
    GLP = "GLP"
    GUM = "GUM"
    GTM = "GTM"
    GGY = "GGY"
    GIN = "GIN"
    GNB = "GNB"
    GUY = "GUY"
    HTI = "HTI"
    HMD = "HMD"
    VAT = "VAT"
    HND = "HND"
    HKG = "HKG"
    HUN = "HUN"
    ISL = "ISL"
    IND = "IND"
    IDN = "IDN"
    IRN = "IRN"
    IRQ = "IRQ"
    IRL = "IRL"
    IMN = "IMN"
    ISR = "ISR"
    ITA = "ITA"
    JAM = "JAM"
    JPN = "JPN"
    JEY = "JEY"
    JOR = "JOR"
    KAZ = "KAZ"
    KEN = "KEN"
    KIR = "KIR"
    PRK = "PRK"
    KOR = "KOR"
    KWT = "KWT"
    KGZ = "KGZ"
    LAO = "LAO"
    LVA = "LVA"
    LBN = "LBN"
    LSO = "LSO"
    LBR = "LBR"
    LBY = "LBY"
    LIE = "LIE"
    LTU = "LTU"
    LUX = "LUX"
    MAC = "MAC"
    MKD = "MKD"
    MDG = "MDG"
    MWI = "MWI"
    MYS = "MYS"
    MDV = "MDV"
    MLI = "MLI"
    MLT = "MLT"
    MHL = "MHL"
    MTQ = "MTQ"
    MRT = "MRT"
    MUS = "MUS"
    MYT = "MYT"
    MEX = "MEX"
    FSM = "FSM"
    MDA = "MDA"
    MCO = "MCO"
    MNG = "MNG"
    MNE = "MNE"
    MSR = "MSR"
    MAR = "MAR"
    MOZ = "MOZ"
    MMR = "MMR"
    NAM = "NAM"
    NRU = "NRU"
    NPL = "NPL"
    NLD = "NLD"
    NCL = "NCL"
    NZL = "NZL"
    NIC = "NIC"
    NER = "NER"
    NGA = "NGA"
    NIU = "NIU"
    NFK = "NFK"
    MNP = "MNP"
    NOR = "NOR"
    OMN = "OMN"
    PAK = "PAK"
    PLW = "PLW"
    PSE = "PSE"
    PAN = "PAN"
    PNG = "PNG"
    PRY = "PRY"
    PER = "PER"
    PHL = "PHL"
    PCN = "PCN"
    POL = "POL"
    PRT = "PRT"
    PRI = "PRI"
    QAT = "QAT"
    REU = "REU"
    ROU = "ROU"
    RUS = "RUS"
    RWA = "RWA"
    BLM = "BLM"
    SHN = "SHN"
    KNA = "KNA"
    LCA = "LCA"
    MAF = "MAF"
    SPM = "SPM"
    VCT = "VCT"
    WSM = "WSM"
    SMR = "SMR"
    STP = "STP"
    SAU = "SAU"
    SEN = "SEN"
    SRB = "SRB"
    SYC = "SYC"
    SLE = "SLE"
    SGP = "SGP"
    SXM = "SXM"
    SVK = "SVK"
    SVN = "SVN"
    SLB = "SLB"
    SOM = "SOM"
    ZAF = "ZAF"
    SGS = "SGS"
    SSD = "SSD"
    ESP = "ESP"
    LKA = "LKA"
    SDN = "SDN"
    SUR = "SUR"
    SJM = "SJM"
    SWZ = "SWZ"
    SWE = "SWE"
    CHE = "CHE"
    SYR = "SYR"
    TWN = "TWN"
    TJK = "TJK"
    TZA = "TZA"
    THA = "THA"
    TLS = "TLS"
    TGO = "TGO"
    TKL = "TKL"
    TON = "TON"
    TTO = "TTO"
    TUN = "TUN"
    TUR = "TUR"
    TKM = "TKM"
    TCA = "TCA"
    TUV = "TUV"
    UGA = "UGA"
    UKR = "UKR"
    ARE = "ARE"
    GBR = "GBR"
    USA = "USA"
    UMI = "UMI"
    URY = "URY"
    UZB = "UZB"
    VUT = "VUT"
    VEN = "VEN"
    VNM = "VNM"
    VGB = "VGB"
    VIR = "VIR"
    WLF = "WLF"
    ESH = "ESH"
    YEM = "YEM"
    ZMB = "ZMB"
    ZWE = "ZWE"


class CountryCode(BaseEnum):
    AF = "AF"
    AX = "AX"
    AL = "AL"
    DZ = "DZ"
    AS = "AS"
    AD = "AD"
    AO = "AO"
    AI = "AI"
    AQ = "AQ"
    AG = "AG"
    AR = "AR"
    AM = "AM"
    AW = "AW"
    AU = "AU"
    AT = "AT"
    AZ = "AZ"
    BS = "BS"
    BH = "BH"
    BD = "BD"
    BB = "BB"
    BY = "BY"
    BE = "BE"
    BZ = "BZ"
    BJ = "BJ"
    BM = "BM"
    BT = "BT"
    BO = "BO"
    BQ = "BQ"
    BA = "BA"
    BW = "BW"
    BV = "BV"
    BR = "BR"
    IO = "IO"
    BN = "BN"
    BG = "BG"
    BF = "BF"
    BI = "BI"
    KH = "KH"
    CM = "CM"
    CA = "CA"
    CV = "CV"
    KY = "KY"
    CF = "CF"
    TD = "TD"
    CL = "CL"
    CN = "CN"
    CX = "CX"
    CC = "CC"
    CO = "CO"
    KM = "KM"
    CG = "CG"
    CD = "CD"
    CK = "CK"
    CR = "CR"
    CI = "CI"
    HR = "HR"
    CU = "CU"
    CW = "CW"
    CY = "CY"
    CZ = "CZ"
    DK = "DK"
    DJ = "DJ"
    DM = "DM"
    DO = "DO"
    EC = "EC"
    EG = "EG"
    SV = "SV"
    GQ = "GQ"
    ER = "ER"
    EE = "EE"
    ET = "ET"
    FK = "FK"
    FO = "FO"
    FJ = "FJ"
    FI = "FI"
    FR = "FR"
    GF = "GF"
    PF = "PF"
    TF = "TF"
    GA = "GA"
    GM = "GM"
    GE = "GE"
    DE = "DE"
    GH = "GH"
    GI = "GI"
    GR = "GR"
    GL = "GL"
    GD = "GD"
    GP = "GP"
    GU = "GU"
    GT = "GT"
    GG = "GG"
    GN = "GN"
    GW = "GW"
    GY = "GY"
    HT = "HT"
    HM = "HM"
    VA = "VA"
    HN = "HN"
    HK = "HK"
    HU = "HU"
    IS = "IS"
    IN = "IN"
    ID = "ID"
    IR = "IR"
    IQ = "IQ"
    IE = "IE"
    IM = "IM"
    IL = "IL"
    IT = "IT"
    JM = "JM"
    JP = "JP"
    JE = "JE"
    JO = "JO"
    KZ = "KZ"
    KE = "KE"
    KI = "KI"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KG = "KG"
    LA = "LA"
    LV = "LV"
    LB = "LB"
    LS = "LS"
    LR = "LR"
    LY = "LY"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    MO = "MO"
    MK = "MK"
    MG = "MG"
    MW = "MW"
    MY = "MY"
    MV = "MV"
    ML = "ML"
    MT = "MT"
    MH = "MH"
    MQ = "MQ"
    MR = "MR"
    MU = "MU"
    YT = "YT"
    MX = "MX"
    FM = "FM"
    MD = "MD"
    MC = "MC"
    MN = "MN"
    ME = "ME"
    MS = "MS"
    MA = "MA"
    MZ = "MZ"
    MM = "MM"
    NA = "NA"
    NR = "NR"
    NP = "NP"
    NL = "NL"
    NC = "NC"
    NZ = "NZ"
    NI = "NI"
    NE = "NE"
    NG = "NG"
    NU = "NU"
    NF = "NF"
    MP = "MP"
    NO = "NO"
    OM = "OM"
    PK = "PK"
    PW = "PW"
    PS = "PS"
    PA = "PA"
    PG = "PG"
    PY = "PY"
    PE = "PE"
    PH = "PH"
    PN = "PN"
    PL = "PL"
    PT = "PT"
    PR = "PR"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RU = "RU"
    RW = "RW"
    BL = "BL"
    SH = "SH"
    KN = "KN"
    LC = "LC"
    MF = "MF"
    PM = "PM"
    VC = "VC"
    WS = "WS"
    SM = "SM"
    ST = "ST"
    SA = "SA"
    SN = "SN"
    RS = "RS"
    SC = "SC"
    SL = "SL"
    SG = "SG"
    SX = "SX"
    SK = "SK"
    SI = "SI"
    SB = "SB"
    SO = "SO"
    ZA = "ZA"
    GS = "GS"
    SS = "SS"
    ES = "ES"
    LK = "LK"
    SD = "SD"
    SR = "SR"
    SJ = "SJ"
    SZ = "SZ"
    SE = "SE"
    CH = "CH"
    SY = "SY"
    TW = "TW"
    TJ = "TJ"
    TZ = "TZ"
    TH = "TH"
    TL = "TL"
    TG = "TG"
    TK = "TK"
    TO = "TO"
    TT = "TT"
    TN = "TN"
    TR = "TR"
    TM = "TM"
    TC = "TC"
    TV = "TV"
    UG = "UG"
    UA = "UA"
    AE = "AE"
    GB = "GB"
    US = "US"
    UM = "UM"
    UY = "UY"
    UZ = "UZ"
    VU = "VU"
    VE = "VE"
    VN = "VN"
    VG = "VG"
    VI = "VI"
    WF = "WF"
    EH = "EH"
    YE = "YE"
    ZM = "ZM"
    ZW = "ZW"


class DayOfWeek(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_tariffs.asciidoc#141-dayofweek-enum
    '''

    monday = 'MONDAY'
    tuesday = 'TUESDAY'
    wednesday = 'WEDNESDAY'
    thursday = 'THURSDAY'
    friday = 'FRIDAY'
    saturday = 'SATURDAY'
    sunday = 'SUNDAY'


class ReservationRestrictionType(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_tariffs.asciidoc#143-reservationrestrictiontype-enum
    '''

    reservation = 'RESERVATION'
    reservation_expires = 'RESERVATION_EXPIRES'


class TariffDimensionType(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_tariffs.asciidoc#145-tariffdimensiontype-enum
    '''

    energy = 'ENERGY'
    flat = 'FLAT'
    parking_time = 'PARKING_TIME'
    time = 'TIME'


class TariffType(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_tariffs.asciidoc#147-tarifftype-enum
    '''

    ad_hoc_payment = 'AD_HOC_PAYMENT'
    profile_cheap = 'PROFILE_CHEAP'
    profile_fast = 'PROFILE_FAST'
    profile_green = 'PROFILE_GREEN'
    regular = 'REGULAR'


class ParkingRestriction(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_locations.asciidoc#1417-parkingrestriction-enum
    '''

    ev_only = 'EV_ONLY'
    plugged = 'PLUGGED'
    disables = 'DISABLED'
    customers = 'CUSTOMERS'
    motorcycle = 'MOTORCYCLES'


class ParkingType(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_locations.asciidoc#1418-parkingtype-enum
    '''

    along_motorway = 'ALONG_MOTORWAY'
    parking_garage = 'PARKING_GARAGE'
    parking_lot = 'PARKING_LOT'
    on_driveway = 'ON_DRIVEWAY'
    on_street = 'ON_STREET'
    underground_garage = 'UNDERGROUND_GARAGE'


class Facility(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_locations.asciidoc#1412-facility-enum
    '''

    hotel = 'HOTEL'
    restaurant = 'RESTAURANT'
    cafe = 'CAFE'
    mall = 'MALL'
    supermarket = 'SUPERMARKET'
    sport = 'SPORT'
    recreation_area = 'RECREATION_AREA'
    nature = 'NATURE'
    museum = 'MUSEUM'
    bike_sharing = 'BIKE_SHARING'
    bus_stop = 'BUS_STOP'
    taxi_stand = 'TAXI_STAND'
    tram_shop = 'TRAM_STOP'
    metro_station = 'METRO_STATION'
    train_station = 'TRAIN_STATION'
    airport = 'AIRPORT'
    parking_lot = 'PARKING_LOT'
    carpool_parking = 'CARPOOL_PARKING'
    fuel_station = 'FUEL_STATION'
    wifi = 'WIFI'


class Status(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_locations.asciidoc#1422-status-enum
    '''

    available = 'AVAILABLE'
    blocked = 'BLOCKED'
    charging = 'CHARGING'
    inoperative = 'INOPERATIVE'
    outoforder = 'OUTOFORDER'
    planned = 'PLANNED'
    removed = 'REMOVED'
    reserved = 'RESERVED'
    unknown = 'UNKNOWN'


class Capability(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_locations.asciidoc#143-capability-enum
    '''

    charging_profile_capable = 'CHARGING_PROFILE_CAPABLE'
    charging_preferences_capable = 'CHARGING_PREFERENCES_CAPABLE'
    chip_card_support = 'CHIP_CARD_SUPPORT'
    contactless_card_support = 'CONTACTLESS_CARD_SUPPORT'
    credit_card_payable = 'CREDIT_CARD_PAYABLE'
    debit_card_payable = 'DEBIT_CARD_PAYABLE'
    ped_terminal = 'PED_TERMINAL'
    remote_start_stop_capable = 'REMOTE_START_STOP_CAPABLE'
    reservable = 'RESERVABLE'
    rfid_reader = 'RFID_READER'
    start_session_connector_required = 'START_SESSION_CONNECTOR_REQUIRED'
    token_group_capable = 'TOKEN_GROUP_CAPABLE'
    unlook_capable = 'UNLOCK_CAPABLE'


class ImageCategory(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_locations.asciidoc#1416-imagecategory-enum
    '''

    charger = 'CHARGER'
    entrance = 'ENTRANCE'
    location = 'LOCATION'
    network = 'NETWORK'
    operator = 'OPERATOR'
    other = 'OTHER'
    owner = 'OWNER'


class EnergySourceCategory(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_locations.asciidoc#148-energysourcecategory-enum
    '''

    nuclear = 'NUCLEAR'
    general_fossil = 'GENERAL_FOSSIL'
    coal = 'COAL'
    gas = 'GAS'
    general_green = 'GENERAL_GREEN'
    solar = 'SOLAR'
    wind = 'WIND'
    water = 'WATER'


class EnvironmentalImpactCategory(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_locations.asciidoc#1410-environmentalimpactcategory-enum
    '''

    nuclear_waste = 'NUCLEAR_WASTE'
    carbon_dioxide = 'CARBON_DIOXIDE'


class TokenType(BaseEnum):
    '''
    https://github.com/ocpi/ocpi/blob/2.2.1/mod_tokens.asciidoc#144-tokentype-enum
    '''

    ad_hoc_user = 'AD_HOC_USER'
    app_user = 'APP_USER'
    other = 'OTHER'
    rfid = 'RFID'


class ConnectorType(BaseEnum):
    chademo = 'CHADEMO'
    chaoji = 'CHAOJI'
    domestic_a = 'DOMESTIC_A'
    domestic_b = 'DOMESTIC_B'
    domestic_c = 'DOMESTIC_C'
    domestic_d = 'DOMESTIC_D'
    domestic_e = 'DOMESTIC_E'
    domestic_f = 'DOMESTIC_F'
    domestic_g = 'DOMESTIC_G'
    domestic_h = 'DOMESTIC_H'
    domestic_i = 'DOMESTIC_I'
    domestic_j = 'DOMESTIC_J'
    domestic_k = 'DOMESTIC_K'
    domestic_l = 'DOMESTIC_L'
    domestic_m = 'DOMESTIC_M'
    domestic_n = 'DOMESTIC_N'
    domestic_o = 'DOMESTIC_O'
    gbt_ac = 'GBT_AC'
    gbt_dc = 'GBT_DC'
    iec_60309_2_single_16 = 'IEC_60309_2_single_16'
    iec_60309_2_three_16 = 'IEC_60309_2_three_16'
    iec_60309_2_three_32 = 'IEC_60309_2_three_32'
    iec_60309_2_three_64 = 'IEC_60309_2_three_64'
    iec_62196_t1 = 'IEC_62196_T1'
    iec_62196_t1_combo = 'IEC_62196_T1_COMBO'
    iec_62196_t2 = 'IEC_62196_T2'
    iec_62196_t2_combo = 'IEC_62196_T2_COMBO'
    iec_62196_t3a = 'IEC_62196_T3A'
    iec_62196_t3c = 'IEC_62196_T3C'
    nema_5_20 = 'NEMA_5_20'
    nema_6_30 = 'NEMA_6_30'
    nema_6_50 = 'NEMA_6_50'
    nema_10_30 = 'NEMA_10_30'
    nema_10_50 = 'NEMA_10_50'
    nema_14_30 = 'NEMA_14_30'
    nema_14_50 = 'NEMA_14_50'
    pantograph_bottom_up = 'PANTOGRAPH_BOTTOM_UP'
    pantograph_top_down = 'PANTOGRAPH_TOP_DOWN'
    tesla_r = 'TESLA_R'
    tesla_s = 'TESLA_S'


class ConnectorFormat(BaseEnum):
    socket = 'SOCKET'
    cable = 'CABLE'


class PowerType(BaseEnum):
    ac_1_phase = 'AC_1_PHASE'
    ac_2_phase = 'AC_2_PHASE'
    ac_2_phase_split = 'AC_2_PHASE_SPLIT'
    ac_3_phase = 'AC_3_PHASE'
    dc = 'DC'


class CommentStatus(TextChoices):
    SUCCESSFUL_CHARGING = 'SUCCESSFUL_CHARGING', 'Успешная зарядка'
    REPORT_PROBLEM = 'REPORT_PROBLEM', 'Сообщить о проблеме'
    CHARGING_IN_PROGRESS = 'CHARGING_IN_PROGRESS', 'Идет зарядка'
    WAITING_CHARGE = 'WAITING_CHARGE', 'Ожидание зарядки'


class AuthType(BaseEnum):
    phone = 'PHONE'
    vk = 'VK'
    apple = 'APPLE'
    google = 'GOOGLE'


class TypeField(Enum):
    success = 'SUCCESS'
    error = 'ERROR'


class Role(BaseEnum):
    cpo = 'CPO'
    emsp = 'EMSP'
    hub = 'HUB'
    nap = 'NAP'
    nsp = 'NSP'
    other = 'OTHER'
    scsp = 'SCSP'


class ConnectionStatus(BaseEnum):
    connected = 'CONNECTED'
    offline = 'OFFLINE'
    planned = 'PLANNED'
    suspended = 'SUSPENDED'


class InterfaceRole(BaseEnum):
    sender = 'SENDER'
    receiver = 'RECEIVER'


class ModuleID(BaseEnum):
    cdrs = 'cdrs'
    chargingprofiles = 'chargingprofiles'
    commands = 'commands'
    credentials = 'credentials'
    hubclientinfo = 'hubclientinfo'
    locations = 'locations'
    sessions = 'sessions'
    tariffs = 'tariffs'
    tokens = 'tokens'


class AuthMethod(BaseEnum):
    auth_request = 'AUTH_REQUEST'
    command = 'COMMAND'
    whitelist = 'WHITELIST'


class CdrDimensionType(BaseEnum):
    current = 'CURRENT'
    energy_export = 'ENERGY_EXPORT'
    energy_import = 'ENERGY_IMPORT'
    max_current = 'MAX_CURRENT'
    min_current = 'MIN_CURRENT'
    max_power = 'MAX_POWER'
    min_power = 'MIN_POWER'
    parking_time = 'PARKING_TIME'
    power = 'POWER'
    reservation_time = 'RESERVATION_TIME'
    state_of_charge = 'STATE_OF_CHARGE'
    time = 'TIME'


class SessionStatus(BaseEnum):
    active = 'ACTIVE'
    completed = 'COMPLETED'
    invalid = 'INVALID'
    pending = 'PENDING'
    reservation = 'RESERVATION'


class ProfileType(BaseEnum):
    cheap = 'CHEAP'
    fast = 'FAST'
    green = 'GREEN'
    regular = 'REGULAR'


class WhitelistType(BaseEnum):
    always = 'ALWAYS'
    allowed = 'ALLOWED'
    allowed_offline = 'ALLOWED_OFFLINE'
    never = 'NEVER'


class CommandType(BaseEnum):
    cancel_reservation = 'CANCEL_RESERVATION'
    reserve_now = 'RESERVE_NOW'
    start_session = 'START_SESSION'
    stop_session = 'STOP_SESSION'
    unlock_connector = 'UNLOCK_CONNECTOR'

aed = Currency('AED')

print('getting constant obj: ', aed)

print('getting it\'s value: ' + aed.value)


