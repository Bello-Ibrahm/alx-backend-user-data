#!/usr/bin/env python3
""" User View Module
"""
from api.v1.views import app_views
from flask import request, jsonify
from os import getenv
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login_session():
    ''' Handle user login with session
    '''
    email = request.form.get('email')
    if email is None or len(email.strip()) == 0:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if password is None or len(password) == 0:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if len(users) <= 0:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            res = jsonify(user.to_json())
            session_name = getenv('SESSION_NAME')
            res.set_cookie(session_name, session_id)
            return res
    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout_session():
    ''' Handle user logout session
    '''
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
