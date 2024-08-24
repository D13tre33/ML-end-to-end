import pandas as pd

# Load the dataset
try:
    data = pd.read_csv('creditcard.csv')
    print('CSV file loaded successfully')
except FileNotFoundError:
    print('CSV file not found')

# Placeholder for further processing
if __name__ == '__main__':
    print('App is running')