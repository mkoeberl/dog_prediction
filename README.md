# dog_prediction

## What is it

A simple web app where you can upload a picture and it tells you what type of dog breed is shown in the picture.
It does so for any picture (not only for pictures of dogs) with one of the following three scenarios being a possible outcome:
- A dog is detected and its breed is predicted.
- A human is detected and a breed is predicted.
- Neither is detected and a breed is predicted.

## How to run
Make sure that you have a virtual environment with Python 3.7.3 set up and install the necessary Python packages by running
```buildoutcfg
pip install /path/to/requirements.txt/requirements.txt
```

This web app uses flask, so in order to run, you need to tell your computer where to find the app.
To do so, change to the directory with `app.py` in it by running
```buildoutcfg
cd /path/to/app.py
```
and then run
```buildoutcfg
export FLASK_APP=app.py
```
and then, to run the app, enter the following command in your terminal/console:
```buildoutcfg
flask run
```
The output should tell you some URL you can enter in your browser. There, usage should be selfexplanatory.

Note that there might be some warnings from tensorflow if you don't have a GPU (or not set up for use by Tensorflow)
but the app should work nonetheless.

## What does it do in detail
In the background three machine learning models are used for classification:
- The first one is OpenCV's implementation of Haar feature-based cascade classifiers to detect human faces in images. Here we use this model to detect humans.
- The second one is ResNet50 trained on the ImageNet data which we use to detect dogs (not to classify its breed but to classify whether the picture shows a dog).
- The third one is a custom model built using transfer learning. It consists of the pre-trained Inception model with two layers on top trained using the Udacity-provided dog breed data.

After a picture is uploaded the app tries to detect a dog. If none is found it tries to detect a human.
Afterwards it runs the picture through the third model to classify the breed (of whatever is shown in the picture).
The output contains the found breed and whether a dog (or a human) was found in the picture.

## What data was used and how did the models do
We had a total of 8351 pictures of dogs of 133 different breeds. Those were split in 6680 training images, 835 validation images and 836 testing images.
On a sample of 100 human images and 100 dog images
- the human detector detected a human in all human images and 11 dog images,
- the dog detector detected a dog in all dogs images and in no human images.

Since the human detector is only used if no dog is detected by the dog detector the suboptimal performance of the human detector doesn't seem to be a problem.
It should be noted however that it is quite likely that the human detector also detects human in pictures of, say, cats, which are neither dogs nor humans.
Thus its results should be taken with a grain of salt. We think though that the average human is quite good at differentiating humans from dogs from other things
and thus the primary goal of the web app should be high-quality dog breed classification. If these models were used for automatization
the available human pictures (of which we have 13 233) should be used to improve the performance of the human detector.

The dog breed classification model achieved an accuracy of approximately 82 % on the test dataset of dog images. Given that there are 133 different breeds (not necessarily balanced)
this seems quite respectable.

## What Python packages were used for this app
- `flask` for the app
- `tensorflow.keras`/`keras` for the dog breed classifier
- `cv2` for the human detector
- `pillow` for image file handling
- and the usual other suspects (see `requirements.txt` for details) ;)

## 

