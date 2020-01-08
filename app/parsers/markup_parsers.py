

class ShowMarkupParser:

    @staticmethod
    def get_songs(markup_key_class, markup, show_title):
        markup_key = markup_key_class(markup, show_title)
        song_list = markup_key.build_song_list()
        return song_list
