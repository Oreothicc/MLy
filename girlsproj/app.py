from flask import Flask, render_template, request
import pandas as pd
from knn_model import predict, predict_type  # Importing the functions directly from your model

app = Flask(__name__, template_folder='template_html')

@app.route('/')
def home():
    return render_template('index.html')  # This loads the HTML page

@app.route('/predict', methods=['POST'])
def predict_route():
    try:
        # Get RGB values and type from the form submission
        r = int(request.form['r'])
        g = int(request.form['g'])
        b = int(request.form['b'])
        ucolor = f"[{r}, {g}, {b}]"
        utype = request.form['type']

        # Use the KNN functions to predict the complementing colors and type
        predicted_matches = predict(ucolor)
        predicted_type_matches = predict_type(utype)

        # Return the result to the template
        return render_template('index.html', 
                               prediction_colors=predicted_matches, 
                               prediction_type=predicted_type_matches)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
