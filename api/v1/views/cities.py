<<<<<<< HEAD
i!/usr/bin/python3

"""
This create a new view for Cities objects that handles all default RESTFul API actions
"""

from api.v1.views import api_view
from flask import abort, jsonify, make_response, request
from flasgger import swagger, swag_from
from model import storage, CNC

@app_views.route('/state/<state_id>/cities', method=['GET','POST'])
@swag_from('swagger_yaml/cities_by_state.yml', methods=['GET', 'POST'])
def cities_per_state(state_id=None):
    """
        cities route to handle http method for requested cities by state
    """
    state_obj = storage.get('State', state_id)
    if state_obj is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        all_cities = storage.all('City')
        state_cities = [obj.to_json() for obj in all_cities.values()
                        if obj.state_id == state_id]
        return jsonify(state_cities)

    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        if req_json.get("name") is None:
            abort(400, 'Missing name')
        City = CNC.get("City")
        req_json['state_id'] = state_id
        new_object = City(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201


@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'])
@swag_from('swagger_yaml/cities_id.yml', methods=['GET', 'DELETE', 'PUT'])
def cities_with_id(city_id=None):
    """
        cities route to handle http methods for given city
    """
    city_obj = storage.get('City', city_id)
    if city_obj is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(city_obj.to_json())

    if request.method == 'DELETE':
        city_obj.delete()
        del city_obj
        return jsonify({}), 200

    if request.method == 'PUT':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        city_obj.bm_update(req_json)
        return jsonify(city_obj.to_json()), 200
=======
#!/usr/bin/python3
"""city"""

from flask import jsonify, abort, request
from models import storage
from models.city import City
from models.state import State
from api.v1.views import app_views


@app_views.route("states/<state_id>/cities", methods=["GET"],
                 strict_slashes=False)
def get_cities(state_id):
    """retrieves the list of all city objects of a state"""
    state = storage.get(State, state_id)
    if state:
        cities = [city.to_dict() for city in state.cities]
        return jsonify(cities)
    else:
        abort(404)


@app_views.route("cities/<city_id>", methods=["GET"], strict_slashes=False)
def get_city(city_id):
    """ returns a city object"""
    city = storage.get(City, city_id)

    if city:
        return jsonify(city.to_dict())
    else:
        abort(404)


@app_views.route("cities/<city_id>", methods=["DELETE"], strict_slashes=False)
def delete_city(city_id):
    """deletes a city object"""
    city = storage.get(City, city_id)

    if city:
        storage.delete(city)
        storage.save()
        return jsonify({})
    else:
        abort(404)


@app_views.route("states/<state_id>/cities", methods=["POST"],
                 strict_slashes=False)
def create_city(state_id):
    """ creates a city"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    data['state_id'] = state_id
    city = City(**data)
    storage.new(city)
    storage.save()
    return jsonify(city.to_dict()), 201


@app_views.route("cities/<city_id>", methods=["PUT"], strict_slashes=False)
def update_city(city_id):
    """updates a city object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    ignore_keys = ['id', 'state_id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(city, key, value)
    storage.save()
    return jsonify(city.to_dict()), 200
>>>>>>> a9af52c83232e49d1ef85dbe8b695439f2d772bd
