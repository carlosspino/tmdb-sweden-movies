import os
import requests
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials

# Load API key
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def get_top10_swedish_movies():
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "with_origin_country": "SE",
        "sort_by": "popularity.desc"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return [[
        m.get("title", "N/A"),
        m.get("release_date", "N/A"),
        m.get("vote_average", "N/A"),
        m.get("popularity", "N/A")
    ] for m in data["results"][:10]]

def push_to_google_sheets(movies):
    # Authenticate with your Gmail via dummy JSON
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
    client = gspread.authorize(creds)

    sheet = client.open("sweden_movies_tmdb").sheet1
    sheet.clear()
    sheet.append_row(["Title", "Release Date", "Rating", "Popularity"])
    for movie in movies:
        sheet.append_row(movie)

def main():
    movies = get_top10_swedish_movies()
    push_to_google_sheets(movies)
    print("Top 10 Swedish movies added to Google Sheets successfully!")

if __name__ == "__main__":
    main()