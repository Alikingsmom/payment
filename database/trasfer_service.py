from database.models import Transaction, PayCategory, Card
from database import get_db


#transfer money
def money_transfer_db(card_from, card_to, amount, transaction_date):
    db = next(get_db())

    card_from_db = db.query(Card)._filter_by(card_number=card_from).first()
    card_to_db = db.query(Card)._filter_by(card_number=card_to).first()

    if card_from_db and card_to_db:
        if card_from_db.card_balance >= amount:
            card_from_db.card_balance -= amount
            card_to_db.card_balance += amount
            new_transaction = Transaction(card_from=card_from,
                                          card_to=card_to,
                                          amount=amount,
                                          transfer_time=transaction_date)

            db.add(new_transaction)
            db.commit()

            return True

        return 'Insufficient fund'

    return 'error code'
