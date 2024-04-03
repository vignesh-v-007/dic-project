import matplotlib.pyplot as plt
from io import BytesIO
import base64
from flask import Flask, render_template, request
import pickle

rating_model = pickle.load(open("rating_model.pkl", "rb"))

def create_feature_importance_chart(model):
    plt.figure(figsize=(10, 6))
    features = ['online_order', 'book_table', 'votes', 'location', 'rest_type' ,'cuisines','cost','type','city','no_of_items']  # Replace with actual features
    importances = model.feature_importances_
    plt.barh(features, importances, color='skyblue')
    plt.xlabel('Importance')
    plt.title('Feature Importance')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return plot_url

feature_importance_plot = create_feature_importance_chart(rating_model)


def create_comparison_chart(original_rating, new_rating):
    plt.figure(figsize=(6, 4))
    categories = ['Original', 'New']
    ratings = [original_rating, new_rating]

    plt.bar(categories, ratings, color=['blue', 'green'])
    plt.xlabel('Rating Type')
    plt.ylabel('Rating')
    plt.ylim(0, 5)  # Assuming rating scale is from 0 to 5
    plt.title('Rating Comparison')

    img = BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf-8')

    return plot_url

data_reg1 = {
    'online_order': [1],
    'book_table': [0],
    'votes': [30],
    'location': ['Whitefield'],
    'rest_type': ['Casual Dining'],
    'cuisines': ['others'],
    'cost': [2000],
    'type': ['Buffet'],
    'city': ['Whitefield'],
    'no_of_items': [0]
}

data_reg2 = {
    'online_order': [0],
    'book_table': [0],
    'votes': [30],
    'location': ['Whitefield'],
    'rest_type': ['Casual Dining'],
    'cuisines': ['others'],
    'cost': [2000],
    'type': ['Buffet'],
    'city': ['Whitefield'],
    'no_of_items': [0]
}

original_rating = rating_model.predict(data_reg1)[0]
new_rating = rating_model.predict(data_reg2)[0]


comparison_plot = create_comparison_chart(original_rating, new_rating)
