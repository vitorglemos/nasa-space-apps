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
        #return self.blurred
    
    def filters(self):
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        #self.blurred = cv2.GaussianBlur(self.gray, (3, 3), 0)
        self.canny = cv2.Canny(self.gray, 350, 500, 10)
        plt.figure(figsize=(40, 40))
        plt.imshow(self.canny)
        self.find_contours()
    
    def find_contours(self):
        self.contours = cv2.findContours(self.canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.contours = self.contours[0] if len(self.contours) == 2 else self.contours[1]
        
    def draw_contours(self, c, color):
        cv2.drawContours(self.image, [c], 0, color, 1)
        
    def execute(self, point=(400, 300), tolerancy=100, r=100):
        count = 0
        k = 0
        self.raio = r
        self.tolerancy = tolerancy
        self.point = point

        
        self.limit_xi = self.point[0] - self.raio 
        self.limit_xj = self.point[0] + self.raio
        self.limit_yi = self.point[1] - self.raio
        self.limit_yj = self.point[1] + self.raio

        tolx1 = self.limit_xi + self.tolerancy
        tolx2 = self.limit_xj + self.tolerancy
        toly1 = self.limit_yi + self.tolerancy
        toly2 = self.limit_yj + self.tolerancy
        

        #k = cv2.circle(self.image, self.point, self.raio, self.red, 3)
        #print(':', x[1])
        for c in self.contours:
            count += 1
            black = (0, 0, 0)
            principal = (36,255,12)
            y = [c][0][0][0][0]
            x = [c][0][0][0][1]
            
            if (x >= self.limit_xi and x <= self.limit_xj):
                self.draw_contours(c, self.red)
                #cv2.drawContours(self.image,[c], 0, self.red, 1)
                
            elif ((x >= tolx2 and x <= tolx1) or (y >= toly1 and y <= toly2)):
                self.draw_contours(c, self.yellow)
               # cv2.drawContours(self.image, [c], 0, self.yellow, 1)
            else:
                self.draw_contours(c, self.green)
               # cv2.drawContours(self.image,[c], 0, self.green, 1)

            k = k + 1
            
if __name__ == "__main__":
    map_re = MapReview('data/map.png')
    image = map_re.get_images()
