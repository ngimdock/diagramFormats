from enum import Enum


class FormatType(str, Enum):
    CSV = "CSV"
    YAML = "YAML"
    TOML = "TOML"
    JSON = "JSON"
    XML = "XML"
    ASN_1 = "ASN.1"
    APACHE_AVRO = "Apache Avro"
    BSON = "BSON"
    CBOR = "CBOR"
    FLAT_BUFFERS = "FlatBuffers"
    FLEX_BUFFERS = "FlexBuffers"
    MICROSOFT_BOND = "Microsoft Bond"
    CAPTN_PROTO = "Capt'n Proto"
    MASSAGE_PACK = "MassagePack"
    PROCOLE_BUFFERS = "Protocol Buffers"
    APACHE_THRIFT = "Apache Thrift"


class UseArea(str, Enum):
    SPREAD_SHEET = "Spreadsheets"
    TELECAMMUNNICATION = "Telecammunications"
    WEB_APPLICATION = "Web Applications"
    SOFTWARE_CONFIGURATION = "Software Configuration"
    BIG_DATA = "Big Data"
    DATABASES = "Databases"
    INTERNET_OF_THINGS = "Internet of Things"
    GAMES = "Games"
    DISTRIBUTED_COMPUTING = "Distributed Computing"
