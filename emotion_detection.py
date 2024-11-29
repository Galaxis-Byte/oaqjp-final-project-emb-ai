import json
import requests

def emotion_detection(text_to_analyse):
    # Information to access the Emotion Predict function of the Watson NLP Library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    # Received response from the API
    response = requests.post(url, json=input_json, headers=headers)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        return json.dumps(data, indent=4)
    else:
        return ""

print(emotion_detection("I love this new technology."))