import cv2
import time


# starting a webcam.
video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None

while True:
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    cv2.imshow("My video", gray_frame_gau)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("My video", thresh_frame)

    contours, check = cv2.findContours(
        dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()