import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://transcripts.fandom.com/wiki/Cartman%27s_Mom_is_Still_a_Dirty_Slut')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='wikitable')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('td')

f = open("south-park-scripts.txt", "a")

for x in artist_name_list_items:
	f.write(x.text)
f.close()
	