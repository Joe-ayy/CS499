from subprocess import Popen, PIPE
import camera_ops
import file_ops as f_ops

cl_on = True
cam_on = True
def run_model_YOLO(modelname, filename):
    #open the file that will be written to
    file = f_ops.open_file(filename)
    # placeholder: add args needed to run YOLO using modelname
    # run the darknet software using the model
    with Popen([modelname], stdout=PIPE) as process:
        for line in process.stdout:
            try:
                if (cl_on):
                    #print line to commandline
                    print(line, end='')
                #write line to the file
                f_ops.write_lap_data_to_file(file, line)
            except KeyboardInterrupt: #user has issued a signal to stop the program
                print("Signal caught. Ending the process and cleaning up.\n")
                f_ops.close_file(file)
                process.kill()

def run_model_cam(modelname, filename, camera):
    file = f_ops.open_file(filename)
    while(True):
        ret, frame = camera.read()

        # run model on frame

        if cam_on:
            cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
