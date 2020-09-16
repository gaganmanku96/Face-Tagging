import os
import pickle
import shutil
from time import time

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

from get_keypts import get_keypts


class Classify:
    def __init__(self):
        self.image_keypt_dict = {}
        self.used = []

    def __get_image_path(self):
        images_list = os.listdir('images')
        images_path = [os.path.join(os.getcwd(), 'images', image_name)
                       for image_name in images_list]
        return images_path
    
    def __train_knn_model(self, points, index, image_path):
        dir_name = 'group_' + str(index)

        try:
            os.mkdir(dir_name)
        except:
            dir_name = dir_name + str(time()).split('.')[-1]
            os.mkdir(dir_name)

        le = LabelEncoder()
        encoded_labels = le.fit_transform([dir_name])
        classifier = KNeighborsClassifier(n_neighbors=1,
                                          algorithm='ball_tree',
                                          weights='distance')
        # points = [list(points)]
        classifier.fit([points], encoded_labels)

        shutil.move(image_path, os.path.join(os.getcwd(), dir_name))
        with open(os.path.join(dir_name, "classifier.pkl"), 'wb') as file:
            pickle.dump((classifier), file)
        print("Classifier saved")
        return classifier, le

    def __generate_image_keypt(self, images_path):
        for path in images_path:
            key_pts = get_keypts(path)
            self.image_keypt_dict[path] = key_pts

    def __match_remaining(self, classifier, le):
        for path, keypts in self.image_keypt_dict.items():
            if path not in self.used and keypts is not None:
                closest_distance = classifier.kneighbors([keypts])
                is_recognized = [closest_distance[0][0][0] <= 0.5]
                if is_recognized[0]:
                    folder_name = le.inverse_transform(closest_distance[1][0])[0]
                    shutil.move(path, os.path.join(os.getcwd(), folder_name))
                    self.used.append(path)

    def get_key_points(self):
        images_path = self.__get_image_path()
        self.__generate_image_keypt(images_path)
        for index, (path, keypts) in enumerate(self.image_keypt_dict.items()):
            if keypts is not None and path not in self.used:
                self.used.append(path)
                classifier, le = self.__train_knn_model(keypts, index, path)
                self.__match_remaining(classifier, le)
            elif keypts is None:
                print(f"Keypoints not found for {path}")                

if __name__ == '__main__':
    classifier = Classify().get_key_points()
