# TMDB Sweden Movies → Google Sheets

This small project fetches the **Top 10 Swedish movies** from the TMDB API and writes them to a Google Sheet using the Google Sheets API.

The goal of this script is to demonstrate:

- API consumption
- Data filtering
- Integration with Google APIs
- Basic automation with Python


## API Used

This project uses the **TMDB Discover endpoint**.

`/discover` allows searching for movies using filters such as:

- ratings
- release dates
- certifications
- country of origin

Documentation reference:

/discover - Sometimes it useful to search for movies and TV shows based on filters or definable values like ratings, certifications or release dates. The discover method make this easy.


Example request used in this project:

https://api.themoviedb.org/3/discover/movie

Parameters used:

- with_origin_country=SE (ISO code of Sweden)
- sort_by=popularity.desc (Watched in the API documentation)


This returns movies produced in Sweden ordered by popularity.


## Features

The script:

1. Fetches Swedish movies from TMDB
2. Selects the top 10 most popular results
3. Extracts relevant fields:
   - title
   - release date
   - rating
   - popularity
4. Pushes the data to Google Sheets


## Setup

### 1 Create TMDB API key

Create an API key from:

https://www.themoviedb.org/settings/api


### 2 Create a `.env` file
TMDB_API_KEY=*********

### 3 Install dependencies
pip install -r requirements.txt



### 4 Google Cloud Setup

1. Create a Google Cloud project
2. Enable **Google Sheets API**
3. Create a **Service Account**
4. Download `credentials.json`
5. Place the file in the project root


### 5 Create Google Sheet

Create a Google Sheet called:
sweden_movies_tmdb


Share the sheet with the **service account email**.


## Run the script
python main.py



## Output

The Google Sheet will be populated with:

| Title | Release Date | Rating | Popularity |
|------|------|------|------|


## Time Spent

30 minutes