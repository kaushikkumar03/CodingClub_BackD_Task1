import requests
import csv


api_key = "3ff557217036431e9950c3cfdedb51f0"

r = requests.get('http://api.football-data.org/v2/competitions').json()
c= csv.writer(open("FootballAPI.csv", "w", encoding='utf-8'), lineterminator = '\n')
c.writerow(["id", "Name", "Area/Country", "Available Seasons", "Tier"])

for item in r['competitions']:
    c.writerow([item["id"], item["name"], item["area"]["name"], item["numberOfAvailableSeasons"], item["plan"]])

with open("FootballAPI.csv", "r") as resultFile:
    reader = csv.reader(resultFile)
    tier = str(input("Enter the required championship tier: "))
    for row in reader:
        if row[4] == tier:
            c= csv.writer(open("results.csv", "w", encoding='utf-8'), lineterminator = '\n')
            c.writerow(["id", "Name", "Area/Country", "Available Seasons", "Tier"])

            for item in r['competitions']:
                c.writerow([item["id"], item["name"], item["area"]["name"], item["numberOfAvailableSeasons"], tier])















    


