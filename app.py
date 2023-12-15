from flask import Flask, request, jsonify
from main import emotion_detection_function

app = Flask(__name__)

@app.route('/detect-emotion', methods=['POST'])
def detect_emotion():
    try:
        image = request.files['image']
        if not image:
            return jsonify({'error': 'No image file found'})
        emotion = emotion_detection_function(image)
        if emotion is None:
            return jsonify({'error': 'Error during emotion detection'})
        return jsonify({'emotion': emotion})
    except Exception as e:
        # Handle any errors that occur during the request
        return jsonify({'error': f"Error during request: {e}"})
'''
@app.route('/detect-emotion', methods=['POST'])
def detect_emotion():
    image = request.files['image']
    image_path = 'D:/OMAR/October/27-10-23/Software/uploads'  
    image.save(image_path)
    emotion = emotion_detection_function(image_path)
    return jsonify({'emotion': emotion})

'''
from flask_cors import CORS
CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
