from flask import Flask, request, jsonify
import random

# creating a Flask app 
app = Flask(__name__)

# hard-coded list of names 
apps = ["Evony: The King's Return","Lords Mobile: Kingdom Wars","Clash of Clans"]


# Returns a JSON response with the chosen app name or an error message if the list is empty.
@app.route("/suggest_app", methods=["GET"])
def get_apps():
    try:
        if not apps:
            raise  IndexError("No apps available.")

        chosen_app = random.choice(apps)
        response = {"app_name": chosen_app}
        return jsonify(response)

    except IndexError as e:
        return jsonify({'error': str(e)}), 404


# Error handler for 404 (Not Found) status code.
# Returns a JSON response with an appropriate error message.
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Sorry, the requested URL was not found on this server.'}), 404