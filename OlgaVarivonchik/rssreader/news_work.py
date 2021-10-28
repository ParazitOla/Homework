"""Module with the function for working with news_all, news_active.
news_all contains all news for all URLs.
news_active contains news generated  according to the specific rules.
"""
import datetime
import dateutil.parser
from base_logger import logger


def news_update(news_all: dict, news_active: dict):
    """
    Update news_all with information from news_active
    Return - dict{} with all information from file
    Read description from url with news (if description not found in main url news
    Args:
      news_all (dictionary): dictionary with all news
      news_active (dictionary): dictionary with news
    Returns:
      news_all (dictionary): dictionary with all news after update with information from news_active
    """
    logger.info('news_update start') #Logs a message
    url = list(news_active.keys())[0]
    dict_from_news_all = news_all.get(url)
    if dict_from_news_all == None:
        news_all.update(news_active)
    else:
        dict_from_news_all['feed_title'] = news_active[url]['feed_title']
        dict_from_news_all_news = dict_from_news_all['news']
        dict_from_new_active_news = news_active[url]['news']
        for item in dict_from_new_active_news:
            dict_from_news_all_news[item] = dict_from_new_active_news[item]
        dict_from_news_all['news'] = dict_from_news_all_news
        new_dict = {url: dict_from_news_all}
        news_all.update(new_dict)
    return news_all


def news_dict_fill(news_item_url: dict, limit_news: int, limit_date: datetime.date):
    """
    Apply filter to news from one site (news_item_url)
    Args:
      news_item_url (dictionary): news for one url
      limit_news (integer): limit of news count
      limit_date (datetime.date): limit of date
    Returns:
      news_dict (dictionary): news from news_item_url after apply all filter's or empty dictionary
    """
    logger.info('news_dict_fill start') #Logs a message
    news_dict = {}
    cnt = 0
    for item_news in news_item_url:
        pubDate_s = news_item_url[item_news]['pubDate']
        pubDate = dateutil.parser.parse(pubDate_s).date()
        # Check for date limit
        if pubDate == limit_date:
            cnt += 1
            if limit_news != None:
                if cnt > limit_news:
                    break
            # print(f'limit_date:{limit_date}/pubDate:{pubDate}')
            title = news_item_url[item_news]['title']
            link = news_item_url[item_news]['link']
            linkimage = news_item_url[item_news]['linkimage']
            description = news_item_url[item_news]['description']
            news_dict[item_news] = {'title': title, 'link': link, 'pubDate': pubDate_s, 'description': description,
                                    'linkimage': linkimage}
    return news_dict


def news_active_from_news_all(news_all: dict, url: str, limit_news: int, limit_date: datetime.date):
    """
    Fill news_active with information from news_all with restriction from command line
    Args:
      news_all (dictionary): dictionary with all news
      url (string): source RSS url or None (if url not provided)
      limit_news (integer): limit of news count
      limit_date (datetime.date): limit of date
    Returns:
      news_active (dictionary): dictionary with news or empty dictionary
    """
    logger.info('news_active_from_news_all start') #Logs a message
    news_active = {}
    if url == None:
        for item_url in news_all:
            dict_from_news_all = news_all[item_url]
            news_item_url = dict_from_news_all['news']
            news_dict = news_dict_fill(news_item_url, limit_news, limit_date)

            if len(news_dict) != 0:
                feed_title = dict_from_news_all['feed_title']
                news_active[item_url] = {'feed_title': feed_title, 'news': news_dict}
    else:
        dict_from_news_all = news_all.get(url)
        if dict_from_news_all != None:
            news_item_url = dict_from_news_all['news']
            news_dict = news_dict_fill(news_item_url, limit_news, limit_date)
            if len(news_dict) != 0:
                feed_title = dict_from_news_all['feed_title']
                news_active[url] = {'feed_title': feed_title, 'news': news_dict}
    return news_active
