def evaluate_prediction(confidence):
    if confidence >= 0.8:
        return "High"
    elif confidence >= 0.6:
        return "Medium"
    else:
        return "Low"
