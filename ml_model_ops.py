from subprocess import Popen, PIPE
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from time import sleep
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
    minus = -1;
    while(True):
        minus *= -1
        ret, frame = camera.read()
        if cam_on:
            cv2.imshow("Camera", frame)
        cv2.imwrite("frame.jpg", frame)
        if minus == 1:
            if ret:
                data = predict_on_img(model, "frame.jpg")
                if cl_on:
                    # print prediction to the file
                    for i in range(0,4):
                        if int(data[i]) != 10:
                            print(data[i], end='')
                print("\n")
                # write prediction to file
                line = ""
                for i in range(0, len(data)):
                    if int(data[i]) != 10:
                        line += str(data[i])
                line += "\n"
                f_ops.write_lap_data_to_file(filename, line)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    camera.release()
    cv2.destroyAllWindows()

def gray_conv(img):
    r = 0.299
    g = 0.587
    b = 0.114
    grayscale_img = np.expand_dims(np.dot(img, [r, g, b]), axis=3)
    return grayscale_img


def img_norm(img_array):
    mean = np.mean(img_array, axis=0)
    std = np.std(img_array, axis=0)

    # perform the normalization
    img_array = (img_array - mean) / std

    return img_array


def img_conv(image_name):
    img_width, img_height = 32, 32
    img = image.load_img(image_name, target_size=(img_width, img_height))
    img = gray_conv(img).astype(np.float32)
    img = img.astype(np.float32) / 255.0

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    image_data = np.vstack([x])

    return image_data


def predict_on_img(model, img_name):
    img = img_conv(img_name)
    prediction = model.predict(img)

    predicted_label = []
    for i in range(0, len(prediction)):
        x = np.amax(prediction[i])
        if x > 0.7:
            predicted_label.append(np.argmax(prediction[i]))
    return predicted_label