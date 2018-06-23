from flask import Flask, jsonify, request
from analyze_image import analyze_image
app = Flask(__name__)


@app.route('/post', methods=['POST'])
def post():
    image = request.files['file']
    results = analyze_image(image)

    return jsonify(results), 200


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
