from uuid import UUID

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from carbon_alt_delete.activities.schemas.activity_category_type import (
    ActivityCategoryType,
)
from carbon_alt_delete.emission_factors.enums.value_mapping_field import (
    ValueMappingField,
)


class ValueMappingCreate(BaseModel):
    field: ValueMappingField
    keys: list[str | None]
    values: list[str | None | UUID] = []

    # Additional attributes
    activity_category_type: ActivityCategoryType | None
    field_id: UUID | None
    formula_term_value_name: str | None

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        alias_generator=to_camel,
    )


class ValueMappingUpdate(ValueMappingCreate):
    id: UUID


ValueMapping = ValueMappingUpdate
