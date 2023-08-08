import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


def fetch_webpage_content(url: str) -> str:
    """Fetches content from a given URL and returns it as a string."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def extract_movie_titles(html_content: str) -> list:
    """Extracts movie titles from the given HTML content."""
    soup = BeautifulSoup(html_content, "html.parser")
    all_movies = soup.find_all(name="h3", class_="title")
    return [movie.getText() for movie in all_movies]


def save_movies_to_file(movie_titles: list, filename: str) -> None:
    """Saves movie titles to the specified file."""
    with open(filename, mode="w") as file:
        for movie in movie_titles[::-1]:  # Reversing the list to save in the desired order
            file.write(f"{movie}\n")


if __name__ == "__main__":
    content = fetch_webpage_content(URL)
    movies = extract_movie_titles(content)
    save_movies_to_file(movies, "movies.txt")
