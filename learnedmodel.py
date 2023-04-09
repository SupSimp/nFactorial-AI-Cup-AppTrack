import cohere
import numpy as np
import pandas as pd
import re

co = cohere.Client('0JUMfSkNCZA7fH1gXUXNyvicm8mNpwv4HAqUckrA') # This is your trial API key
response = co.classify(
  model='76cd0d2f-6115-4fab-af76-71b5a1d50ac2-ft',
  inputs=["i will go to the church to forgive my sins"])

# Example data - predictions and confidences
predictions = ['anger', 'fear', 'joy', 'love', 'sadness', 'surprise']
confidences = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# Function to update confidence scores based on new input
def update_confidences(new_input):
    # Your code to update the confidence scores based on new input
    # This will depend on how the model and input are implemented
    
    # For demonstration purposes, we can randomly update the confidence scores
    import random
    for i in range(len(confidences)):
        confidences[i] += random.uniform(-0.1, 0.1)

# Update confidence scores based on new input
new_input = "sample input"
update_confidences(new_input)

# Sort confidence scores in descending order
sorted_indices = sorted(range(len(confidences)), key=lambda k: confidences[k], reverse=True)

# Select top 3 confidence scores and corresponding predictions
top_3_indices = sorted_indices[:3]
top_3_predictions = [predictions[i] for i in top_3_indices]

# Display the top 3 predictions and confidence scores
print("Top 3 predictions:")
for i in range(len(top_3_predictions)):
    print(f"{i+1}. {top_3_predictions[i]}")

# Return the top 3 predictions as a list
#return top_3_predictions

