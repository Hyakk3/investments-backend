from app.extensions import db

class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)   # Nome do investimento
    type = db.Column(db.String(50), nullable=False)    # Tipo do investimento
    amount = db.Column(db.Float, nullable=False)       # Valor investido
    date = db.Column(db.Date, nullable=False)          # Data do investimento
