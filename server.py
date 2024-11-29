from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion App")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    # Send and receive response from API
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    # Construct the statement
    statement = f"For the given statement, the system response is " \
                f"'anger': {response['anger']}, " \
                f"'disgust': {response['disgust']}, " \
                f"'fear': {response['fear']}, " \
                f"'joy': {response['joy']} and " \
                f"'sadness': {response['sadness']}. " \
                f"The dominant emotion is <strong>{response['dominant_emotion']}<strong>."

    return statement

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)