import fresh_tomatoes
import media

# Class Instances Defining

Padman = media.Movie("Padman",
                     "Padman who invented low-cost sanitary pads",
                     "https://upload.wikimedia.org/wikipedia/en/f/ff/Padman_poster.jpeg",  # noqa
                     "https://www.youtube.com/watch?v=-K9ujx8vO_A"
                     )

Black_panther = media.Movie("Black Panther",
                            "Black Panther is a  film based on"
                            "the Marvel Comics character.",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU"
                            )
Wonder_woman = media.Movie("Wonder Woman",
                           "Wonder Woman is a blend of an uplifting & humorous"
                           "outlook with strong female characters.",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",  # noqa
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo"
                           )
Deadpool_two = media.Movie("Deadpool 2",
                           "Deadpool 2 is an film based on the"
                           "Marvel Comics character Deadpool.",
                           "https://upload.wikimedia.org/wikipedia/en/c/cf/Deadpool_2_poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=I4tFNfROlqk"
                           )
Avengers = media.Movie("Avengers: Infinity War",
                       "Avengers: Infinity War is an film based on"
                       "the Marvel Comics superhero team the Avengers.",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/9/90/Avengers_Infinity_War.jpg/220px-Avengers_Infinity_War.jpg",  # noqa
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
Incredibles_two = media.Movie("Incredibles 2",
                              "Incredibles 2 is an upcoming American"
                              "3D computer-animated superhero film.",
                              "https://upload.wikimedia.org/wikipedia/en/2/27/The_Incredibles_2.jpg",  # noqa
                              "https://www.youtube.com/watch?v=ZJDMWVZta3M"
                              )

# Using an Array(movies) to Display the list

movies = [
    Padman,
    Black_panther,
    Wonder_woman,
    Deadpool_two,
    Avengers,
    Incredibles_two,
    ]

# Using fresh_tomatoes.py to convert instances into Html file.

fresh_tomatoes.open_movies_page(movies)
