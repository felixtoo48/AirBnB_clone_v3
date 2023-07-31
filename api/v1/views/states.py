#!/usr/bin/python3
"""state"""

from flask import jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route("states", methods=["GET"], strict_slashes=False)
def get_states():
    """retrieves the list of all state objects"""
    states = storage.all(State).values()

    return jsonify([state.to_dict() for state in states])


@app_views.route("states/<state_id>", methods=["GET"], strict_slashes=False)
def get_state(state_id):
    """ returns a state object"""
    state = storage.get(State, state_id)

    if state:
        return jsonify(state.to_dict())
    else:
        abort(404)


@app_views.route("states/<state_id>", methods=["DELETE"], strict_slashes=False)
def delete_state(state_id):
    """deletes a state object"""
    state = storage.get(State, state_id)

    if state:
        storage.delete(state)
        storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route("states", methods=["POST"], strict_slashes=False)
def create_state():
    """ creates a state"""
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    state = State(**data)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201


@app_views.route("states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """updates a state object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
