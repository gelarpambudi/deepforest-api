from flask import request, jsonify, make_response
from app import app
from deep_forest import predict_deepforest   


@app.route("/api/predict-deepforest", methods=["POST"])
def POST_handler():
    if request.method == "POST" :
        input_image = request.files['image']
        results = predict_deepforest.predict(input_image)
        print(type(results))
        return jsonify(type = type(results))


if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port='5555')