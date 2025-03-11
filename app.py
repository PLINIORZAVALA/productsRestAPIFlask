from flask import Flask, jsonify
from products import products  # Importa la lista de productos

app = Flask(__name__)

@app.route('/ping')
def ping():
    return "¡Hola, Mundo! Esta es mi primera aplicación Flask."

# Ruta para obtener los datos del json
@app.route('/json', methods=['GET'])
def get_json():
    return jsonify({"message": "pong!"})

# Ruta para obtener todos los productos
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": products, "message": "Lista de productos"})#objeto con lista de productos

# Ruta para obtener un solo datos del archivo json
@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    print(product_name)
    return 'received'

if __name__ == "__main__":
    app.run(debug=True, port=5000)