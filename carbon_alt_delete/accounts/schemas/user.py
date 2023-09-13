from uuid import UUID

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: UUID
    company_id: UUID = Field(alias="companyId")
    first_name: str | None = Field(alias="firstName")
    last_name: str | None = Field(alias="lastName")
    email: EmailStr | None
    is_admin: bool = Field(alias="isAdmin")
    is_readonly: bool = Field(alias="isReadonly")
    is_consultant: bool = Field(alias="isConsultant")
