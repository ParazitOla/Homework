"""Main Module with functions for working rss-reader"""
import argparse
from bs4 import BeautifulSoup
from datetime import datetime
from storage_work import read_storage, write_storage
from output_work import print_news, print_news_pdf, print_news_html, color_term
from news_work import news_update, news_active_from_news_all
from url_work import connect_url, feed_title_from_soup, news_active_from_url
from base_logger import logger

isjson = False
storage_file_name = 'rss_reader.json'
html_file_name = 'rss_reader.html'
pdf_file_name = 'rss_reader.pdf'
source_url = ''
limit_date = None
limit_news = None


def news_from_url(url: str, limit_news: int, file_name):
    """
     All work with news from url
     Args:
       url (string): RSS url
       limit_news (integer): max count news from url, None for all news
     Returns:
       news_active (dictionary): dictionary with news or None if error
    """
    logger.info('news_from_url start') #Logs a message
    request = connect_url(url)
    if request == None:
        return None

    soup = BeautifulSoup(request.content, 'xml')
    feed_title = feed_title_from_soup(soup)
    if feed_title == None:
        print('This is an incorrect RSS url!')
        return None

    news_active = news_active_from_url(url, soup, feed_title, limit_news)

    if news_active == None:
        print('No news!')
        return None

    # read from file to news_all
    news_all = read_storage(file_name)

    # update news_all
    news_all = news_update(news_all, news_active)

    # write news_all to file
    if write_storage(storage_file_name, news_all) == False:
        print('Error while write to local storage!')
    return news_active


def news_from_storage(url: str, limit_news: int, limit_date: datetime.date, file_name):
    """
     All work with news from local storage
     Args:
       file_name (string): file name for local storage
       url (string): source RSS url or None (if url not provided)
       limit_news (integer): limit of news count
       limit_date (datetime.date): limit of date
     Returns:
       news_active (dictionary): dictionary with news or None if error or no news or now news for user request
    """
    logger.info('news_from_storage start') #Logs a message
    news_all = read_storage(file_name)

    if len(news_all) == 0:
        print('No news in local storage!')
        return None

    news_active = news_active_from_news_all(news_all, url, limit_news, limit_date)

    if len(news_active) == 0:
        print('No cached news for you request!')
        return None

    return news_active


def main():
    global storage_file_name
    global isjson
    global source_url
    global limit_news
    global limit_date
    global color

    parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader.')
    parser.add_argument('source', nargs='?', default=None, help='RSS URL')
    parser.add_argument('--version', dest='version', action='store_true', required=False, help='Print version info')
    parser.add_argument('--json', dest='json', action='store_true', required=False, help='Print result as JSON stdout')
    parser.add_argument('--verbose', dest='verbose', action='store_false', required=False,
                        help='Outputs verbose status messages')
    parser.add_argument('--limit', dest='limit', type=int, default=None, required=False,
                        help='Limit news topics if this parameter provided')
    parser.add_argument('--date', dest='limitdate', type=str, default=None, required=False,
                        help='Limit news topics of publishing date')
    parser.add_argument('--to-html', dest='html', action='store_true', required=False,
                        help='Converts news to HTML format')
    parser.add_argument('--to-pdf', dest='pdf', action='store_true', required=False,
                        help='Converts news to PDF format')
    parser.add_argument('--colorize', dest='colorize', action='store_true', required=False,
                        help='Colorize news')

    args = parser.parse_args()

    if args.verbose:
        logger.disable()

    isjson = args.json
    limit_news = args.limit
    color = args.colorize

    if args.version:
        print('Version 1.5')
        exit()

    source_url = args.source

    if (args.limitdate == None) and (source_url == None):
        print('provided URL')
        exit(1)

    if args.limitdate == None:
        limit_date = None
    else:
        try:
            limit_date = datetime.strptime(args.limitdate, "%Y%m%d").date()
        except ValueError:
            print("date must be formatted as YYYYMMDD")
            exit(1)

    if args.limitdate == None:
        news_active = news_from_url(source_url, limit_news, storage_file_name)
    else:
        news_active = news_from_storage(source_url, limit_news, limit_date, storage_file_name)

    if news_active == None:
        exit(1)

    logger.info('Output news for user in txt or json')
    if args.colorize == True:
        logger.info('Colorize in terminal') #Logs a message
        color_term(news_active, color)
    else:
        print_news(news_active, isjson)

    if args.html == True:
        logger.info('Output news into html file') #Logs a message
        print_news_html(news_active, html_file_name)

    if args.pdf == True:
        logger.info('Output news into pdf file') #Logs a message
        print_news_pdf(news_active, pdf_file_name)

    logger.info('Program is ending')


if __name__ == '__main__':
    main()

    # "https://news.yahoo.com/rss/"
    # "https://www.kommersant.ru/RSS/main.xml"
    # "https://feeds.skynews.com/feeds/rss/world.xml"
    # "https://news.un.org/feed/subscribe/ru/news/all/rss.xml"
    # "https://news.yahoo.com/rss/" --limit 2 --verbose
