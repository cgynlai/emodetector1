import requests
import json

def emotion_detector(text_to_analyse):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }


    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    json_response = json.loads(response.text)
    emotions = json_response['emotionPredictions'][0]['emotion']
    dominant = max(emotions, key=emotions.get)

    formatted_response = {
        'anger' : emotions['anger'],
        'disgust' : emotions['disgust'],
        'fear' : emotions['fear'],
        'joy' : emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion' : dominant
    }



    return formatted_response
    """
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None

    # Return the label and score in a dictionary
    return {'label': label, 'score': score}   
    """