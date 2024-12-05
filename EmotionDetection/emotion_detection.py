import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL and headers as per the API documentation
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Create the payload for the POST request
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
 
    # Send a POST request to the Watson NLP API
    response = requests.post(url, headers=header, json=myobj)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract and return the 'text' attribute from the response
        response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
        return response.text  #
    else:
        # Return an error message if the request fails
        return f"Error: {response.status_code} - {response.text}"

# Example usage:
# text_to_analyze = "I am so happy today!"
# print(emotion_detector(text_to_analyze))
