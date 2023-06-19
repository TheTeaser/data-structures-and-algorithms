import pytest
from Challenge28.movie_sort import sort_by_year, sort_by_title, Movie

class TestMovieSorting:
    @pytest.fixture
    def movies(self):
        return [
            Movie("A Good day to die", 1965, ["Meow"]),
            Movie("V for vendetta", 2010, ["Thriller"]),
            Movie("The Dark Knight Rises", 2012, ["Action"]),
            Movie("The Green mile", 1999, ["Drama"]),
            Movie("The Matrix", 1999, ["Action", "Sci-Fi"]),
        ]

    def test_sort_by_year(self, movies):
        expected_result = [
            Movie("V for vendetta", 2010, ["Thriller"]),
            Movie("The Dark Knight Rises", 2012, ["Action"]),
            Movie("The Matrix", 1999, ["Action", "Sci-Fi"]),
            Movie("The Green mile", 1999, ["Drama"]),
            Movie("A Good day to die", 1965, ["Meow"]),
        ]
        sorted_movies = sort_by_year(movies)
        assert all(
            movie.title == expected.title and movie.year == expected.year
            for movie, expected in zip(sorted_movies, expected_result)
        )

    def test_sort_by_title(self, movies):
        expected_result = [
            Movie("A Good day to die", 1965, ["Meow"]),
            Movie("The Dark Knight Rises", 2012, ["Action"]),
            Movie("The Green mile", 1999, ["Drama"]),
            Movie("The Matrix", 1999, ["Action", "Sci-Fi"]),
            Movie("V for vendetta", 2010, ["Thriller"]),
        ]
        sorted_movies = sort_by_title(movies)
        assert all(
            movie.title == expected.title and movie.year == expected.year
            for movie, expected in zip(sorted_movies, expected_result)
        )
