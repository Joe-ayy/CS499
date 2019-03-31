import sys
import numpy as np
import cv2
import camera_ops as c_ops
import data_ops as d_ops
import file_ops as f_ops
import ml_model_ops as ml_ops


def main():
    # region ### Verify the existence and connection of web camera and the machine learning model ###
    # Remind the user to make sure the web camera is properly connected
    input("Make sure the web camera is connected. Press Enter to continue...")

    # Loop until the camera object is found
    while True:
        camera = c_ops.create_cam()

        # If the camera object isn't found, prompt the user to verify the camera is connected
        if c_ops.verify_cam(camera):
            print("Camera found.")
            break
        else:
            c_ops.destroy_cam(camera)
            user_resp = input("Web camera not found. Press Enter to try again or any other key to exit the program: ")
            if user_resp != '':
                # Camera not found and user wants to terminate the program
                sys.exit(1)

    # INSERT ML MODEL EXISTENCE AND CONNECTION IF APPLICABLE
    # endregion


if __name__ == "__main__":
    main()
