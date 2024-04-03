import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

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

# Encode the input Variables
def Encode(dummy_df):
    for column in dummy_df.columns[~dummy_df.columns.isin(["rate", "cost", "votes"])]:
        dummy_df[column] = dummy_df[column].factorize()[0]
    return dummy_df

# Load your trained models
online_order_model = pickle.load(open("online_order_model.pkl", "rb"))
rating_model = pickle.load(open("rating_model.pkl", "rb"))

data_class1 = {
    'name': ['Samplere'],
    'book_table': [0],
    'rate': [4.8],
    'votes': [30],
    'location': ['Whitefield'],
    'rest_type': ['Casual Dining'],
    'cuisines': ['others'],
    'cost': [2000],
    'type': ['Buffet'],
    'city': ['Whitefield'],
    'no_of_items': [0]
}

data_class2 = {
    'name': ['SAMPLE12'],
    'book_table': [1],
    'rate': [4.3],
    'votes': [500],
    'location': ['Banashankari'],
    'rest_type': ['Casual Dining'],
    'cuisines': ['others'],
    'cost': [500],
    'type': ['Buffet'],
    'city': ['Whitefield'],
    'no_of_items': [30]
}

data_reg = {
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

df1 = pd.DataFrame(data_class1)#, columns=columns_class)
df2 = pd.DataFrame(data_class2)
#df.name = df.name.apply(lambda x: x.title())
#df.online_order.replace(("Yes", "No"), (True, False), inplace=True)
df1.book_table.replace(("Yes", "No"), (True, False), inplace=True)
df2.book_table.replace(("Yes", "No"), (True, False), inplace=True)

df_use1 = Encode(df1.copy())
df_use2 = Encode(df2.copy())

# Make predictions using the model
prediction1 = online_order_model.predict(df_use1)[0]
prediction2 = online_order_model.predict(df_use2)[0]
#prediction = rating_model.predict(df_use)
print(prediction1,prediction2)


comparison_plot = create_comparison_chart(prediction1, prediction2)

