from app.repositories.investment_repository import (
    create_investment,
    get_all_investments,
    get_investment_by_id,
    delete_investment,
    update_investment
)
from datetime import datetime, date as date_cls

VALID_TYPES = ["Ação", "Fundo", "Título"]

def add_investment(name, type, amount, date_str):
    if not name or not type:
        raise ValueError("Nome e tipo do investimento são obrigatórios")

    if type not in VALID_TYPES:
        raise ValueError(f"Tipo inválido. Use um dos seguintes: {', '.join(VALID_TYPES)}")

    if amount <= 0:
        raise ValueError("O valor deve ser positivo")

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Data inválida, use o formato YYYY-MM-DD")

    if date > date_cls.today():
        raise ValueError("A data não pode estar no futuro")

    return create_investment(name, type, amount, date)

def list_investments():
    return get_all_investments()

def remove_investment(investment_id):
    investment = get_investment_by_id(investment_id)
    if not investment:
        raise ValueError("Investimento não encontrado")
    delete_investment(investment)
    return investment

def edit_investment(investment_id, data):
    # Faz uma cópia para não mutar o dicionário original
    updated_data = data.copy()

    # Se veio "date" no JSON, converte
    if "date" in updated_data:
        try:
            updated_data["date"] = datetime.strptime(updated_data["date"], "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Data inválida, use o formato YYYY-MM-DD")

    return update_investment(investment_id, updated_data)
