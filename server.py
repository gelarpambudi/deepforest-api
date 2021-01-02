import os
from flask import request, jsonify, make_response
from werkzeug.utils import secure_filename
from app import app
from predict_deepforest import predict

@app.route("/api/predict-deepforest", methods=["POST"])
def POST_handler():
    if request.method == "POST" :
        input_image = request.files['image'].read()
        results = predict(input_image)
        print(type(results))
        return jsonify(results)

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port='5555')