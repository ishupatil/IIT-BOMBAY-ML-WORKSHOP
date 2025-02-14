import pandas as pd
import random
import string
import numpy as np

# Define parameters for dataset generation
NUM_ROWS = 100000  # Number of rows in the dataset

# Sample data for columns
sample_names = ["Alice", "Bob", "Charlie", "David", "Eve", None, "", "Frank"]
sample_emails = ["example1@gmail.com", "example2@yahoo.com", "", None, "example3@outlook.com", "test@@domain.com", "user@domain"]
sample_countries = ["USA", "Canada", "India", "UK", None, "", "Germany", "Australia"]
invalid_dates = ["2024-13-01", "2024-02-30", None, "", "not-a-date"]

# Functions to generate random data
def random_name():
    return random.choice(sample_names)

def random_email():
    return random.choice(sample_emails)

def random_country():
    return random.choice(sample_countries)

def random_date():
    if random.random() > 0.8:
        return random.choice(invalid_dates)
    return f"2024-{random.randint(1, 12):02}-{random.randint(1, 28):02}"

def random_salary():
    if random.random() > 0.9:
        return None
    return round(random.uniform(20000, 120000), 2)

def random_phone():
    if random.random() > 0.8:
        return ''.join(random.choices(string.ascii_letters, k=10))  # Invalid phone numbers
    return ''.join(random.choices(string.digits, k=10))

def random_age():
    if random.random() > 0.8:
        return None
    return random.randint(18, 70)

def random_reviews():
    return random.choice(["Good", "Bad", "Neutral", None, "", "gibberish123"])

def random_rating():
    return random.choice([1, 2, 3, 4, 5, None, "", "invalid"])

# Generate the dataset
print("Generating dirty dataset...")
data = {
    "Name": [random_name() for _ in range(NUM_ROWS)],
    "Email": [random_email() for _ in range(NUM_ROWS)],
    "Country": [random_country() for _ in range(NUM_ROWS)],
    "Date": [random_date() for _ in range(NUM_ROWS)],
    "Salary": [random_salary() for _ in range(NUM_ROWS)],
    "Phone": [random_phone() for _ in range(NUM_ROWS)],
    "Age": [random_age() for _ in range(NUM_ROWS)],
    "Review": [random_reviews() for _ in range(NUM_ROWS)],
    "Rating": [random_rating() for _ in range(NUM_ROWS)],
}

# Create DataFrame
dirty_df = pd.DataFrame(data)

# Introduce random duplicates
dirty_df = pd.concat([dirty_df, dirty_df.sample(frac=0.1, random_state=42)])

# Shuffle the dataset
dirty_df = dirty_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
output_file = "dirty_dataset.csv"
dirty_df.to_csv(output_file, index=False)

print(f"Dirty dataset generated and saved to {output_file} with {NUM_ROWS} rows and various data issues.")
