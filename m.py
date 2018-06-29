import webbrowser


class M():
    def __init__(self, tittle, story_line, poster, trailer):
        # this function store value of movie tittle, storyline, poster, trailer
        self.title = tittle
        self.storyline = story_line
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        # this function imported webbrowser to open web link
        webbrowser.open(self.trailer_youtube_url)
