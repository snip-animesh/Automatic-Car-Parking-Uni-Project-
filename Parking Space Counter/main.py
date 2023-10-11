import cv2
import pickle
import cvzone
import numpy as np

# Video feed
cap = cv2.VideoCapture(0)


with open("CarParkPos", 'rb') as f:
    posList = pickle.load(f)

WIDTH, HEIGHT = 80,35
kernel = np.ones((3, 3), np.uint8)
CarYes = (0, 0, 255)
CarNo = (210, 230, 37)
TextColor = (230, 98, 37)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
bgWidth , bgHeight = 1280 , 720
CAR_PIXEL = 1100


def check_parking_space(imgPro,img,imgBG):
    spaceCounter = 0
    parks = []
    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y:y + HEIGHT, x:x + WIDTH]
        # cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)


        if count < CAR_PIXEL  :
            Color = CarNo
            thickness = 2
            if posList.index(pos) !=0 and posList.index(pos) !=1:
                spaceCounter += 1
            parks.append(0)
        else:
            Color = CarYes
            thickness = 2
            parks.append(1)
        cv2.rectangle(img, pos, (pos[0] + WIDTH, pos[1] + HEIGHT), color=Color, thickness=thickness)
        cvzone.putTextRect(img, str(count), (x, y + HEIGHT - 5), scale=1,
                           thickness=2, offset=0)

    cvzone.putTextRect(img, f'Free: {str(spaceCounter)}/{len(posList)-2}', (30, 50), scale=2,
                       thickness=3, offset=10, colorR=TextColor)
    # Putting counted value on background image
    cv2.putText(imgBG, str(len(posList)), (1120, 355), cv2.FONT_ITALIC, 1, GREEN, thickness=3)
    cv2.putText(imgBG, str(spaceCounter), (1120, 415), cv2.FONT_ITALIC,1,RED,thickness=3)
    return parks


def run():
        success, img = cap.read()
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(
                cv2.CAP_PROP_FRAME_COUNT):  # if current frame == total num of frame
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # setting current frame to 0

        # importing background Image
        imgBackground = cv2.imread('Resources/background.png')
        # resize the image
        imgBackground = cv2.resize(imgBackground, (bgWidth, bgHeight), interpolation=cv2.INTER_LINEAR)

        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV, 15, 4)
        imgMedian = cv2.medianBlur(imgThreshold, 1)

        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

        parks=check_parking_space(imgDilate,img,imgBackground)

        # Placing CCTV footage to background image
        imgResize = cv2.resize(img, (695, 341))  # width & height
        imgBackground[178:519, 132:827] = imgResize  # height & width

        cv2.imshow("CCTV", imgBackground)
        # cv2.imshow("ImageDilate", imgDilate)
        cv2.waitKey(10)
        return parks


if __name__=="__main__":
    while True:
        run()