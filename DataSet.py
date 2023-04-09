import numpy as np
import pandas as pd
data = pd.read_csv('new_emotions.csv', delimiter=';')

#cols_to_remove = ["tweet_id"]

# drop the specified columns from the DataFrame
#data.drop(cols_to_remove, axis=1, inplace=True)

# drop all rows with NaN values
#data.dropna(how='all', inplace=True)

# save the modified DataFrame back to a CSV file
#data.to_csv("preprocessed_data.csv", index=False)

print(data)
