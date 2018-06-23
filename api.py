from dotenv import load_dotenv
from flask import Flask, jsonify, request
from analyze_image import analyze_image
load_dotenv()
app = Flask(__name__)


@app.route('/pizza', methods=['POST'])
def pizza():
    image = request.files['file']
    results = analyze_image(image)
    for el in results:
        if el['Name'] == 'Pizza':
            response = {
                'message': 'Pizza confirmed.',
                'confidence': el
            }
            return jsonify(response), 200
    response = {
        'message': 'Pizza not found.',
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
