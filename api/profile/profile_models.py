from pydantic import BaseModel
from datetime import datetime


# user's sign up
class UserDent(BaseModel):
    profile_photo: str
    name: str
    surname: str
    phone_number: str
    email: str
    city: str
    reg_date: datetime
    password: str


# user's card
class CardDent(BaseModel):
    card_number: int
    cardholder: str
    exp_date: int
    card_balance: float
    card_name: str

