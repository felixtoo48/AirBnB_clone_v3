#!/usr/bin/python3
"""places amenities view module"""

from flask import jsonify, abort
from models import storage
from models.place import Place
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def get_amenities_from_place(place_id):
    """Retrieves the list of all Amenity objects of a Place"""
    place = storage.get(Place, place_id)
    if place:
        amenities = [amenity.to_dict() for amenity in place.amenities]
        return jsonify(amenities)
    else:
        abort(404)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_amenity_from_place(place_id, amenity_id):
    """Deletes a Amenity object from a Place"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if place is None or amenity is None:
        abort(404)
    if storage == "db":
        if amenity not in place.amenities:
            abort(404)
        place.amenities.remove(amenity)
        storage.save()
    else:
        amenity_ids = place.amenity_ids
        if amenity_id not in amenity_ids:
            abort(404)
        amenity_ids.remove(amenity_id)
        place.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['POST'], strict_slashes=False)
def link_amenity_to_place(place_id, amenity_id):
    """Link a Amenity object to a Place"""
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)
    if place is None or amenity is None:
        abort(404)
    if storage == "db":
        if amenity in place.amenities:
            return jsonify(amenity.to_dict()), 200
        place.amenities.append(amenity)
        storage.save()
    else:
        amenity_ids = place.amenity_ids
        if amenity_id in amenity_ids:
            return jsonify(amenity.to_dict()), 200
        amenity_ids.append(amenity_id)
        place.save()
    return jsonify(amenity.to_dict()), 201
