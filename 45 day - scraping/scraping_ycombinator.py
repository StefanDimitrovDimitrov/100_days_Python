#news.ycomninator.com/robots.txt

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

# print(response.text) ## the same as to read the website in our main file

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# find_all_a_tags = soup.select(selector=".storylink")
# print(find_all_a_tags.getText())

# find_all_a_tags = soup.find_all(name="a", class_= "storylink")
# for tag in find_all_a_tags:
#     print(tag.getText())
#
# find_all_span_tags = soup.find_all(name="span", class_= "score")
# for score in find_all_span_tags:
#     print(score.getText())

# find_first_article = soup.find(name='a', class_="storylink")
# print(find_first_article)
# article_title = find_first_article.getText()
# print(article_title)
# article_link = find_first_article.get("href")
# print(article_link)
# find_first_upvote = soup.find(name="span", class_="score")
# article_upvote = find_first_upvote.getText().split()[0]
# print(article_upvote)

################# create a list with all the titles, lincs and points ##########

articles = [article.getText() for article in soup.find_all(name='a', class_="storylink")]
links = [link.get("href") for link in soup.find_all(name='a', class_="storylink")]
upvote = [int(points.getText().split()[0]) for points in soup.find_all(name="span", class_="score")]

max_index = upvote.index(max(upvote))

print(articles[max_index])
print(links[max_index])
print(upvote[max_index])

#
# print(articles)
# print(links)
# print(upvote)