import sys
import camera_ops as c_ops
import file_ops as f_ops
import ml_model_ops as ml_ops


def main():
    #model_name = "SVHN_model_multi.h5"
    filename = f_ops.generate_filename()
    for i in range(0, len(sys.argv)):
        # change file to output data to
        if sys.argv[i] == "-f":
            if sys.argv[i+1] != "":
                filename = sys.argv[i+1]
        # option to hide the command line output
        elif sys.argv[i] == "--hide-cl-output":
            ml_ops.cl_on = False
        # option to hide the display of the webcam
        elif sys.argv[i] == "--hide-webcam":
            ml_ops.cam_on = False

    # region ### Verify the existence and connection of web camera and the machine learning model ###
    # Remind the user to make sure the web camera is properly connected
    input("Make sure the web camera is connected. Press Enter to continue...")

    # Loop until the camera object is found
    while True:
        camera = c_ops.create_cam()

        # If the camera object isn't found, prompt the user to verify the camera is connected
        if c_ops.verify_cam(camera):
            print("Camera found. Press q while hovering over camera view to exit program.")
            break
        else:
            c_ops.destroy_cam(camera)
            user_resp = input("Web camera not found. Press Enter to try again or any other key to exit the program: ")
            if user_resp != '':
                # Camera not found and user wants to terminate the program
                sys.exit(1)

    # INSERT ML MODEL EXISTENCE AND CONNECTION IF APPLICABLE

    # Run the YOLO/Darknet software on the model
    # ml_ops.run_model_YOLO(model_name, filename)

    # OR

    # Run the model on an image stream using OpenCV
    # ml_ops.run_model_cam(filename, camera)
    # endregion
    sys.exit(0)

if __name__ == "__main__":
    main()
