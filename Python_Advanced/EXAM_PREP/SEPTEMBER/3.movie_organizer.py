def movie_organizer(*args):
    film_genres = {}

    for movie_name, genre in args:
        if genre not in film_genres:
            film_genres[genre] = []
        film_genres[genre].append(movie_name)

    sorted


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))