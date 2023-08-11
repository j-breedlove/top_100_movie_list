## 100 Movies that You Must Watch
![top_100_movies.png](top_100_movies.png)
1. Clone the repository:
```bash
git clone https://github.com/j-breedlove/top_100_movie_list.git
```
2. Change directory:
```bash
cd top_100_movie_list
```

# Objective

Scrape the top 100 movies of all time from a website. Generate a text file called `movies.txt` that lists the movie titles in ascending order (starting from 1). 
The result should look something like this:

```
1) The Godfather
2) The Empire Strikes Back
3) The Dark Knight
4) The Shawshank Redemption
... and so on
```
The central idea behind this project is to be able to use BeautifulSoup to obtain some data - like movie titles - from a website like Empire's (or from, say Timeout or Stacker that have curated similar lists). 

### ⚠️ Important: Use the Internet Archive's URL

Since websites change very frequently, **use this link** 
```
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
```
from the Internet Archive's Wayback machine.
