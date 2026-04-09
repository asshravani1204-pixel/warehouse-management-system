from flask import Blueprint, request, jsonify
from models import db, Product

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json

    new_product = Product(
        name=data['name'],
        category=data['category'],
        price=data['price'],
        description=data.get('description')
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product added"}), 201


@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()

    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "category": p.category,
            "price": p.price
        })

    return jsonify(result)