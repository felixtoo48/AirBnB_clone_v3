#!/usr/bin/python3
<<<<<<< HEAD

"""
this file handles all default RESTFul API response 
"""

from api.v1.views import api_views
from flask import abort, jsonify, make_response, request
from flasgger import Swagger, swag_from
from models import storage, CNC

@app_views.route('/states', methods=['GET', 'POST'])
@swag_from('swagger_yaml/states_no_id.yml', methods=['GET', 'POST'])
def states_no_id():
    """
        states route to handle http method for requested states no id provided
    """
    if request.method == 'GET':
        all_states = storage.all('State')
        all_states = list(obj.to_json() for obj in all_states.values())
        return jsonify(all_states)

    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        if req_json.get("name") is None:
            abort(400, 'Missing name')
        State = CNC.get("State")
        new_object = State(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
@swag_from('swagger_yaml/states_id.yml', methods=['PUT', 'GET', 'DELETE'])
def states_with_id(state_id=None):
    """
        states route to handle http method for requested state by id
    """
    state_obj = storage.get('State', state_id)
    if state_obj is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(state_obj.to_json())

    if request.method == 'DELETE':
        state_obj.delete()
        del state_obj
        return jsonify({})

    if request.method == 'PUT':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        state_obj.bm_update(req_json)
        return jsonify(state_obj.to_json())
=======
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
>>>>>>> a9af52c83232e49d1ef85dbe8b695439f2d772bd
