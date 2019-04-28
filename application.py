import os
import json

from flask import Flask, Response, request

import crypto
from fingerprint import FingerPrint

UPLOAD_FOLDER = "pictures"

application = Flask(__name__)

@application.route("/wallets", methods=["POST"])
def get_wallet():
    file = request.files['finger']
    filename = UPLOAD_FOLDER + "/" + file.filename
    file.save(os.getcwd() + "/" + filename)
    finger_module = FingerPrint(filename)
    seed_phrase = finger_module.get_seed_phrase()
    private_key, public_key = crypto.generate_wallet(seed_phrase)
    return_data = json.dumps({
        "seed": seed_phrase,
        "private_key": private_key,
        "public_key": public_key,
        "balance": crypto.get_balance(public_key)
    })
    return Response(return_data, mimetype="application/json"), 200

if __name__ == "__main__":
    application.run(
        host="0.0.0.0",
        port=int(os.environ.get('PORT', 5000)),
        debug=True
    )
