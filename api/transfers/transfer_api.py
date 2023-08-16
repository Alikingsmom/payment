from main import app
from .transfer_models import P2PDent

# 2
@app.post('/api/transfer-money')
async def money_transfer(transfer_data: P2PDent):
    # transfer function
    result = transfer_data
    print(result)

    # if transfer successful than status
    return {'status': 1, 'message': result}


# function to get last transaction 3
@app.get('/api/monitoring')
async def user_payments(user_id: int, card_id: int = 0):
    pass
