# import the necessary packages
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth

import io

# initialize our Flask application and the Keras model
app = Flask(__name__)
model = None


"""
Load Model Function:
Pretrained ImageNet and provided by Keras,
To be substituted with self model
"""

def load_model():
    global model
    model = ResNet50(weights="imagenet")

"""
Prepare Image Function:
Accepts Input Image
Converts the mode to RGB
Resizes to 224x224 (RESNET)
Image to array with scaling
"""
def prepare_image(image, target):
    if image.mode != "RGB":
        image = image.convert("RGB")

    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    return image
"""
Predict Function:
Process any requests at the /predict endpoint
Read the Image
Process the image with prepare_image
pass it to the network
loop over results and add them to the data dic tto present
JSON response

"""

@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if request.method == "POST":
        if request.files.get("image"):
            # read the image in PIL format
            image = request.files["image"].read()
            image = Image.open(io.BytesIO(image))

            # preprocess the image and prepare it for classification
            image = prepare_image(image, target=(224, 224))

            # classify the input image and then initialize the list
            # of predictions to return to the client
            preds = model.predict(image)
            results = imagenet_utils.decode_predictions(preds)
            data["predictions"] = []

            # loop over the results and add them to the list of
            # returned predictions
            for (imagenetID, label, prob) in results[0]:
                r = {"label": label, "probability": float(prob)}
                data["predictions"].append(r)

            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return jsonify(data)

if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    load_model()
    app.run(debug = False, threaded = False)
