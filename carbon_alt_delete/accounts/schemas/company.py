import datetime
from uuid import UUID

from pydantic import BaseModel, Field, NonNegativeInt


class Company(BaseModel):
    id: UUID
    name: str
    created_at: datetime.date = Field(alias="createdAt")
    is_consulting_company: bool = Field(alias="isConsultingCompany")
    is_demo_company: bool = Field(alias="isDemoCompany")
    available_client_companies: NonNegativeInt | None = Field(alias="availableClientCompanies")


class CompanyCreate(BaseModel):
    name: str
