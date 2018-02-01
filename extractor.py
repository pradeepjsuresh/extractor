try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import csv
from bs4 import BeautifulSoup
for t in range(1,10,1):
         quote_page="(the url of the website)"
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	table = soup.find('table', {'class': '<tablename>'})
	for row in table.findAll("tr"):
      		cells = row.findAll("td")
        	if len(cells) == 5:
                	t = cells[0].find(text=True)
                	n = cells[1].find(text=True)
                	m = cells[2].find(text=True)
                	t = cells[3].find(text=True)
                	e = cells[4].find(text=True)
                	with open('output.csv', 'a') as csv_file:
                       		writer = csv.writer(csv_file)
                        	writer.writerow([t, n, m, t, e])

