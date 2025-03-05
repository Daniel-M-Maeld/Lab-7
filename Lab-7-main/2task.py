import json
import requests

key = "308395f04a374fac9dd57310d7648847"

while True:
    search = input("1 - top headlines for a country, 2 - top headlines for category, 3 - news articles that mention a specific topic or keyword, 0 - exit: ")
    match search:
        case "1":
            country = input("Enter a country: ")
            response = requests.get(f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={key}")
            text = response.text
            print(text)
        case "2":
            category = input("Enter category: ")
            response = requests.get(f"https://newsapi.org/v2/top-headlines?sources={category}&apiKey={key}")
            text = response.text
            print(text)
        case "3":
            news = input("Enter news: ")
            year = input("Enter year: ")
            sort = input("Sort by:: ")
            response = requests.get(f"https://newsapi.org/v2/everything?q={news}&from={year}&sortBy={sort}&apiKey=={key}")
            text = response.text
            print(text)
        case "0":
            break
        case _:
            print("I want 1, 2 or 3!!!")

