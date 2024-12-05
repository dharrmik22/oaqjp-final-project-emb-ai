from emotion_detection import emotion_detector
import unittest


def test_emotion_detection(self):
    # Test case for positive sentiment
    result_1 = emotion_detector('I am glad this happened')
    formatted_response = json.loads(result_1)
    emotion_data = formatted_response['emotionPredictions'][0]['emotion']

# Find the emotion with the maximum score
    max_emotion = max(emotion_data, key=emotion_data.get)






    self.assertEqual(max_emotion, 'joy')
   
unittest.main()
