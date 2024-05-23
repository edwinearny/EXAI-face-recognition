# Interpretability of Deep Learning Model (InceptionV3) in Face Recognition

## Project Overview
This project explores the interpretability of a deep learning model (InceptionV3) in face recognition using LIME (Local Interpretable Model-agnostic Explanations), Saliency Maps, and examines the model's performance under partial occlusion of faces. The project is structured into three main files:

1. **load_lfw.py**: Loads and arranges the LFW (Labeled Faces in the Wild) dataset into training and testing splits.
2. **compressing_lfw_aligned.ipynb**: Detects, aligns, extracts, and compresses the images from the LFW dataset.
3. **inception_XAI.ipynb**: Loads the compressed file, initializes the InceptionV3 model, explains the original faces using LIME and Saliency Maps, and includes model predictions after partial occlusion of images.

## Files Description

### 1. load_lfw.py
This script handles loading the LFW dataset and arranging the images into a training and testing split with a 90:10 ratio.
- Load LFW dataset
- Split the dataset into training and testing sets (90% training, 10% testing)

### 2. compressing_lfw_aligned.ipynb
This notebook performs the following tasks:
- Detects faces in the images
- Aligns the detected faces
- Extracts and compresses the images into a single file for efficient processing

### 3. inception_XAI.ipynb
This notebook includes the main tasks for model interpretation and evaluation:
- Loads the compressed file from the previous step
- Initializes the InceptionV3 model with custom top layers
- Uses LIME and Saliency Maps to explain the model's predictions on original face images
- Evaluates the model's predictions after partial occlusion of the face images

## Requirements
To run the project, you need the following libraries:
- tensorflow
- keras
- matplotlib
- scikit-image
- scikit-learn
- lime
- tf-keras-vis

Install the required packages using pip:
```sh
pip install tensorflow keras matplotlib scikit-image scikit-learn lime tf-keras-vis
