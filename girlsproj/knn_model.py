import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier

# Load the datasets
df = pd.read_excel(r'C:\Users\aatee\OneDrive\Desktop\girlsproj\colordataset.xlsx')
dfs = pd.read_excel(r'C:\Users\aatee\OneDrive\Desktop\girlsproj\types.xlsx')

# Vectorizer for color (RGB)
vectorizer_color = CountVectorizer()

# Function to predict matching colors based on RGB input
def predict(user_color_rgb):
    ipvector = vectorizer_color.transform([user_color_rgb])
    neighbors = knn_model.kneighbors(ipvector, return_distance=False)
    predictions = [y.iloc[i] for i in neighbors[0]]
    return predictions

# Function to predict matching types based on clothing type input
def predict_type(utype):
    iptvector = vectorizer_type.transform([utype])
    neighborst = knn_model2.kneighbors(iptvector, return_distance=False)
    type_predictions = [y1.iloc[i] for i in neighborst[0]]
    return type_predictions

# Prepare the training data for the KNN models
x = df['RGB']
y = df['Complement']
x_vectorized = vectorizer_color.fit_transform(x)
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(x_vectorized, y)

# Vectorizer for clothing types
vectorizer_type = CountVectorizer()
x1 = dfs['type']
y1 = dfs['typematch']
x1_vectorized = vectorizer_type.fit_transform(x1)
knn_model2 = KNeighborsClassifier(n_neighbors=3)
knn_model2.fit(x1_vectorized, y1)
