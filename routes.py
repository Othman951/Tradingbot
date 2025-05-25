from flask import Blueprint, jsonify
import requests

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "Hello World from Flask!"

@main.route("/dexscreener-price/<pair>")
def dexscreener_price(pair):
    url = f"https://api.dexscreener.com/latest/dex/pairs/{pair}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Impossible de récupérer les données"}), 500



