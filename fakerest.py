from flask import Flask, jsonify


app = Flask(__name__)

USER = {"id": 1,
        "firstname": "John",
        "lastname": "Doe",
        "timezone": "America/Montreal",
        "language": "fr_FR",
        "description": "The most common name in America",
        "caller_id": "Johnny",
        "outgoing_caller_id": "default",
        "mobile_phone_number": "5554151234",
        "username": "john",
        "password": "supersecretpassword",
        "music_on_hold": "waiting",
        "preprocess_subroutine": "ivr",
        "userfield": "",
        "links": [{
            "rel": "users",
            "href": "https://xivoserver/1.1/users/1"
        }]}

EXTENSION = {
    "id": 1,
    "context": "default",
    "exten": "1234",
    "commented": False,
    "links": [{
        "rel": "extensions",
        "href": "https://xivoserver/1.1/extensions/1"
    }]}


@app.route('/1.1/users', methods=['POST'])
def create_user():
    return jsonify(**USER)


@app.route('/1.1/users', methods=['GET'])
def list_users():
    return jsonify(total=2, items=[USER, USER])


@app.route('/1.1/users/<int:user_id>')
def get_user(user_id):
    return jsonify(**USER)


@app.route('/1.1/users/<int:user_id>', methods=['PUT', 'DELETE'])
def modify_user(user_id):
    return ('', 204)


@app.route('/1.1/extensions', methods=['POST'])
def create_extension():
    return jsonify(**EXTENSION)


@app.route('/1.1/extensions', methods=['GET'])
def list_extensions():
    return jsonify(total=2, items=[EXTENSION, EXTENSION])


@app.route('/1.1/extensions/<int:extension_id>')
def get_extension(extension_id):
    return jsonify(**EXTENSION)


@app.route('/1.1/extensions/<int:extension_id>', methods=['PUT', 'DELETE'])
def modify_extension(extension_id):
    return ('', 204)


if __name__ == "__main__":
    app.run(port=9486, debug=True)
