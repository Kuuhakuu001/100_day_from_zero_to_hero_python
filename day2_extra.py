# This is day 2 extra homework

# Section 1 - List Creation and Accessing
print("Section 1 - List Creation and Accessing")

# Câu 1
lst_data = list(range(1, 11))
print("Câu 1:", lst_data)

# Câu 2
result_2 = lst_data[:5]
print("Câu 2:", result_2)

# Câu 3
result_3 = [x for x in lst_data if x % 2 != 0]
print("Câu 3:", result_3)

# Câu 4
total_sum = 0
for num in lst_data:
    total_sum += num
print("Câu 4:", total_sum)
print("--------------------------------------")

# Section 2 - List CRUD
print("Section 2 - List CRUD")

# Câu 1
lst_data = list(range(2, 13, 2))
print("Câu 1:", lst_data)

# Câu 2
lst_data = [x for x in lst_data if x % 3 != 0]
print("Câu 2:",lst_data)

# Câu 3
lst_data.extend([1, 2, 3])
lst_data[3:3] = [6, 7, 8]
print("Câu 3:", lst_data)

# Câu 4
result_3 = [0 if isinstance(x, int) and (x % 2 == 0 or x % 5 == 0) else x for x in lst_data]
print("Câu 4:", result_3)
print("--------------------------------------")

# Section 3 - List and Branching
print("Section 3 - List and Branching")

def is_armstrong(number):
    digits = list(map(int, str(number)))
    power = len(digits)
    return sum(digit ** power for digit in digits) == number

# Given test case
test_case_1 = [130, 270, 153, 407, 177, 371, 1000, 1634, 370]

# Result list for Armstrong numbers
result = [num for num in test_case_1 if is_armstrong(num)]

# Print the result
print("Các số Armstrong có trong list là:", result)
print("--------------------------------------")

# Section 4 - List and Branching
print("Section 4 - List and Branching")

def can_have_most_candies(candies, extraCandies):
    max_candies = max(candies)
    result = [candy + extraCandies >= max_candies for candy in candies]
    return result

# Test cases
test_case_1 = [2, 3, 5, 1, 3]
extraCandies_1 = 3
test_case_2 = [4, 2, 1, 1, 2]
extraCandies_2 = 1
test_case_3 = [12, 1, 12]
extraCandies_3 = 10

# Output results
result_1 = can_have_most_candies(test_case_1, extraCandies_1)
result_2 = can_have_most_candies(test_case_2, extraCandies_2)
result_3 = can_have_most_candies(test_case_3, extraCandies_3)

print("Test case 1:", result_1)
print("Test case 2:", result_2)
print("Test case 3:", result_3)
print("--------------------------------------")

# Section 5 - Computing median for a list of numbers
print("Section 5 - Computing median for a list of numbers")
# Câu 1
lst_data = list(range(1, 11))
print("Câu 1:", lst_data)

# Câu 2
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n //2
    if n % 2 == 0:
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        median = sorted_data[mid]
    return median

median_value = calculate_median(lst_data)
print("Câu 2:", median_value)

# Câu 3
lst_odd_filter = sorted([x for x in lst_data if x % 2 != 0], reverse=True)
print("Câu 3:", lst_odd_filter)
print("--------------------------------------")

# Section 6 - Computing mean for a list of numbers
# Câu 1
lst_data = list(range(1, 11))
print("Câu 1:", lst_data)

# Câu 2
odd_arr = [x for x in lst_data if x % 2 != 0]
even_arr = [x for x in lst_data if x % 2 == 0]
mean_odd = sum(odd_arr) / len(odd_arr)
mean_even = sum(even_arr) / len(even_arr)
print(f"Câu 2: Mean lẻ: {mean_odd} - Mean chẵn: {mean_even}")

# Câu 3
mean = sum(lst_data) / len(lst_data)
median = calculate_median(lst_data)
print(f"Câu 3: Mean = Median = {mean}")
print("--------------------------------------")

# Section 7 - Bag of Words (NLP)
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
print("--------------------------------------")

# Section 8 - Algorithms on List
print("Section 8 - Algorithms on List")

def find_none(arr):
    for i in range(len(arr)):
        if arr[i] == None:
            return i


def find_nones(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] == None:
            result.append(i)
    return result

lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]
print(f"Vị trí None đầu tiên: {find_none(lst_data)} - Danh sách vị trí có giá trị None: {find_nones(lst_data)}")
print("--------------------------------------")

# Section 9 - Interpolation for List (Time-series)
import numpy as np
print("Section 9 - Interpolation for List (Time-series)")

lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]

# Nearest Neighbor Interpolation
def nearest_neighbor_interpolation(data):
    # Convert list to numpy array for easy manipulation
    data_array = np.array(data)
    
    # Find indices of None values
    none_indices = np.where(data_array == None)[0]
    
    # Iterate over None indices
    for idx in none_indices:
        # Find the nearest non-None value
        left = idx - 1
        right = idx + 1
        # Look for the nearest neighbor on the left side
        while left >= 0 and data_array[left] is None:
            left -= 1
        # Look for the nearest neighbor on the right side
        while right < len(data_array) and data_array[right] is None:
            right += 1
         # Determine the closest non-None neighbor
        if left >= 0 and right < len(data_array):
            if (idx - left) <= (right - idx):
                data_array[idx] = data_array[left]
            else:
                data_array[idx] = data_array[right]
        elif left >= 0:
            data_array[idx] = data_array[left]
        elif right < len(data_array):
            data_array[idx] = data_array[right]
    
    return data_array.tolist()

# Apply the interpolation
interpolated_data = nearest_neighbor_interpolation(lst_data)

# Print the result
print("Interpolated List:", interpolated_data)
print("--------------------------------------")

# Section 10 - 2D List
print("Section 10 - 2D List")

