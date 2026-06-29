import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder='../templates')
data = pd.read_csv('cleaned_data.csv')
pipe = pickle.load(open("RidgeModel1.pkl", 'rb'))


@app.route('/')
def index():
    # Get sorted unique locations from the data
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)


@app.route('/predict', methods=['POST'])
def predict():
    # Get user input data from the form
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')

    print(location, bhk, bath, sqft)

    # Create input data for prediction
    input_data = pd.DataFrame([[location, float(sqft), int(bath), int(bhk)]],
                              columns=['location', 'total_sqft', 'bath', 'bhk'])

    # Perform prediction
    prediction = pipe.predict(input_data)[0]*100  # Multiply by 100000 for the final price

    return str(prediction)

    # Return the prediction result to the user (render it on a result page)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
