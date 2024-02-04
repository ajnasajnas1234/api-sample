
# import
# create an application
# create another funtion to read the content from the json file
# here open the file and use the name,next write in which mode we want the data to display(read,write,or both) "as file" used to assign the get data 
# next i need to written the content after read 
# return using load and refer to the file 
# rout function handle ,what to return when a function call
# return the above product
# next need to return the data into front end
# to return into front end need to convert into json
# jsonify used to convert 


from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def load_products():
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)

@app.route('/', methods=['GET'])
def hello():
    return "hello"

@app.route('/products', methods=['GET'])
def get_products():
    data = load_products()
    return jsonify(data)

def save_products_data(products):
    with open('products.json', 'w') as file:
        json.dump(products, file, indent=4)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    products = load_products()
    product = None
    
    for p in products:
        if p["id"] == product_id:
            product = p
            break
    return jsonify(product) if product else ('product not found', 404)

@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.json
    
    products = load_products()
    products.append(new_product) 
    save_products_data(products) 

    return new_product  


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    products = load_products()
    product = None
    
    for p in products:
        if p["id"] == product_id:
            product = p
            break
    update_product = request.json
    product.update(update_product)
    save_products_data(products) 

    return update_product



@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    products = load_products()

    updated_list = list(filter(lambda p: p["id"] != product_id, products))
    save_products_data(updated_list) 
   
    return "Successfully Deleted",204

app.run(debug=True)

