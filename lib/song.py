class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = []
    artists = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.update_counters(self)

    @classmethod
    def update_counters(cls, song):
        cls.count += 1

        if song.genre not in cls.genres:
            cls.genres.append(song.genre)
        if song.artist not in cls.artists:
            cls.artists.append(song.artist)

        if song.genre in cls.genre_count:
            cls.genre_count[song.genre] += 1
        else:
            cls.genre_count[song.genre] = 1

        if song.artist in cls.artist_count:
            cls.artist_count[song.artist] += 1
        else:
            cls.artist_count[song.artist] = 1