# Authors: Rachel Dunn, Laura GF, Anouk de Brouwer, Courtney V, Janson Lin
# Date created: Sept 12 2020
# Date modified: 

# Import libraries 
from datetime import datetime
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import sys

##usage: python web_scrapping.py https://www.waterlevels.gc.ca/eng/data/table/2020/wlev_sec/7965 2020-01-01 2020-04-30

def parseData(dataURL, startTime, endTime):
	r = requests.get(dataURL)
	soup = BeautifulSoup(r.text, 'html.parser')

	tables = soup.find_all(class_='width-100')

	date = []
	height = []
	for table in tables:
	
		# get month and year from caption
		month_year = table.find("caption").text.strip()
		[month,year] = month_year.split()
	
		# get all cells by looking for 'align-right' class
		cell = table.find_all(class_="align-right")
	
		# loop over cells in table
		# every 1st cell has the day, every 2nd cell has the time, every 3rd cell has the height 
		for index in range(len(cell)):
		
			# get day
			if ((index % 3) == 0):
				d = cell[index].text.strip()
		
			# get time 
			if ((index % 3) == 1):
				t = cell[index].text.strip()
			
				# paste year, month, day and time together, and append to date list
				ymdt_str = '-'.join([year,month,d,t])
				#ymdt = datetime.strptime(ymdt_str,'%Y-%B-%d-%I:%M %p')
				date.append(ymdt_str)
		
			# get tide height
			if ((index % 3) == 2):
				height.append(cell[index].text.strip())

	#add lists to dataframe
	tides = pd.DataFrame()
	tides['Date'] = pd.to_datetime(date)
	tides['Height_m'] = pd.to_numeric(height)

	#index dataframe by date
	tides.set_index('Date',inplace=True)
	#subset dataframe to only output data between requested dates
	tidesSubset = tides.loc[startTime:endTime,]
	print(tidesSubset)
	tidesSubset.to_csv(r'./tidesSubset.csv', header = True)


if __name__ == "__main__":
	
	#parse arguments
	str(sys.argv)
	dataURL = str(sys.argv[1])
	startTime = str(sys.argv[2])
	endTime = str(sys.argv[3])
	parseData(dataURL, startTime, endTime)

