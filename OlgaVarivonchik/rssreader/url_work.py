"""Working with url (read news, etc.)"""
import requests
import dateutil.parser
from bs4 import BeautifulSoup
from base_logger import logger


def connect_url(url: str):
    """
     Return the source code for the provided URL.
     Args:
        url (string): URL of the page to scrape.
     Returns:
        response (object): HTTP response object from get_source or None if error
    """
    logger.info('connect_url start') #Logs a message
    headers = {
        'User-Agent': 'Mozilla/5.0',
    }
    try:
        request = requests.get(url, headers)
        return request
    except requests.exceptions.RequestException as e:
        print('Error connection with the specified url!')
        return None


def feed_title_from_soup(soup):
    """
     Read feed title from url
     Args:
       none
     Returns:
       feed_title (string): feed title or None if error
    """
    logger.info('feed_title_from_soup start') #Logs a message
    feed_title = soup.find('title').text
    return feed_title


def get_description(url: str):
    """
    Read description from url with news (if description not found in main url news
     Args:
       url (string): url with news
     Returns:
       description (string): description for url or None if does not contain description
    """
    logger.info('get_description start') #Logs a message
    request = connect_url(url)
    if request == None:
        return None
    soup = BeautifulSoup(request.content, 'html.parser')
    head = soup.find('head')
    if head != None:
        attr = head.find('meta', attrs={'name': 'description'})
    else:
        return None
    if attr != None:
        description = attr.get('content')
    else:
        return None
    return description


def news_active_from_url(url: str, soup, feed_title: str, limit_news: int):
    """
    Read all news from url with limit constraints
    Args:
      url (string): source url
      soup (BeautifulSoup)
      feed_title (string): feed title
      limit (integer): how much news to read (None if unrestricted)
    Returns:
      news_active (dictionary): dictionary with news or None if now news
    """
    logger.info('news_active_from_url start') #Logs a message
    cnt = 0
    news_dict = {}
    news_active = {}
    items = soup.find_all('item')
    for item in items:
        cnt += 1
        if (limit_news != None):
            if (cnt > limit_news):
                break
        guid = item.find('guid').text
        title = item.find('title').text
        link = item.find('link').text
        linkimage = ''
        pubDate_s = dateutil.parser.parse(item.find('pubDate').text).isoformat()
        description_tag = item.find('description')
        if description_tag != None:
            description = description_tag.text
            enclosure = item.find('enclosure')
            if enclosure != None:
                encl_type = enclosure.attrs['type']
                if encl_type != None:
                    if 'image' in encl_type:
                        linkimage = enclosure.attrs['url']
        else:
            description = get_description(link)
            if description == None:
                description = 'No description'
            it = item.find('media:content')
            if it != None:
                linkimage = it.attrs['url']
            else:
                linkimage = ''

        news_dict[guid] = {'title': title, 'link': link, 'pubDate': pubDate_s, 'description': description,
                           'linkimage': linkimage}
    news_active[url] = {'feed_title': feed_title, 'news': news_dict}
    # if no news, return None
    if cnt == 0:
        return None
    return news_active
