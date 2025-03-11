from flask import Flask, jsonify, request
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

# Ruta para obtener un solo dato del archivo json
@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        return jsonify({"product": productFound[0]})
    return jsonify({"message": "Product not found"})

# Ruta con metodo POST para agregar productos
@app.route('/products', methods = ['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Succesfully", "products": products})

# Ruta para actualizar los datos de un producto
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    if not product_found:
        return jsonify({"message": "Product Not Found"}), 404
    product = product_found[0]
    if not all(key in request.json for key in ['name', 'price', 'quantity']):
        return jsonify({"message": "Missing required fields (name, price, quantity)"}), 400
    product['name'] = request.json['name']
    product['price'] = request.json['price']
    product['quantity'] = request.json['quantity']
    return jsonify({
        "message": "Product Updated",
        "product": product
    })

# Ruta para eliminar un productos
# Ruta para eliminar un producto
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    if not product_found:
        return jsonify({"message": "Product Not Found"}), 404
    products.remove(product_found[0])
    return jsonify({
        "message": "Product Deleted",
        "products": products
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)