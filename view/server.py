from flask import Flask, request, jsonify
from marshmallow import ValidationError

from businsess_logic.order_usecases import order_create, order_get_many, order_get_by_id
from businsess_logic.product import Product
from data_access.product_repo import products
from view.order_schemas import OrderCreateDtoSchema, OrderSchema, OrderGetManyParams
from view.product_schemas import  Product_schema

app = Flask(__name__)


@app.post("/api/v1/order")
def order_create_endpoint():
    try:
        order_create_dto = OrderCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        order = order_create(
            product_ids=order_create_dto['product_ids']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return OrderSchema().dump(order)


@app.get("/api/v1/order")
def order_get_many_endpoint():
    try:
        order_get_many_params = OrderGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    order = order_get_many(
        page=order_get_many_params['page'],
        limit=order_get_many_params['limit'],
    )

    return OrderSchema(many=True).dump(order)


@app.get("/api/v1/order/<id>")
def order_get_by_id_endpoint(id):
    order = order_get_by_id(id)

    if order is None:
        return {
            "error": 'Not found'
        }, 404

    return OrderSchema().dump(order)



@app.post('/api/v1/products', methods=['POST'])
def create_product():
    product = Product_schema().load(request.json)
    products.append(product)
    return Product_schema().dump(product)

@app.get('/api/v1/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.get("/api/v1/product")
def get_products():
    return Product_schema(many=True).dump(products)

@app.get("/api/v1/product/<id>")
def get_product_by_id(id):
    product = None
    for i in products:
        if i['id'] == id:
            product = i
            break

    if product is None:
        return {
            "error": 'Not found'
        }, 404

    return Product_schema().dump(product)
def run_server():
    app.run()
