from flask import Blueprint, jsonify

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET"])
def login():
    return jsonify({"message": "Login API Ready"})

@auth.route("/register", methods=["GET"])
def register():
    return jsonify({"message": "Register API Ready"})