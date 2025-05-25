import os
from flask import Flask
from routes import main

app = Flask(__name__)
app.register_blueprint(main)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Récupère le port fourni par Render ou 5000 par défaut
    app.run(host="0.0.0.0", port=port, debug=True)


