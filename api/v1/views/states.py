#!/usr/bin/python3
"""creates a new view for State objects"""
from models import storage
from models.state import State
from flask import Flask, abort, request, jsonify, Blueprint

states = Blueprint("states", __name__)


@states.route('/states', methods=['GET'], strict_slashes=False)
def get_state():
    """ retrieves the list of all State obj """
    all_state = []
    states = storage.all("State").values()
    for s in states:
        all_state.append(s.to_dict())
    return jsonify(all_state)


<<<<<<< HEAD
@states.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
=======
@app_views.route('/states/<state_id>', methods=['GET'])
>>>>>>> parent of 1576752... Revert "updated"
def get_id(state_id):
    """ retrieves State object """
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


<<<<<<< HEAD
@states.route('/states/<state_id>', methods=['DELETE'],
              strict_slashes=False)
=======
@app_views.route('/states/<state_id>', methods=['DELETE'])
>>>>>>> parent of 1576752... Revert "updated"
def delete_state(state_id):
    """ delete State object if no id """
    state = storage.get("State", state_id)
    empty = {}
    if state is None:
        abort(404)

    state.delete()
    storage.save()
    storage.close()
    return (jsonify(empty), 200)


@states.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """ creates State object """
    req = request.get_json()
    if req is None:
        abort(400, "Not a JSON")
    if "name" not is req:
        abort(400, "Missing name")
    state = State(**req)
    storage.new(state)
    state.save()
    storage.close()
    return (jsonify(state.to_dict()), 201)


<<<<<<< HEAD
@states.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
=======
@app_views.route('/states/<state_id>', methods=['PUT'])
>>>>>>> parent of 1576752... Revert "updated"
def update_state(state_id):
    """update"""
    req = request.get_json()
    state = storage.get("State", state_id)
    if req is None:
        abort(400, "Not a JSON")
    if state is None:
        abort(404)
    ignore_keys = ["id", "created_at", "updated_at"]
    for key, value in req.items():
        if key not in ignore_keys:
            setattr(state, key, value)
    state.save()
    storage.close()
    return jsonify(state.to_dict()), 200
