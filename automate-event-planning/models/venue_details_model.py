from pydantic import BaseModel


class VenueDetailsModel(BaseModel):
  name: str
  address: str
  capacity: int
  booking_status: str