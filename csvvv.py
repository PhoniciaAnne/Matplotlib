import matplotlib.pyplot as plt
import csv
from collections import Counter

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    language_counter = Counter()
    
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(","))
    
# Create lists for the languages and their popularity
languages = []
popularity = []

# Get the 15 most common languages
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# Plotting the data
plt.barh(languages, popularity)

# Adding title and labels
plt.title("Most Popular Programming Languages")
plt.xlabel("Languages")
plt.ylabel("Number of Developers")
plt.tight_layout()

# Show the plot
plt.show()
