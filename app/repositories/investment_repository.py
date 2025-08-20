from app.models.models import Investment
from app.extensions import db


def create_investment(name, type, amount, date):
    investment = Investment(
        name=name,
        type=type,
        amount=amount,
        date=date
    )
    db.session.add(investment)
    db.session.commit()
    return investment

def get_all_investments():
    return Investment.query.all()

def get_investment_by_id(investment_id):
    return Investment.query.get(investment_id)

def delete_investment(investment):
    db.session.delete(investment)
    db.session.commit()

def update_investment(investment_id, data):
    investment = Investment.query.get(investment_id)
    if not investment:
        return None

    investment.name = data.get("name", investment.name)
    investment.type = data.get("type", investment.type)
    investment.amount = data.get("amount", investment.amount)
    investment.date = data.get("date", investment.date)  # já é datetime.date

    db.session.commit()
    return investment

