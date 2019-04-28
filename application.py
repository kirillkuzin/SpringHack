import os

from flask import Flask, request
from werkzeug.utils import secure_filename

import crypto
from fingerprint import FingerPrint

UPLOAD_FOLDER = "pictures"

application = Flask(__name__)

@application.route("/wallets", methods=["POST"])
def get_wallet():
    file = request.files['finger']
    filename = UPLOAD_FOLDER + "/" + secure_filename(file.filename)
    file.save(os.getcwd() + "/" + filename)
    finger_module = FingerPrint(filename)
    seed_phrase = finger_module.get_seed_phrase()
    private_key, public_key = crypto.generate_wallet(seed_phrase)
    return_data = {
        "seed": seed_phrase,
        "private_key": private_key,
        "public_key": public_key
    }
    return str(return_data), 200

if __name__ == "__main__":
    application.run(
        debug=True
    )
