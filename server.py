from flask import request, jsonify, make_response
from app import app
from predict_deeepforest import load_model, predict   

global model = load_model()

@app.route("/api/predict-deepforest", methods=["POST"])
def POST_handler():
    if request.method == "POST" :
        input_image = request.files['image']
        results = predict(input_image, model)
        print(type(results))
        return jsonify(type = type(results))


if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port='5555')