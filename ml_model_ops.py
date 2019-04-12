from subprocess import Popen, PIPE
from keras.models import load_model
import numpy as np
import cv2
import file_ops as f_ops

cl_on = True
cam_on = True
model = load_model("SVHN_model_multi.h5")

def run_model_YOLO(modelname, filename):
    #open the file that will be written to
    file = f_ops.open_file(filename)
    # placeholder: add args needed to run YOLO using modelname
    # run the darknet software using the model
    with Popen([modelname], stdout=PIPE) as process:
        for line in process.stdout:
            try:
                if cl_on:
                    # print line to commandline
                    print(line, end='\n')
                # write line to the file
                f_ops.write_lap_data_to_file(file, line)
            except KeyboardInterrupt: # user has issued a signal to stop the program
                print("Signal caught. Ending the process and cleaning up.\n")
                f_ops.close_file(file)
                process.kill()

def run_model_cam(filename, camera):
    while(True):
        ret, frame = camera.read()
        if ret:
            '''
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = np.expand_dims(frame_gray, axis=1)
            frame_data = cv2.resize(frame, (32, 32))
            # run model on frame
            data = model.predict(frame_data, batch_size=1)
            if cl_on:
                # print prediction to the file
                for i in range(0,4):
                    if int(data[i]) != 10:
                        print(data[i], end='')
            print
            # write prediction to file
            line = ""
            for i in range(0, 4):
                if int(data[i]) != 10:
                    line += str(data[i])
            line += "\n"
            f_ops.write_lap_data_to_file(filename, line)
            '''
            if cam_on:
                cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    camera.release()
    cv2.destroyAllWindows()
