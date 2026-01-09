import pickle
import pandas as pd

#import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION='1.0.0'

classes = model.classes_.tolist()

def predict_output(user_input:dict):
    input_df = pd.DataFrame([user_input])
    predicted_output = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)
    #create mapping {'class_name':'probability'}
    class_probs = dict(zip(classes, map(lambda p:round(p,4), probabilities)))
    return {
        'predicted_category':predicted_output,
        'confidence':round(confidence,4),
        'class_probabilities':class_probs

    }