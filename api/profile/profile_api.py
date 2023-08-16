from fastapi import Body


from main import app
from.profile_models import UserDent, CardDent


# registration
@app.post('/api/register-user')
async def user_registration(user_data: UserDent):
    print(user_data)

    # after registration will be given user id
    return {'status': 1, 'message': 'Registration Completed'}


# Sign in to account
@app.post('/api/login-user')
async def login_user(phone_number: int = Body(), password: str = Body()):
    # check data
    checker = None

    # if data correct send user id and user data
    return {'status': 1, 'message': 'Logged in'}


# adding card
@app.post('/api/add-card')
async def add_user_card(card_data: CardDent):
    #calldata for adding card to base
    result = card_data
    print(card_data)

    #if card adding successfully than status
    return {'status': 1, 'message': result}


# get user profile on front
@app.get('/api/user-data')
async def get_user_data(user_id: int):
    pass


# get exact user card or all cards 1
@app.get('/api/user-cards')
async def get_user_cards(user_id: int, card_id: int=0):
    pass
