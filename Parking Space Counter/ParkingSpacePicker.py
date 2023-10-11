import cv2
import pickle

cap=cv2.VideoCapture(0)

# width and height of one parking slot
WIDTH, HEIGHT = 80,35

try:
    with open("CarParkPos", 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


def mouse_click(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    elif events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + WIDTH and y1 < y < y1 + HEIGHT:
                posList.pop(i)
    with open("CarParkPos", "wb") as f:
        pickle.dump(posList, f)


while True:
    succ,img = cap.read()
    img = cv2.resize(img, (695, 341))  # width & height
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + WIDTH, pos[1] + HEIGHT), (230, 230, 41), 2)
    cv2.imshow('Image', img)
    # to detect mouse click
    cv2.setMouseCallback("Image", mouse_click)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
