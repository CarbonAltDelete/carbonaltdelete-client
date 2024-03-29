from uuid import UUID

from pydantic import BaseModel, Field, EmailStr, ConfigDict

from carbon_alt_delete.accounts.enums.user_status import UserStatus


class User(BaseModel):
    id: UUID
    company_id: UUID = Field(alias="companyId")
    first_name: str | None = Field(alias="firstName")
    last_name: str | None = Field(alias="lastName")
    email: EmailStr | None
    is_admin: bool = Field(alias="isAdmin")
    is_readonly: bool = Field(alias="isReadonly")
    is_readonly_limited: bool = Field(alias="isReadonlyLimited")
    is_consultant: bool = Field(alias="isConsultant")
    status: UserStatus


class UserCreate(BaseModel):
    company_id: UUID = Field(alias="companyId")
    first_name: str | None = Field(alias="firstName")
    last_name: str | None = Field(alias="lastName")
    email: EmailStr | None
    is_admin: bool = Field(alias="isAdmin", default=False)
    is_readonly: bool = Field(alias="isReadonly", default=False)
    is_readonly_limited: bool = Field(alias="isReadonlyLimited", default=False)

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )
