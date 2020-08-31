from flask import Flask, request, jsonify
import numpy as np
import json
from PIL import Image
import face_recognizition_api as api

app = Flask(__name__)


@app.route('/getkeypts', methods=['POST'])
def get_keypts():
    result = "error"
    try:
        image = request.files['file']
        print("File recieved")
        image = np.array(Image.open(image))
        result = api.get_encoding(image, type='image')
    except Exception as e:
        print("Error in docker ")
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
