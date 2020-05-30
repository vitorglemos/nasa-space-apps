import cv2
import matplotlib.pyplot as plt

class MapReview():
    def __init__(self, path_image):
        self.image = cv2.imread(path_image)
        self.red = (255, 0, 0)
        self.yellow = (255, 192, 14)
        self.green = (55, 255, 14)
        self.original = None
        self.gray = None
        self.thresh = None
        self.blurred = None
        self.canny = None
        self.contours = None
        self.filters()
        self.execute()
     
    def get_images(self):
        return self.image
    
    def filters(self):
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.blurred = cv2.GaussianBlur(self.gray, (3, 3), 0)
        self.canny = cv2.Canny(self.blurred, 50, 200, 10)
        self.find_contours()
    
    def find_contours(self):
        self.contours = cv2.findContours(self.canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.contours = self.contours[0] if len(self.contours) == 2 else self.contours[1]
        
    def execute(self):
        count = 0
        k = 0

        my = [400, 300]
        limitx1 = my[0] + 50
        limitx2 = my[0] - 50
        limity1 = my[1] + 50
        limity2 = my[1] - 50

        tolx1 = my[0] + 50 + 15
        tolx2 = my[0] - 50 - 15
        toly1 = my[1] + 50 + 15
        toly2 = my[1] - 50 - 15
        for c in self.contours:
            count += 1
            black = (0, 0, 0)
            principal = (36,255,12)
            x1 = [c][0][0][0][0]
            y1 = [c][0][0][0][1]
    
            if ((x1 >= limitx2 and x1 <= limitx1) or (y1 >= limity1 and y1 <= limity2)):
                cv2.drawContours(self.image,[c], 0, self.red, 1)
            elif ((x1 >= tolx2 and x1 <= tolx1) or (y1 >= toly1 and y1 <= toly2)):
                cv2.drawContours(self.image,[c], 0, self.yellow, 1)
            else:
                cv2.drawContours(self.image,[c], 0, self.green, 1)

            k = k + 1
            
if __name__ == "__main__":            
    map_re = MapReview('data/map.png')
    image = map_re.get_images()
