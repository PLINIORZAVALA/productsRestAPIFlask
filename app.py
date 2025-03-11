from flask import Flask, jsonify
from products import products  # Importa la lista de productos

app = Flask(__name__)

@app.route('/ping')
def ping():
    return "¡Hola, Mundo! Esta es mi primera aplicación Flask."

# Ruta para obtener todos los productos
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True, port=5000)