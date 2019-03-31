import numpy as np
import cv2


def create_cam():
    # Return a video camera object
    return cv2.VideoCapture(0)


def destroy_cam(web_cam):
    # Release a video camera object
    web_cam.release()


def verify_cam(web_cam):
    # Check to make sure the web camera is connected
    if web_cam.isOpened():
        return True
    else:
        return False
