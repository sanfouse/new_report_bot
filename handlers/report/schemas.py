from pydantic import BaseModel


class ReportSchema(BaseModel):
    route_number: str | None
    date: str | None
    time: str | None
    car_numbers: str | None
    route: str | None
    report: str | None
    email: str | None
    telegram: str | None