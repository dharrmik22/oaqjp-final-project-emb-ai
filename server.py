from flask import Flask, render_template, request


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    from emotion_detection import emotion_detector

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    formatted_response = json.loads(response)


    # Extract the label and score from the response
    label = formatted_response['emotionPredictions'][0]['emotion']

    # Return a formatted string with the sentiment label and score
    return "The given text has been identified as {} ".format(label.split('_')[1])