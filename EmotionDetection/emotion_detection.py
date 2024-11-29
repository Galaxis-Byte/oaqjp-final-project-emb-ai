import json
import requests

def emotion_detector(text_to_analyse):
    # Information to access the Emotion Predict function of the Watson NLP Library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Received response from the API
    response = requests.post(url, json=input_json, headers=headers)

    # Perform error handling for blank entries
    if response.status_code == 400:
        blank_dict = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }
        return blank_dict

    # Convert response to JSON format
    json_response = response.json()

    # Construct the output
    emotion_dict = json_response["emotionPredictions"][0]['emotion']
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    emotion_dict["dominant_emotion"] = dominant_emotion

    return emotion_dict