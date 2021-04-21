from bs4 import BeautifulSoup
#import lxml
with open('website.html') as file:
    contents = file.read()

# print tag and the textContent
soup = BeautifulSoup(contents, "html.parser") # "lxml"
print(soup.title) # print the tag
print(soup.title.string) # print the textContent
#print(soup.prettify()) # print the html formatted
print(soup.p) # print first paragraph

all_anchor_tags = soup.find_all(name = "a") #all a tags
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText()) # get the textContent
    print(tag.get("href")) # get the link

heading = soup.find(name="h1", id="name")# get the specific h1 tag by ### id ###
print(heading)

section_heading = soup.find(name="h3", class_= "heading") # get by class IMPORTANT class_
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get("class"))

################# css selectors ########################
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)
