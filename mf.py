import requests
import re
import json
import pandas as pd
import time
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()


def main():
	main_start = time.time()

	# mention the number of days in range starting from today to history
	for day in range(13,15):
		start = time.time()
		today = (datetime.now() - timedelta(days=day)).strftime('%d-%b-%Y')
		month_name = (datetime.now() - timedelta(days=day)).strftime('%b')
		print(f'\nFetching data for {today}!!!')

		url = os.getenv('RAPID_API_URL')

		querystring = {"SchemeType":"All","Date":today}
		headers = {
			'x-rapidapi-host': os.getenv('RAPID_API_HOST'),
			'x-rapidapi-key': os.getenv('RAPID_API_KEY')
		}
		response = requests.request("GET", url, headers=headers, params=querystring)

		# The response is a list of JSON object in string format
		MF_data = json.loads(response.text)

		# Converting the JSON data to Pandas Dataframe so as to save the data as CSV
		df = pd.DataFrame(MF_data)
		df['Scheme Category'] = df['Scheme Category'].apply(lambda x: re.findall(r'\( (.+) \)', x)[0])

		# creating a destination folder(if doesn't exist) for saving the csv file
		destination_folder = f'./data/{month_name}'
		if (os.path.exists(destination_folder)):
			df.to_csv(f'{destination_folder}/MF_{today}.csv', index=False)
		else:
			os.makedirs(destination_folder)

		end = time.time()
		print(f'Time taken for this operation is {end - start} seconds\n')

	print(f'Total Time taken for the operation is {time.time() - main_start} seconds')

if __name__ == "__main__":
	main()
