# server/controllers.py

from flask import jsonify, request
from .models import Plant

def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.serialize() for plant in plants])

def get_plant(id):
    plant = Plant.query.get_or_404(id)
    return jsonify(plant.serialize())

def create_plant():
    data = request.get_json()
    new_plant = Plant(**data)
    db.session.add(new_plant)
    db.session.commit()
    return jsonify(new_plant.serialize()), 201
