from bs4 import BeautifulSoup
import requests

url ="https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512"

response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, "html.parser")

movies = [movie.getText() for movie in soup.find_all(name='h1', class_="list-item__title")]
movies_dict = {i+1: movie for i, movie in enumerate(reversed(movies))}

f = open("TOP_100_Movies.txt", "w")
for num,movie in movies_dict.items():
    f.write(f"{num}: {movie}\n")
f.close()