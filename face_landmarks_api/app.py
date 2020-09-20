from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import face_recognizition_api as api
import logging

app = Flask(__name__)


@app.route('/getkeypts', methods=['POST'])
def get_keypts():
    try:
        image = request.files['file']
        logging.info("Image recieved")
        image = np.array(Image.open(image))
        result = api.get_encoding(image, type='image')
        return result
    except Exception:
        return "Something went wrong", 400

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0') 
