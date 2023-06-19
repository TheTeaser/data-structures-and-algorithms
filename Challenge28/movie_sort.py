class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

def sort_by_year(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie.year, reverse=True)
    return sorted_movies

def sort_by_title(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie.title)
    return sorted_movies

movies = [
    Movie("A Good day to die", 1965, ["Meow"]),
    Movie("V for vendetta", 2010, ["Thriller"]),
    Movie("The Dark Knight Rises", 2012, ["Action"]),
    Movie("The Green mile", 1999, ["Drama"]),
    Movie("The Matrix", 1999, ["Action", "Sci-Fi"]),
]

sorted_by_year = sort_by_year(movies)
print('Sorted by year:')
for movie in sorted_by_year:
    print(f"{movie.title} ({movie.year})")
print('Sorted by title:')
sorted_by_title = sort_by_title(movies)
for movie in sorted_by_title:
    print(f"{movie.title} ({movie.year})")