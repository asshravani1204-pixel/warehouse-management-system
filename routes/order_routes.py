from flask import Blueprint, request, jsonify
from models import db, Order, OrderItem, Product

order_bp = Blueprint('order', __name__)

# 🔹 GET all orders
@order_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    result = []

    for order in orders:
        items = OrderItem.query.filter_by(order_id=order.id).all()

        item_list = []
        for item in items:
            product = Product.query.get(item.product_id)

            item_list.append({
                "product_name": product.name,
                "quantity": item.quantity,
                "price": item.price_at_time
            })

        result.append({
            "order_id": order.id,
            "customer": order.customer_name,
            "status": order.status,
            "total_price": order.total_price,
            "items": item_list
        })

    return jsonify(result)


# 🔹 CREATE order
@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json

    order = Order(
        customer_name=data['customer_name'],
        customer_address=data['customer_address'],
        status="pending",
        total_price=0
    )

    db.session.add(order)
    db.session.flush()  # get order.id

    total_price = 0

    for item in data['items']:
        product = Product.query.get(item['product_id'])

        order_item = OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=item['quantity'],
            price_at_time=product.price
        )

        total_price += product.price * item['quantity']
        db.session.add(order_item)

    order.total_price = total_price

    db.session.commit()

    return jsonify({
        "message": "Order created successfully",
        "order_id": order.id,
        "order_date": order.created_at,
    })