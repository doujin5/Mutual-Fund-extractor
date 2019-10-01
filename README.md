# Mutual Fund Extractor
This app collects data about all mutual funds datewise **latest-mutual-funds** via the API provided at [Rapid API](rapidapi.com) and stores the data in a segregated manner in `data` folder.

### Setup

1. Install Pipenv as `pip install pipenv`
2. Run `pipenv shell` to start the virtual environment.
3. Run all the dependencies as `pipenv install`
4. Create `.env` file and store the keys as given in `.env.example` file.
5. The Rapid API Key, Host and URL can be got from this [Link](https://rapidapi.com/suneetk92/api/latest-mutual-fund-nav?endpoint=apiendpoint_78274348-459c-4f50-8234-3acf2999b184). (Note: You have to signup at rapidapi.com to get the keys)
6. Run `python mf.py` to start the script.
7. The resulting data can be found inside the `data` folder.

### Application of Data
The data can be used for 
- Data Analysis 
- Pattern Matching
- Data Science
- Predicting upcoming status of Mutual funds.