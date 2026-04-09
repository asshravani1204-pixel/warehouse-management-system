from flask import Flask
from flask_cors import CORS
from models import db

app = Flask(__name__)
CORS(app)

# 🔧 Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
from routes.order_routes import order_bp

app.register_blueprint(order_bp)

# 🏠 Test route
@app.route('/')
def home():
    return {"message": "Backend running"}

# 🚀 Run server + create DB
if __name__ == '__main__':
    with app.app_context():   # 👈 THIS is where that code goes
        db.create_all()       # 👈 creates database.db

    app.run(debug=True)
    
    from routes.order_routes import order_bp
app.register_blueprint(order_bp)