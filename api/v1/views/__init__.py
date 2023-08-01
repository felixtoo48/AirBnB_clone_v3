#!/usr/bin/python3
"""initializing blueprint views"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *  # noqa
<<<<<<< HEAD
from api.v1.views.states import *  # noqa
from api.v1.views.cities import * # noqa
=======
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
>>>>>>> a9af52c83232e49d1ef85dbe8b695439f2d772bd
