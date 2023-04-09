import cohere 
import csv 
import telebot 
 
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
 
API_TOKEN = "6183059196:AAHrAIjR_qZJ_foJk6QOI7rhrqaYqdOLPJ0" 
 
bot = telebot.TeleBot(API_TOKEN) 
 
@bot.message_handler(commands=['start']) 
def send_welcome(message): 
    bot.reply_to(message, "Hello! Please text me") 
 
@bot.message_handler(func=lambda message: True) 
def echo_message(message): 
    co = cohere.Client('0JUMfSkNCZA7fH1gXUXNyvicm8mNpwv4HAqUckrA') # This is your trial API key 
    response = co.classify( 
    model='76cd0d2f-6115-4fab-af76-71b5a1d50ac2-ft', 
    inputs=["i will go to the church to forgive my sins"]) 
 
    # Update confidence scores based on new input 
    new_input = "sample input" 
    update_confidences(new_input) 
 
    # Sort confidence scores in descending order 
    sorted_indices = sorted(range(len(confidences)), key=lambda k: confidences[k], reverse=True) 
 
    # Select top 3 confidence scores and corresponding predictions 
    top_3_indices = sorted_indices[:3] 
    top_3_predictions = [predictions[i] for i in top_3_indices] 
 
    newPredictions = tuple(sorted(top_3_predictions)) 
    moods = dict() 
    moodsList = list() 
 
    with open('moods.csv', newline='') as csvfile: 
        reader = csv.reader(csvfile, delimiter=";") 
        for row in reader: 
            key = tuple([i.strip() for i in row[0].split(",")]) 
            value = row[1] 
            moods[key] = value 
        moodsList.append(moods) 
 
    for i in moodsList: 
        response = i[newPredictions] 
    bot.reply_to(message, response) 
 
if __name__ == "__main__": 
    bot.polling()

