"""Module with the functions of working with printing for the user"""
import json
import dateutil.parser
import textwrap
import os
from fpdf import FPDF
from colorama import init as c_init, Fore, Back, Style
from base_logger import logger

c_init() # will filter ANSI escape sequences out of any text sent to stdout


def print_news_json(dict_for_output: dict):
    """
    Output news in json format
    Args:
      dict_for_output (dictionary): dictionary with news for output
    Returns:
      none
    """
    logger.info('print_news_json start') #Logs a message
    json_object = json.dumps(dict_for_output, indent=4, ensure_ascii=False)
    print(json_object)
    return


def print_news_text(dict_for_output: dict):
    """
    Output news in text format
    Args:
      dict_for_output (dictionary): dictionary with news for output
    Returns:
      none
    """
    logger.info('print_news_text start') #Logs a message
    for item_feed in dict_for_output:
        print('=============================================')
        print(f'RSS URL: {item_feed}')
        print('Feed: %s \n ' % dict_for_output[item_feed]['feed_title'])
        for item_news in dict_for_output[item_feed]['news']:
            print('Title: %s' % dict_for_output[item_feed]['news'][item_news]['title'])
            pubDate_s = dict_for_output[item_feed]['news'][item_news]['pubDate']
            pubDate = dateutil.parser.parse(pubDate_s)
            pubDate_s = pubDate.strftime('%a, %d %b %Y %H:%M:%S %z')
            print('Date: %s' % pubDate_s)
            link = dict_for_output[item_feed]['news'][item_news]['link']
            print('Link: %s' % link)
            print('Description: %s' % dict_for_output[item_feed]['news'][item_news]['description'])
            print('Links:')
            print('[1]: %s ' % link)
            linkimage = dict_for_output[item_feed]['news'][item_news]['linkimage']
            if linkimage != '':
                print('[2]: %s (image)' % linkimage)
            else:
                print('[2]: No image')
            print()
        print('=============================================')
    return


def print_news_html(dict_for_output: dict, html_file_name: str):
    """
    Converts news to HTML format and saves it to a local file
     Args:
       dict_for_output (dictionary): dictionary with news for convertation
     Returns:
       none
     """
    logger.info('print_news_html start') #Logs a message
    s_html = '''<html><head><title>rss_reader</title></head><body><div class="text-block"><div class="paragraph">'''
    for item_feed in dict_for_output:
        s_html = s_html + f'RSS URL: {item_feed}<br>'
        s_html = s_html + 'Feed: %s \n ' % dict_for_output[item_feed]['feed_title'] + '<br><br>'
        for item_news in dict_for_output[item_feed]['news']:
            title = 'Title: %s' % dict_for_output[item_feed]['news'][item_news]['title']
            s_html = s_html + title + '<br>'
            pubDate_s = dict_for_output[item_feed]['news'][item_news]['pubDate']
            pubDate = dateutil.parser.parse(pubDate_s)
            pubDate_s = pubDate.strftime('%a, %d %b %Y %H:%M:%S %z')
            s_html = s_html + 'Date: %s' % pubDate_s + '<br>'
            link = dict_for_output[item_feed]['news'][item_news]['link']
            s_html = s_html + 'Link: <a href={}>{}</a>'.format(link, link) + '<br>'
            description = 'Description: %s' % dict_for_output[item_feed]['news'][item_news]['description']
            s_html = s_html + description + '<br>'
            linkimage = dict_for_output[item_feed]['news'][item_news]['linkimage']
            if linkimage != '':
                s_tmp = f'''
                <a href="{linkimage}" class="list-group-item list-group-item-action d-flex gap-3 py-3" \\ 
                aria-current="true">
                    <img src="{linkimage}" alt="twbs" width="150" class= flex-shrink-0">
                    <div class="d-flex gap-2 w-100 justify-content-between">
                    </div>
                </a>'''
                s_html = s_html + s_tmp
            s_html = s_html + '<br>'
        s_html = s_html + '<hr>'
    s_html = s_html + '''</div></div></body></html>'''
    try:
        with open(html_file_name, "w", encoding="utf-8") as file:
            file.write(s_html)
    except:
        print('Error writing news in HTML format to file!')
    return


