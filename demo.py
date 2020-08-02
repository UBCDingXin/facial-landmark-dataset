import cv2

from fmd.ds300w.dataset import DS300W
from fmd.mark_dataset.util import draw_marks


DATASET_DIR = "/home/robin/data/facial-marks/300W"

if __name__ == "__main__":
    # Construct a dataset.
    ds = DS300W("300w")

    # Populate the dataset with essential data, and see what we have got.
    ds.populate_dataset(DATASET_DIR)
    print(ds)

    # Randomly pick a sample and show the result.
    random_sample = ds.pick_one()
    lucky_image = random_sample.read_image()
    draw_marks(lucky_image, random_sample.marks)
    cv2.imshow("Preview", lucky_image)
    cv2.waitKey()

    # Loop through the dataset and show all the samples.
    for sample in ds.all_samples():
        image = sample.read_image()
        draw_marks(image, sample.marks)
        draw_marks(image, sample.get_key_marks(), color=(255, 0, 0))
        cv2.imshow("Preview", image)
        if cv2.waitKey(500) == 27:
            break