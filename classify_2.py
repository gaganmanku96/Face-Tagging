import os

import pandas as pd
from sklearn.cluster import DBSCAN

from get_keypts import get_keypts


class Classify:
    def __init__(self):
        self._image_keypt_dict = {}
        self._path = 'images'
        self.df = None

    def _process_keypoints(self):
        for image in os.listdir(self._path):
            path = os.path.join(os.getcwd(), self._path, image)
            pts = get_keypts(path)
            if pts is not None:
                self._image_keypt_dict[image] = pts
        df = pd.DataFrame.from_dict(self._image_keypt_dict)
        self.df = df.transpose()
    
    def apply_algorithm(self):
        if self.df is None:
            self._process_keypoints()
        dbscan = DBSCAN()
        print(dbscan.fit_predict(self.df))


if __name__ == "__main__":
    obj = Classify()
    obj.apply_algorithm()
