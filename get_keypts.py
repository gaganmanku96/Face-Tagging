import requests
import json
import re

import numpy as np

URL = 'http://0.0.0.0:5000/getkeypts'


def get_keypts(image, method='docker'):
    if method == 'docker':
        f = {'file': open(image, 'rb').read()}
        result = requests.post(URL, files=f)
        if result.status_code == 200:
            try:
                keypts = json.loads(result.text)['points']
                keypts = np.array(keypts).reshape((1,-1))[0]
                return keypts
            except:
                return None
        else:
            print("Something went wrong while trying to get keypts")
            return None