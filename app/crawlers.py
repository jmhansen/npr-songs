from app.parsers.utils import get_markup
from app.utils import dedupe_list


def get_npr_links_from_archive_page(archive_url, show_urls=None, depth=10):
    if not show_urls:
        show_urls = []
    markup = get_markup(archive_url)

    shows_raw = markup.find_all(class_='program-show__title')
    show_urls += [show.find('a')['href'] for show in shows_raw]

    # maybe make it into a set from the beginning?
    if show_urls:
        show_urls = dedupe_list(show_urls)

    if len(show_urls) < depth:
        # parse 'https://www.npr.org/programs/morning-edition/2019/03/19/704683333/morning-edition-for-march-19-2019?showDate=2019-03-19'
        oldest_show_date = show_urls[-1].split('showDate=')[-1]
        episode_id = show_urls[-1].split('/')[8]
        # strip the archive url of any url parameters
        cleaned_archive_url = archive_url.split('?date')[0]

        # the episode id is required, so this will add a duplicate url to the list each time
        # which is why we need to dedupe above
        if oldest_show_date and episode_id:
            oldest_show_archive_url = cleaned_archive_url + '?date={}&eid={}'.format(oldest_show_date, episode_id)
            show_urls += get_npr_links_from_archive_page(oldest_show_archive_url, show_urls, depth=depth)

    # dedupe show_urls again
    if show_urls:
        show_urls = dedupe_list(show_urls)

    return show_urls
