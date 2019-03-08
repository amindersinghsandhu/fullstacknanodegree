import webbrowser


# Defining Class Movie

class Movie:
    """ This class collect info about Movies and Display them """

    # Constructor def of class defined

    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube
    ):
        """Pulls movie data from entertainment file
        and returns a list a Movie objects"""

        # Instance Variable used to get info of Movies

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        # Instance method show_trailer decleared

    def Show_trailer(self):
        """It Opens Webrowser And open youtube Trailer"""
        webbrowser.open(self.trailer_youtube_url)
