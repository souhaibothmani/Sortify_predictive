# Integration_3_Team_11_Sortify_AI_model_predictive

## Overview

This project implements a waste material classification system using an ESP32 microcontroller with camera and a deep learning model to classify various types of garbage based on images. The system captures images from the camera, processes them using a Python-based model, and sends back the predicted material type to the ESP32, which then communicates with the Spring Boot web application for further processing.
## Features

ESP32 Microcontroller: Captures images and sends them to the server for classification.
Deep Learning Model: Classifies images into various material types (e.g., cardboard, plastic, etc.).
Spring Boot Web Application: Receives predictions from the ESP32 and displays the results.
Material Classification: The model is trained to predict material types based on image data, providing accurate results for waste management.
How it Works

Image Capture: The ESP32 captures an image of the waste using the camera.
Image Processing: The ESP32 sends the image to the web server via an HTTP POST request. The image is passed to the Python backend that hosts the trained deep learning model.
Model Inference: The Python backend loads the trained model (ResNet50) and processes the image to predict the material type.
Prediction Response: The predicted material is sent back to the ESP32 as an HTTP response.
Data Display: The prediction is displayed on the web application, where users can track the classification results.
## Setup

Requirements
Hardware:
ESP32-CAM
Software:
Python 3.x (for running the model)
Flask (for setting up the Python server)
Spring Boot 
PostgreSQL (for storing classification data)
PIL (for image resizing and compression)
## Model Training

The model used for material classification is a ResNet50 model, which was trained on a dataset of various materials. After training, the model achieved an accuracy of 96% on the validation dataset, ensuring reliable predictions for the materials of garbage.
Other Models Tested
In addition to the ResNet50 model, I also experimented with Gaussian Naive Bayes (GaussianNB) and Logistic Regression models. However, these models performed significantly worse, achieving an accuracy of around 37%. The results highlight the advantages of using a deep learning approach for this classification task.
## Model Accuracy

After training, the ResNet50 model achieved an impressive 96% accuracy on the validation dataset. This makes the model highly reliable for predicting material types based on garbage images.
Results of Other Models:
Gaussian Naive Bayes (GaussianNB): 37% accuracy
Logistic Regression: 37% accuracy
These models were tested but did not perform well, reinforcing the effectiveness of the ResNet50 model for this classification task.
## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request with your changes. You can also submit issues for any bugs or enhancements you'd like to see.
