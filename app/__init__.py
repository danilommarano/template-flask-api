from flask import Flask

app = Flask(__name__)

# Configurações
app.config.from_object('config.settings')