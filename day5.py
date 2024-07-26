print("Section 7 - Bag of Words (NLP)")

from sklearn.feature_extraction.text import CountVectorizer
# Define the corpus
corpus = ["Tôi thích môn Toán", "Tôi thích AI", "Tôi thích âm nhạc"]

# Create the vectorizer
vectorizer = CountVectorizer()

# Tokenize and build vocabulary
X = vectorizer.fit_transform(corpus)

# Convert sparse matrix to dense array
vector_array = X.toarray()

# Get the vocabulary
vocabulary = vectorizer.get_feature_names_out()

# Define the input sentence
input_sentence = "Tôi thích AI thích Toán"

# Transform the input sentence
input_vector = vectorizer.transform([input_sentence]).toarray()

# Output the results
print("Vocabulary:", vocabulary)
print("Bag-of-Words for 'Tôi thích AI thích Toán':", input_vector[0].tolist())