import cv2
import numpy as np
from imutils.video import filevideostream
from yolodetect import YoloDetect

# Chua cac diem nguoi dung chon de tao da giac
points = []
# new model Yolo
model = YoloDetect()


def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])

def draw_polygon(frame, points):
    for point in points:
        frame = cv2.circle( frame, (point[0], point[1]), 5, (0,0,255), -1)
    # print(points)

    frame = cv2.polylines(frame, [np.int32(points)], False, (255,0, 0), thickness=2)
    return frame

detect = False

path = 'bienso.mp4'
cap = cv2.VideoCapture(path)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret ==True:
    #   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = draw_polygon(frame, points)
        if detect:
            frame = model.detect(frame,points)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('d'):
            points.append(points[0])
            detect = True

        cv2.imshow("Intrusion Warning", frame)
        cv2.setMouseCallback('Intrusion Warning', handle_left_click, points)
    else:
        break
    # Hien anh ra man hinh
    
cap.release()
cv2.destroyAllWindows()
