from flask import Blueprint, request, jsonify
from app.services.investment_service import add_investment, list_investments, remove_investment, edit_investment
investment_bp = Blueprint("investment", __name__)

@investment_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()

    try:
        investment = add_investment(
            data["name"],
            data["type"],
            data["amount"],
            data["date"]
        )
        return jsonify({
            "id": investment.id,
            "name": investment.name,
            "type": investment.type,
            "amount": investment.amount,
            "date": str(investment.date)
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@investment_bp.route("/", methods=["GET"])
def index():
    investments = list_investments()
    return jsonify([
        {
            "id": inv.id,
            "name": inv.name,
            "type": inv.type,
            "amount": inv.amount,
            "date": str(inv.date)
        }
        for inv in investments
    ])


@investment_bp.route("/<int:investment_id>", methods=["DELETE"])
def delete(investment_id):
    try:
        investment = remove_investment(investment_id)
        return jsonify({
            "message": "Investimento deletado com sucesso",
            "id": investment.id
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 404


@investment_bp.route("/<int:investment_id>", methods=["PUT"])
def update_investment_route(investment_id):
    data = request.json
    investment = edit_investment(investment_id, data)
    if not investment:
        return jsonify({"message": "Investment not found"}), 404
    return jsonify({
        "id": investment.id,
        "name": investment.name,
        "type": investment.type,
        "amount": investment.amount,
        "date": investment.date.strftime("%Y-%m-%d")
    })
