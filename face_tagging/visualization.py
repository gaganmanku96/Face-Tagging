import os

import matplotlib.pyplot as plt


def visualize(matched_pairs, images_path="assets/train_images"):

    if matched_pairs == []:
        raise ValueError("Empty List")
    
    n_rows = len(matched_pairs)

    for group, images in matched_pairs.items():
        fig = plt.figure(figsize=(10,10))
        fig.subplots_adjust(hspace=1.2)
        for idx, image in enumerate(images):
            img = plt.imread(os.path.join(images_path, image))
            ax = fig.add_subplot(n_rows, idx+1, idx+1)
            ax.title.set_text(group)
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            plt.imshow(img)
