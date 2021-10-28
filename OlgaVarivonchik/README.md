
RSS-reader is implemented with  Python 3.9.

RSS-reader this is a command-line utility which receives URL and prints results in human-readable format.
User can run this application both with and without installation of CLI utility.

Format of the news console output:
___________________________________________________
RSS URL: Link RSS
Feed: Title of the feed
 
Title: Title of the news
Date: Date of publication of the news (in format: Sun, 20 Oct 2019 04:21:44 +0300)
Link: The news' link
Description: Short news description. 
Links:
[1] news link
[2] image link (or message that you have no image there)
___________________________________________________

Example:
___________________________________________________
RSS URL: https://www.kommersant.ru/RSS/main.xml
Feed: Новости ООН 
 
Title: День рождения ООН на ЭКСПО в Дубае
Date: Sun, 24 Oct 2021 13:34:01 -0400
Link: https://www.kommersant.ru/doc/5050407
Description: Международное сотрудничество – единственное эффективное средство для решения актуальных проблем современности. Наглядным примером этому стала борьба с пандемией. 
Links:
[1] https://www.kommersant.ru/doc/5050407 
[2]: https://www.kommersant.ru/Issues.photo/DAILY/2021/195/KSP_015446_00002_1_t219_230836.jpg (image)
___________________________________________________


The RSS-reader can run with additional arguments:

  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided
  --date         A date in `%Y%m%d` format 
  --to-html      Converts news to HTML format and saves it to a local file
  --to-pdf       Converts news to PDF format and saves it to a local file
  --colorize     Colorize news

The arguments --date works with both --json, --limit, --verbose, --to-html, --to-pdf,  --colorize and their different combinations.
If --date specified together with RSS source, then RSS-reader can get news for this date from local cache that were fetched from specified source

The optional argument --colorize print the result of the utility in colorized mode only at console output.

The news converted at format: .html, .pdf

Format convertation process influenced by --limit argument.
If --json is specified together with convertation options, then JSON news printed to stdout, and converted file contain news in normal format.



JSON format:
___________________________________________________

{
    link_RSS_1: {
        "feed_title_1": Item_title_from_RSS,
        "news": {
            "news_guid_1*": {
                "title": name_of_the_news,
                "link": link_of_the_news,
                "pubDate": the_publishing_date,
                "description": shot_description
				"linkimage":link_of_the_image
            },
        "news": {
            "news_guid_2*": {
                "title": name_of_the_news,
                "link": link_of_the_news,
                "pubDate": the_publishing_date,
                "description": shot_description
				"linkimage":link_of_the_image
            }
		}
	},	
	link_RSS_2: {
        "feed_title_2": Item_title_from_RSS,
        "news": {
            "news_guid_3*": {
                "title": name_of_the_news,
                "link": link_of_the_news,
                "pubDate": the_publishing_date,
                "description": shot_description
				"linkimage":link_of_the_image
            },
        "news": {
            "news_guid_4*": {
                "title": name_of_the_news,
                "link": link_of_the_news,
                "pubDate": the_publishing_date,
                "description": shot_description
				"linkimage":link_of_the_image
            }	
		}
    }
}
*news guid Unique identifier of the item from RSS
___________________________________________________

Examle:
___________________________________________________

{
    "https://news.yahoo.com/rss/": {
        "feed_title": "Yahoo News - Latest News & Headlines",
        "news": {
            "colombia-announces-capture-one-most-233233294.html": {
                "title": "Colombia's most wanted drug lord captured in jungle raid",
                "link": "https://news.yahoo.com/colombia-announces-capture-one-most-233233294.html",
                "pubDate": "2021-10-23T23:32:33+00:00",
                "description": "Colombian security forces have captured the country\u2019s most wanted drug trafficker, a rural farmers.",
				"linkimage": "https://s.yimg.com/uu/api/res/1.2/sbSt9k2i59Ne3T5Dahi7dg--~B/aD0xNTAwO3c9MjAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/1fc569ce977352662b4cf3039acae975"

            },
            "trump-weekend-freakout-over-horrible-040447931.html": {
                "title": "Trump Has Weekend Freakout Over 'Horrible' Fox News Ads",
                "link": "https://news.yahoo.com/trump-weekend-freakout-over-horrible-040447931.html",
                "pubDate": "2021-10-25T04:04:47+00:00",
                "description": "The former guy had a meltdown over his once-favorite network for running ads critical of him."
				"linkimage": "https://s.yimg.com/uu/api/res/1.2/sbSt9k2i59Ne3T5Dahi7dg--~B/aD0xNTAwO3c9MjAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/1fc569ce977352662b4cf3039acae975"

            }
        }
    },
    "https://news.un.org/feed/subscribe/ru/news/all/rss.xml": {
        "feed_title": "\u041d\u043e\u0432\u043e\u0441\u0442\u0438 \u041e\u041e\u041d",
        "news": {
            "https://news.un.org/feed/view/ru/story/2021/10/1412462": {
                "title": "\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u041e\u041e\u041d \u043d\u0430",
                "link": "https://news.un.org/feed/view/ru/story/2021/10/1412462",
                "pubDate": "2021-10-24T13:34:01-04:00",
                "description": "\u041c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u043e\u0435 \u0441\u043e\u0442\u0440\\u0043f\u0435\u0440\u0432\u044b\u0439 \u043"
				"linkimage": "https://global.unitednations.entermediadb.net/assets/mediadb/services/module/asset/downloads/preset/Libraries/Production+Library/28-06-2021_Palestine_Ramallah_Shirin_Yaseen_2.jpg/image770x420cropped.jpg"


            },
            "https://news.un.org/feed/view/ru/story/2021/10/1412422": {
                "title": "\u0412 \u0412\u041e\u0417 \u043f\u0440\u0438\u0437\u044b\",
                "link": "https://news.un.org/feed/view/ru/story/2021/10/1412422",
                "pubDate": "2021-10-24T00:40:05-04:00",
                "description": "\u041f\u043e \u0441\u043b\u0443\u0447\u0430\u044e \u0412\u0441\u0435\u043c\u0438\u0440\u043d\u043e\u0433\u043e."
				"linkimage": "https://www.kommersant.ru/Issues.photo/DAILY/2021/195/KMO_090329_01330_1_t219_204214.jpg"

            }
        }
    }
}

___________________________________________________

The RSS news can stored in a local storage. The storage format corresponds to the json format, no string division is used
The storage is located in a working directory.


The utilita is crossplatform, it successfully works both Linux (testing on Oracle Linux) and Windows.

Codebase covered with unit tests with at least 50% coverage:

Name                      Stmts   Miss  Cover   
-------------------------------------------------
base_logger.py                5      0   100%
news_work.py                 55      7    87%   
output_work.py              137     61    55%   
rss_reader.py                95     58    39%   
storage_work.py              19      2    89%   
test\__init__.py              0      0   100%
test\test_rss_reader.py      65      2    97%   
url_work.py                  68     21    69%   
--------------------------------------------------
TOTAL                       444    151    66%

