This file contains instructions for generating the necessary files needed to create 
a digit classifier using Google's SVHN dataset using YOLO.

The SVHN Dataset is used for training the machine learning models.
You can find the model at the following website:
http://ufldl.stanford.edu/housenumbers/

Installation instructions for installing darknet in Windows 10 can be found here:
https://github.com/AlexeyAB/darknet#how-to-train-tiny-yolo-to-detect-your-custom-objects

PLEASE NOTE
The python notebooks provided are only tested in a GoogleColab environment.
Instructions for running the data preprocessing and model creation functions are written assuming
code execution is done in a GoogleColab environment; however, with the proper libraries,
the notebooks can be uploaded into any environment that supports .ipynb (such as Jupyter) to
be executed locally. Alternatively, .ipynb can be uploaded into a GoogleColab and be downloaded
as a .py file.

Before running YOLO, be sure that you're using an NVIDIA GPU and that its drivers are up to date!

**************************************************************************************************

FILES TO GENERATE .txts FOR TRAINING YOLO USING SVHN
	-SVHN_Preprocess_YOLO.ipynb
	-unpacker.py
	-train.tar.gz (from SVHN Dataset Format 1)
	-test.tar.gz (from SVHN Dataset Format 1)

	
EXECUTION STEPS

1) Upload the YOLO preprocess notebook.
   In GoogleColab expand the side window-pane, select the Files header, select upload,
   and finally upload the necessary files listed above.
   
3) Download the generated .zip files from the notebook (saved under the Files header).
	-train_txt.zip
	-test_txt.zip
	-train.txt
	-test.txt
	
**************************************************************************************************

TRAINING YOLO USING TXT FILES

BE SURE TO HAVE PASTED darknet53.conv.74 into
 .../darknet-master/build/darknet/x64
 
You can find the download link for the darknet53 file on AlexeyAB's GitHub
Alternatively, you can directly download it from: http://pjreddie.com/media/files/darknet53.conv.74


NECESSARY FILES
	-train.tar.gz
	-test.tar.gz
	-train_txt.zip
	-test_txt.zip
	-train.txt
	-test.txt
	-svhn.data
	-svhn.names
	
1) Go to the following directory .../darknet-master/build/darknet/x64/data
   Paste train.txt and test.txt here.
   Paste svhn.data and svhn.names here.
   
1.2) Go into the /obj folder
   Create a folder named train in this directory.
   Create a folder named test in this directory.
   
1.3) Copy all the .txt files from train_txt.zip into the /train folder (should be 33402 files)
     Copy all the .txt files from test_txt.zip into the /test folder (should be 13068 files)
   
1.4) Unzip the training images from train.tar.gz
	 Unzip the testing images from test.tar.gz
     Copy all of the training images into the /train folder you created.
     Copy all of the testing images into the /test folder you created.
   

2) Go to the following directory .../darknet-master/build/darknet/x64/cfg
   Paste yolov3-svhn.cfg here.
   
You should now be able to train a model.
Open the command prompt from the following directory:  .../darknet-master/build/darknet/x64
Use the following command to train a model: 
darknet.exe detector train data/svhn.data cfg/yolov3-svhn.cfg darknet53.conv.74


When finished training, weights for the model are saved in the /backup folder.
Rename your chosen weights file to yolov3-svhn.weights and copy it into the /x64 folder


You should now be able to run the digit classifier.
Open the command prompt from the following directory:  .../darknet-master/build/darknet/x64
Use the following command to run the classifier: 
darknet.exe detector demo cfg/svhn.data cfg/yolov3-svhn.cfg yolov3-svhn.weights

**************************************************************************************************

CLASSIFICATION/TRAINING TIP
It is important that the width and height parametes in the .cfg file are large enough to be able
to be able to view images at a high enough resolution to actually make predictions.
It is reccomended that the values set for these are square (the same value) and that the values
are multiples of 32 (ie: 832 x 832)

PLEASE NOTE: Increasing these values will slow prediction time on each frame of video input, so
it is reccomended that you have a powerful enough GPU to maintain a decent FPS.