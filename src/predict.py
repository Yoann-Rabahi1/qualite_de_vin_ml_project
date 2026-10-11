import joblib
import pandas as pd



def predict_wine_quality(model, input_dict):

    df_input = pd.DataFrame(input_dict)



    prediction = model.predict(df_input)

    probability = model.predict_proba(df_input)[:, 1]

    return (prediction[0], probability[1])