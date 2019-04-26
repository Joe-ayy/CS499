This file contains instructions for generating the necessary files needed to create 
a digit classifier using Google's SVHN dataset using Keras models.

The SVHN Dataset is used for training the machine learning models.
You can find the model at the following website:
http://ufldl.stanford.edu/housenumbers/

PLEASE NOTE
The python notebooks provided are only tested in a GoogleColab environment.
Instructions for running the data preprocessing and model creation functions are written assuming
code execution is done in a GoogleColab environment; however, with the proper libraries,
the notebooks can be uploaded into any environment that supports .ipynb (such as Jupyter) to
be executed locally. Alternatively, .ipynb can be uploaded into a GoogleColab and be downloaded
as a .py file.

**************************************************************************************************

FILES FOR PREPROCESSING

Single-Digit Preprocess Files
	-SVHN_Preprocess_Single.ipynb
	-train_32x32 (from SVHN Dataset Format 2)
	-test_32x32 (from SVHN Dataset Format 2)


Multi-Digit Preprocess Files
	-SVHN_Preprocess_Multi.ipynb
	-unpacker.py
	-train.tar.gz (from SVHN Dataset Format 1)
	-test.tar.gz (from SVHN Dataset Format 1)


PREPROCESSING STEPS

1) Upload the necessary notebook for the type of model you wish to create preprocessed data for.
   In GoogleColab expand the side window-pane, select the Files header, select upload,
   and finally upload the necessary files.
   
2) Run all of the cells in the notebook.

3) Download the generated .h5 files from the notebook (saved under the Files header).
	-SVHN_Preprocessed_Single.h5/SVHN_Preprocessed_Multi.h5
	
**************************************************************************************************

FILES FOR MODEL CREATION

Single-Digit Model Files
	-SVHN_Model_Single.ipynb
	-SVHN_Preprocessed_Single.h5

Multi-Digit Model Files
	-SVHN_Model_Multi.ipynb
	-SVHN_Preprocessed_Multi.h5

	
MODEL CREATION STEPS

1) Upload the necessary notebook for the type of model you wish to create.
   In GoogleColab expand the side window-pane, select the Files header, select upload,
   and finally upload the necessary files.
   
2) Run all the cells in the notebook.

3) Download the generated .h5 files from the notebook (saved under the Files header).
	-SVHN_model_single.h5/SVHN_model_multi.h5
	
**************************************************************************************************	

MODEL TIPS

Tip 1
When fitting the model for training, it might be wise to update the initial input tenser to
accomodate a higher resolution image (the input for the models provided is initially 32x32).
It is reccomended to update the resolution to a number divisible by 32 and square (such as 832x832).
Please note that by increasing the input tenser, the time necessary to make predictions increases.

Tip 2
Our team tried to keep the code for this project modularized. It should be easy to swap-out/update
the default model architecture we've provided to a model of your choosing.
By creating/researching a better model you should be able to improve accuracy on this dataset.
Our initial research has shown that some models for this dataset have achieved ~98% accuracy.

Tip 3
Training models for a large number of epochs isn't feasible in the GoogleColab environment,
as the virtual machine's runtime will disconnect before the model can finish training.
It is reccomended to train models in a local environment.