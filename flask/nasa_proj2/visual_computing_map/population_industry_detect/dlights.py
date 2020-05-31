from imutils import contours
from skimage import measure
import numpy as np
import imutils
import cv2


class VisionManager():
    def __init__(self, path: str):
        self.image = cv2.imread(path)
        self.mask = None
        self.threshold = None
        self.gaussian = None
        self.gray = None
        self.gauss_x = 11
        self.gauss_y = 11
        self.thresh_x = 52
        self.thresh_y = 200

    def execute_detect(self):
        self.gray_filter()
        self.gaussian_filter(self.gauss_x, self.gauss_y)
        self.threshold_op(self.thresh_x, self.thresh_y)
        self.create_labels()
        self.get_circles_world()

    def save_image(self, output_path):
        cv2.imwrite(output_path, self.image)

    def create_labels(self):
        labels = measure.label(self.threshold,
                               connectivity=1)
        self.mask = np.zeros(self.threshold.shape,
                             dtype="uint8")
        for label in np.unique(labels):
            if label == 0:
                continue

            label_mask = np.zeros(self.threshold.shape, dtype="uint8")
            label_mask[labels == label] = 255
            num_pixels = cv2.countNonZero(label_mask)
            if num_pixels > 300:
                self.mask = cv2.add(self.mask, label_mask)

    def gray_filter(self):
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def gaussian_filter(self, x, y):
        self.gaussian = cv2.GaussianBlur(self.gray, (x, y), 0)

    def threshold_op(self, x, y):
        image_1 = cv2.threshold(self.gaussian, x, y, cv2.THRESH_BINARY)[1]
        self.threshold = cv2.dilate(cv2.erode(image_1, None, iterations=1),
                                    None, iterations=8)

    def find_lights_world(self):
        return contours.sort_contours(imutils.grab_contours(
            cv2.findContours(self.mask.copy(),
                             cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_SIMPLE)))[0]

    def get_circles_world(self):
        color = (255, 230, 0)
        for k in self.find_lights_world():
            (ki, li), radius = cv2.minEnclosingCircle(k)
            cv2.circle(self.image, (int(ki), int(li)),
                       int(radius), color, 1)


if __name__ == "__main__":
    image_list = ["data/region1.png",
                 "data/region2.png",
                 "data/region3.png",
                 "data/region4.png",
                 "data/region5.png",
                 "data/region6.png"]
    for index, image in enumerate(image_list):

        analytics = VisionManager(image)
        analytics.execute_detect()
        analytics.save_image(f"data/output_{index}.jpg")