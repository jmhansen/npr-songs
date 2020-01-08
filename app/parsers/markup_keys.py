

class BaseMarkupKey:
    date_kwargs = None
    songs_kwargs = None
    song_title_kwargs = None
    song_artist_kwargs = None

    def __init__(self, markup, show_title):
        self.markup = markup
        self.show_title = show_title

    def get_show_title(self):
        return self.show_title

    def get_episode_date(self):
        return self.markup.find(**self.date_kwargs).text

    def get_songs_markup(self):
        return self.markup.find_all(class_='song-meta-wrap')

    def build_song_list(self):
        songs_markup = self.get_songs_markup()
        song_list = []

        for i, song in enumerate(songs_markup, 1):
            # solve for empty song_title or artist tag
            if song.find(**self.song_title_kwargs):
                song_title = song.find(**self.song_title_kwargs).text.strip()
            else:
                song_title = ''

            if song.find(**self.song_artist_kwargs):
                artist = song.find(**self.song_artist_kwargs).text.strip()
            else:
                artist = ''

            if song_title and artist:
                song_dict = {
                    'song_title': song_title,
                    'artist': artist,
                    'order': i,
                    'program': self.get_show_title(),
                    'date': self.get_episode_date()
                }
                song_list.append(song_dict)

        return song_list


class NPRGenericShowMarkupKey(BaseMarkupKey):
    date_kwargs = {'class_': 'date'}
    songs_kwargs = {'class_': 'song-meta-wrap'}
    song_title_kwargs = {'class_': 'song-meta-title'}
    song_artist_kwargs = {'class_': 'song-meta-artist'}

    def get_episode_date(self):
        raw_show_date = super().get_episode_date()
        show_date = raw_show_date.splitlines()[2].lstrip()
        return show_date
