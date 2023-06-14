import mechanicalsoup, re, os
from pathlib import Path

curentWorkingDirectory = Path.cwd()

url = 'https://www.wikipedia.org/'

browser = mechanicalsoup.StatefulBrowser()
main_page = browser.get(url)
main_page_html = main_page.soup
form = main_page_html.select("#search-form")[0]

print("What do you want to search for: ")
name = input()
form.select("#searchInput")[0]["value"] = name

search_page = browser.submit(form, url)

search_page_html = search_page.soup
paragraphs = search_page_html.select("h1, h2, h3, p")

home = Path.home()

os.chdir(home / 'Desktop/')

file_name = name
file_name = re.sub(r'\..*?', "", file_name)
with open(file_name + '.txt', 'w+', encoding="utf-8") as wiki_file:
    for paragraph in paragraphs:
        paragraph = re.sub(r'\[.*?\]', "", paragraph.text)
        wiki_file.write(paragraph + '\n')
    wiki_file.close
print("The file is saved on your desktop.")
print("Have a nice day")

os.chdir(curentWorkingDirectory)