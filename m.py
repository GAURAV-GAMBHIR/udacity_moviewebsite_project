import webbrowser


class M():
    def __init__(self, t, story, pi, ty):
        # this function store value of movie tittle, storyline, poster, trailer
        self.title = t
        self.storyline = story
        self.poster_image_url = pi
        self.trailer_youtube_url = ty

    def show_trailer(self):
        # this function imported webbrowser to open web link
        webbrowser.open(self.trailer_youtube_url)
