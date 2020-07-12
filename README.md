# Deep Learning REST API (simple)

## Description
This repository presents a method of taking a ML model and deploying it as an API, showing the easiest way to take an deep learning model to production.
I also take advantage of Test Driven Development (TDD) by writing acceptance and developer tests throughout, which can be seen in _testing/_.

## TDD
I started with the assumption that the Keras API was inherently well tested (thus out of the scope of our requirements) and that Flask was equally so, therefore I started with the simple test cases found in _tests.robot_
- Submit Photo
  - Send a Photo using a POST request
  - App receives Photo
  - Photo sent = photo received
- Model correctly predicts sample photos
  - Model receives photo
  - Model makes prediction
  - Prediction = expected

which contain the high level keywords also in _tests.robot_
- Supply Image
- Detection  

using the low level keywords written in _TestLibrary.py_
- send_img
- post_img
- image_analysis

The results are then stored in the files _log.html_, _output.xml_, and _report.html_ also located in _testing/_

## API
The API consists of two actions (hence simple). One responds to the get request of the URL (in this case the host machine) and provides a basic form to uplaod a file for precition. The second action is a POST method that takes the uploaded file (upon the submit button being pressed) and returns a JSON (I said **simple**) response of the top 5 predictions from the network.

Note: The Model is not loaded every time a prediction is requested, instead I load the model upon the main execution of the file _simple_keras_api_server.py_ right before the server is started.

The main focus of this API was to learn how to load a keras model efficiently, serve it using Flask, and make predictions returnable (JSON) to the client.

## ResNet50
More can be read about RESNET here on the [keras website].
## Development Environment
The following python libraries are used:
`numpy, gevent, flask, pillow, keras, tensorflow, robotframework`


## Todo

- COVID Model
  - Add ML assisted diagnosis of COVID from patient's lung xrays concept
  - Write tests for including it into the system
    - Training Model
    - Loading Model
    - Model receives/predicts xrays
- Front-end revamp
- Add separate report folder within _testing_/
- Tests
  - What happens when no file is submitted
  - Too large of file
  - Not an Image on request


[keras website]: https://keras.io/api/applications/
