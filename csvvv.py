import matplotlib.pyplot as plt 
import csv 
with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    row = next(csv_reader)
    print(row['LanguagesWorkedWith'].split(","))
    