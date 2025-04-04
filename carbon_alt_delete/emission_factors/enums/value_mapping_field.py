from enum import Enum


class ValueMappingField(str, Enum):
    KEYWORD_ATTRIBUTE_UNIT = "keywordAttributeUnit"
    UNIT = "UNIT"
    ORGANIZATIONAL_UNIT = "organizationUnit"
    TRADED_FROM_ORGANIZATIONAL_UNIT = "tradedFromOrganizationalUnit"
    ACTIVITY_CATEGORY = "activityCategory"
    TRIP_TYPE = "go_and_return"
    OPTION = "OPTION"
    VOLUME_UNCERTAINTY = "VOLUME_UNCERTAINTY"
    EMISSION_FACTOR_FINGERPRINT = "EMISSION_FACTOR_FINGERPRINT"
