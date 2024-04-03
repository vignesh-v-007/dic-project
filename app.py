import os
import pickle
from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt


app = Flask(__name__)

# Load your trained models
online_order_model = pickle.load(open("online_order_model.pkl", "rb"))
rating_model = pickle.load(open("rating_model.pkl", "rb"))

def create_feature_importance_chart(model,features):
    plt.figure(figsize=(10, 6))
    features = features
    importances = model.feature_importances_
    plt.barh(features, importances, color='skyblue')
    plt.xlabel('Importance')
    plt.title('Feature Importance')
    filename = 'feature_importance.png'
    filepath = os.path.join('static', filename)
    plt.savefig(filepath)
    plt.close()  # Close the plot to release memory
    return filename

# Encode the input Variables
def Encode(dummy_df):
    for column in dummy_df.columns[~dummy_df.columns.isin(["rate", "cost", "votes"])]:
        dummy_df[column] = dummy_df[column].factorize()[0]
    return dummy_df

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/select_prediction', methods=['POST'])
def select_prediction():
    choice = request.form.get('prediction_choice')
    if choice == 'rating':
        return redirect(url_for('rating_input'))
    if choice == 'online_order':
        return redirect(url_for('online_order_input'))
    else:
        return redirect(url_for('home'))

@app.route('/rating_input')
def rating_input():
    return render_template('rating_input.html')

@app.route('/online_order_input')
def online_order_input():
    return render_template('online_order_input.html')

@app.route('/predict_rating', methods=['POST'])
def predict_rating():
    try:
        data_reg = {
        'online_order': [str(request.form.get('online_order'))],
        'book_table': [str(request.form.get('book_table'))],
        'votes': [int(request.form.get('votes'))],
        'location': [str(request.form.get('location'))],
        'rest_type': [str(request.form.get('rest_type'))],
        'cuisines': [str(request.form.get('cuisines'))],
        'cost': [int(request.form.get('cost'))],
        'type': [str(request.form.get('type'))],
        'city': [str(request.form.get('city'))],
        'no_of_items': [int(request.form.get('no_of_items'))]}

        df = pd.DataFrame(data_reg)
        df.book_table.replace(("Yes", "No"), (1, 0), inplace=True)
        df.online_order.replace(("Yes", "No"), (1, 0), inplace=True)
        df_use = Encode(df.copy())
        prediction = rating_model.predict(df_use).round(2)

        print(prediction)

        book_table = request.form.get('book_table')
        online_order = request.form.get('online_order')
        cost = request.form.get('cost')
        votes = request.form.get('votes')
        no_of_items = request.form.get('no_of_items')

        # Convert form data to appropriate types
        book_table_value = 1 if book_table == 'True' else 0
        online_order_value = 1 if online_order == 'True' else 0
        cost_value = float(cost)
        votes_value = int(votes)
        no_of_items_value = int(no_of_items)

        features = ['online_order', 'book_table', 'votes', 'location', 'rest_type',
                     'cuisines', 'cost', 'type', 'city', 'no_of_items']
        feature_importance_plot = create_feature_importance_chart(rating_model,features)

        # Return prediction
        #return render_template('rating_input.html', prediction='Predicted Rating: {:.2f}'.format(prediction[0]))
        #return render_template('rating_result.html', prediction=prediction[0])
        return render_template('rating_result.html', prediction=prediction[0], 
                               book_table_value=book_table_value,
                               online_order_value=online_order_value,
                               cost_value=cost_value,
                               votes_value=votes_value,
                               no_of_items_value=no_of_items_value)
    except Exception as e:
        #return render_template('rating_input.html', prediction='An error occurred: {}'.format(e))
        return render_template('error.html', error_message=str(e))

@app.route('/predict_online_order', methods=['POST'])
def predict_online_order():
    try:
        data_class = {
        'name': [str(request.form.get('name'))],
        'book_table': [str(request.form.get('book_table'))],
        'rate': [float(request.form.get('rate'))],
        'votes': [int(request.form.get('votes'))],
        'location': [str(request.form.get('location'))],
        'rest_type': [str(request.form.get('rest_type'))],
        'cuisines': [str(request.form.get('cuisines'))],
        'cost': [int(request.form.get('cost'))],
        'type': [str(request.form.get('type'))],
        'city': [str(request.form.get('city'))],
        'no_of_items': [int(request.form.get('no_of_items'))]}

        df = pd.DataFrame(data_class)
        df.name = df.name.apply(lambda x: x.title())
        df.book_table.replace(("Yes", "No"), (True, False), inplace=True)
        df_use = Encode(df.copy())

        # Make predictions using the model
        prediction = online_order_model.predict(df_use).round(2)
        print(prediction)

        features = ['name', 'book_table', 'rate', 'votes', 'location', 
                    'rest_type', 'cuisines', 'cost', 'type', 'city', 'no_of_items']
        create_feature_importance_chart(online_order_model,features)

        # Return prediction
        return render_template('online_order_result.html', prediction=prediction[0])
        #return render_template('online_order_input.html', prediction='Predicted Rating: {:.2f}'.format(prediction[0]))
    except Exception as e:
        return render_template('error.html', error_message=str(e))

if __name__ == "__main__":
    app.run(debug=False)
