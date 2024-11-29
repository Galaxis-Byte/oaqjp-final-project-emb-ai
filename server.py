"""
This Python script creates a Flask application to detect emotions
from the given text using the emotion_detector function.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion App")

@app.route("/")
def index():
    """
    Renders the homepage.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Detect the dominant emotion from the given text.

    Returns:
        A formatted string containing emotion scores and the dominant emotion.
        If the text is invalid, returns an error message.
    """
    # Send and receive response from API
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "<strong>Invalid text! Please try again!<strong>"

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
