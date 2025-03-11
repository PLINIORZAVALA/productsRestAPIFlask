# Importa las clases y funciones necesarias de Flask
from flask import Flask, jsonify, request
# Importa la lista de productos desde el archivo products.py
from products import products

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta básica para probar que la aplicación está funcionando
@app.route('/ping')
def ping():
    return "¡Hola, Mundo! Esta es mi primera aplicación Flask."

# Ruta para obtener un mensaje JSON de prueba
@app.route('/json', methods=['GET'])
def get_json():
    return jsonify({"message": "pong!"})

# Ruta para obtener todos los productos
@app.route('/products', methods=['GET'])
def get_products():
    # Devuelve un JSON con la lista de productos y un mensaje
    return jsonify({"products": products, "message": "Lista de productos"})

# Ruta para obtener un solo producto por su nombre
@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    # Busca el producto en la lista `products` que coincida con el nombre proporcionado
    productFound = [product for product in products if product['name'] == product_name]
    
    # Si se encuentra el producto, devuélvelo en formato JSON
    if (len(productFound) > 0):
        return jsonify({"product": productFound[0]})
    
    # Si no se encuentra el producto, devuelve un mensaje de error
    return jsonify({"message": "Product not found"})

# Ruta para agregar un nuevo producto usando el método POST
@app.route('/products', methods=['POST'])
def addProduct():
    # Crea un nuevo producto con los datos enviados en el cuerpo de la solicitud (JSON)
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    
    # Agrega el nuevo producto a la lista de productos
    products.append(new_product)
    
    # Devuelve un mensaje de éxito y la lista actualizada de productos
    return jsonify({"message": "Product Added Succesfully", "products": products})

# Ruta para actualizar los datos de un producto existente usando el método PUT
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    # Busca el producto en la lista `products` que coincida con el nombre proporcionado
    product_found = [product for product in products if product['name'] == product_name]
    
    # Si no se encuentra el producto, devuelve un error 404
    if not product_found:
        return jsonify({"message": "Product Not Found"}), 404
    
    # Obtiene el producto encontrado
    product = product_found[0]
    
    # Verifica que los campos necesarios (name, price, quantity) estén en el JSON de la solicitud
    if not all(key in request.json for key in ['name', 'price', 'quantity']):
        return jsonify({"message": "Missing required fields (name, price, quantity)"}), 400
    
    # Actualiza los datos del producto con los valores proporcionados en el JSON
    product['name'] = request.json['name']
    product['price'] = request.json['price']
    product['quantity'] = request.json['quantity']
    
    # Devuelve un mensaje de éxito y el producto actualizado
    return jsonify({
        "message": "Product Updated",
        "product": product
    })

# Ruta para eliminar un producto usando el método DELETE
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    # Busca el producto en la lista `products` que coincida con el nombre proporcionado
    product_found = [product for product in products if product['name'] == product_name]
    
    # Si no se encuentra el producto, devuelve un error 404
    if not product_found:
        return jsonify({"message": "Product Not Found"}), 404
    
    # Elimina el producto de la lista
    products.remove(product_found[0])
    
    # Devuelve un mensaje de éxito y la lista actualizada de productos
    return jsonify({
        "message": "Product Deleted",
        "products": products
    })

# Punto de entrada para ejecutar la aplicación Flask
if __name__ == "__main__":
    # Inicia la aplicación en modo debug en el puerto 5000
    app.run(debug=True, port=5000)

"""
LINK VIDIO YOUTUBE: https://youtu.be/Esdj9wlBOaI?si=wBPh8BXrtfp-SwbS
"""