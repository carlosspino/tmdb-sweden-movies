import os
import requests
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials

# Load environment variables from .env
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def get_top10_swedish_movies():
    """
    Call TMDB API /discover/movie and return the top 10 Swedish movies by popularity.
    """
    url = "https://api.themoviedb.org/3/discover/movie"  # TMDB API endpoint

    params = {
        "api_key": TMDB_API_KEY,
        "with_origin_country": "SE",    # Filter for movies from Sweden
        "sort_by": "popularity.desc"    # Sort by descending popularity
    }

    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error if the request fails

    data = response.json()
    movies = data["results"][:10]  # Take only the first 10 movies

    movie_list = []
    for movie in movies:
        movie_list.append([
            movie.get("title", "N/A"),
            movie.get("release_date", "N/A"),
            movie.get("vote_average", "N/A"),
            movie.get("popularity", "N/A")
        ])

    return movie_list

def push_to_google_sheets(movies):
    """
    Push the list of movies to a Google Sheet using Service Account credentials.
    Assumes credentials.json exists and has proper access to the sheet.
    """
    # Define the scopes for Google Sheets API
    scope = ["https://www.googleapis.com/auth/spreadsheets"]

    # Authenticate with Google Service Account
    creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
    client = gspread.authorize(creds)

    # Open the Google Sheet by name
    sheet = client.open("sweden_movies_tmdb").sheet1

    # Clear any existing data in the sheet
    sheet.clear()

    # Write headers
    sheet.append_row(["Title", "Release Date", "Rating", "Popularity"])

    # Append movie rows
    for movie in movies:
        sheet.append_row(movie)

def main():
    movies = get_top10_swedish_movies()
    push_to_google_sheets(movies)
    print("Top 10 Swedish movies added to Google Sheets successfully!")

if __name__ == "__main__":
    main()