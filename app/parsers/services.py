from app.parsers.markup_keys import NPRGenericShowMarkupKey
from app.parsers.markup_parsers import ShowMarkupParser
from app.parsers.utils import get_markup


def get_songs_for_generic_npr_episode(url, show_title):
    markup = get_markup(url)
    song_list = ShowMarkupParser.get_songs(NPRGenericShowMarkupKey, markup, show_title)
    return song_list