def print_news_pdf(dict_for_output: dict, pdf_file_name: str):
    """
    Converts news to PDF format and saves it to a local file
      Args:
         dict_for_output (dictionary): dictionary with news for convertation
      Returns:
         none
    """
    logger.info('print_news_pdf start') #Logs a message

    def print_l(pdf, s: str, ln: int):
        lines = textwrap.wrap(s, ln, break_long_words=False)
        for line in lines:
            pdf.cell(200, 5, txt=line, ln=1, align='L')
        return

    max_l = 90
    pdf = FPDF()
    pdf.WIDTH = 210
    pdf.HEIGHT = 297
    font_file = os.path.join(os.path.dirname(__file__), 'DejaVuSans.ttf')
    pdf.add_font('DejaVu', '', font_file, uni=True)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.set_font('DejaVu', '', 10)
    for item_feed in dict_for_output:
        pdf.cell(200, 5, txt="================================", ln=1, align='L')
        print_l(pdf, f'RSS URL: {item_feed}', max_l)
        print_l(pdf, 'Feed: %s \n ' % dict_for_output[item_feed]['feed_title'], max_l)
        pdf.cell(200, 5, txt='', ln=1, align='L')
        for item_news in dict_for_output[item_feed]['news']:
            print_l(pdf, 'Title: %s' % dict_for_output[item_feed]['news'][item_news]['title'], max_l)
            pubDate_s = dict_for_output[item_feed]['news'][item_news]['pubDate']
            pubDate = dateutil.parser.parse(pubDate_s)
            pubDate_s = pubDate.strftime('%a, %d %b %Y %H:%M:%S %z')
            pdf.cell(200, 5, txt='Date: %s' % pubDate_s, ln=1, align='L')
            print_l(pdf, 'Link: %s' % dict_for_output[item_feed]['news'][item_news]['link'], max_l)
            print_l(pdf, 'Description: %s' % dict_for_output[item_feed]['news'][item_news]['description'], max_l)
            linkimage = dict_for_output[item_feed]['news'][item_news]['linkimage']
            if linkimage != '':
                print_l(pdf, 'Link image: %s' % linkimage, max_l)
            pdf.cell(200, 5, txt='', ln=1, align='L')
        pdf.cell(200, 5, txt="================================", ln=1, align='L')
    try:
        pdf.output(pdf_file_name)
    except:
        print('Error write in PDF format!')
    return


def print_news(news_active: dict, isjson: bool):
    """
    Output information for user
    Args:
      news_active (dictionary): dictionary with news
      isjson (boolean): if True - output in JSON format
    Returns:
      none
    """
    logger.info('print_news start') #Logs a message
    if isjson:
        print_news_json(news_active)
    else:
        print_news_text(news_active)
    return


def color_term(dict_for_output: dict, color: bool):
    """
    Make print the result of the utility in colorized mode
    Args:
    dict_for_output (dictionary): dictionary with news
    color (boolean): if True - print the output
    Returns
    none
    """
    logger.info('color_term start') #Logs a message
    if color:
        for item_feed in dict_for_output:
            print(Fore.BLUE, Back.YELLOW + '=============================================', Style.RESET_ALL)
            print(Style.BRIGHT, Fore.YELLOW + f'RSS URL: {item_feed}', Style.RESET_ALL)
            print(Style.BRIGHT, Fore.YELLOW + 'Feed: %s \n ' % dict_for_output[item_feed]['feed_title'],
                  Style.RESET_ALL)
            for item_news in dict_for_output[item_feed]['news']:
                print(Fore.MAGENTA + 'Title: %s' % dict_for_output[item_feed]['news'][item_news]['title'])
                pubDate_s = dict_for_output[item_feed]['news'][item_news]['pubDate']
                pubDate = dateutil.parser.parse(pubDate_s)
                pubDate_s = pubDate.strftime('%a, %d %b %Y %H:%M:%S %z')
                print(Fore.CYAN + 'Date: %s' % pubDate_s)
                link = dict_for_output[item_feed]['news'][item_news]['link']
                print(Fore.BLUE + 'Link: %s' % link)
                print(Fore.GREEN + 'Description: %s' % dict_for_output[item_feed]['news'][item_news]['description'])
                print(Fore.BLACK, Back.WHITE + 'Links:', Style.RESET_ALL)
                print(Fore.RED + '[1]: %s ' % link)
                linkimage = dict_for_output[item_feed]['news'][item_news]['linkimage']
                if linkimage != '':
                    print('[2]: %s (image)' % linkimage)
                else:
                    print('[2]: No image')
                print()
            print(Fore.BLUE, Back.YELLOW + '=============================================', Style.RESET_ALL)
    return
