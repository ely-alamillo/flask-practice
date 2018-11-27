from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [{"name": "Flask Shop", "items": [{"name": "route", "price": "2.00"}]}]


@app.route("/test")
def home():
    return "hello world"


# POST store
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return jsonify(new_store)


# GET single store
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)

    return jsonify({"message": "store not found."})


# GET all stores
@app.route("/stores")
def get_stores():
    return jsonify({"stores": stores})


# POST item to store
@app.route("/store/<string:name>/item", methods=["POST"])
def create_store_item(name):
    for store in stores:
        if store["name"] == name:
            request_data = request.get_json()
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
    return jsonify({"message": "store not found."})


# GET item in store
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "store item not found."})


app.run(port=5000)
