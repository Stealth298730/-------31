from flask import Flask

from app.models.base import create_db
from app.models.pizza import Pizza
from app.models.position import Position
from app.routes.position import position_blueprint
from app.routes.pizzas import pizza_blueprint


app = Flask(__name__ , static_folder = "app.static" , template_folder = "app.templates") 
app.register_blueprint(position_blueprint)
app.register_blueprint(pizza_blueprint)

create_db()