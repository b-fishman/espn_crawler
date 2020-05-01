import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from pandas import DataFrame

url = 'http://www.espn.com/college-football/weekly/_/seasontype/2'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())

header = soup.find('tr', attrs={'class': 'colhead'})
columns = [col.get_text() for col in header.find_all('td')]
final_df = pd.DataFrame(columns=columns)
final_df

players = soup.find_all('tr', attrs={'class': re.compile('row player-23-')})
# print(players)
for player in players:
    stats = [stat.get_text() for stat in player.find_all('td')]
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    final_df = pd.concat([final_df, temp_df], ignore_index=True)
    print(final_df)
