"""Configuration for API requests and general script globals

"""
import os

STATUS_FILE = os.path.dirname(os.path.abspath(__file__)) + '/logs/status.log'
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/output/'

VIEWSTAT_FILE = os.path.dirname(os.path.abspath(__file__)) + '/viewstat.cfg'
EVENTVALIDATON_FILE = os.path.dirname(os.path.abspath(__file__)) + '/eventvalidation.cfg'

URI = '' # Place the URL
TOTAL_ENTRY = 21283
NUMBER_OF_PAGES = 2065

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Content-Length': '44116',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'CookieCheck=Detected; ASP.NET_SessionId=j34bwjr5iwkrwx1taridcdiz',
    'Host': '185.47.49.235',
    'Origin': '', # Place the URL
    'Referer': '', # Place the URL
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

GET_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'CookieCheck=Detected; ASP.NET_SessionId=j34bwjr5iwkrwx1taridcdiz',
    'Host': '', #Place the IP
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

FORM_FIELDS = {
   '__EVENTTARGET': r'GridView1',
   '__EVENTARGUMENT': r'UNDEF__EVENTARGUMENT',
   '__VIEWSTATE': r'UNDEF__VIEWSTAT',
   '__VIEWSTATEGENERATOR': r'900CEDFE',
   '__VIEWSTATEENCRYPTED': r'',
   '__EVENTVALIDATION': r'UNDEF__EVENTVALIDATION',
   'NameTXT': r'',
   'LnameTXT': r'',
   'MeliTXT': r'',
   'OzviatTXT': r'',
   'ParvaneTXT': r'',
   'txtTarahi': r'',
   'txtNezarat': r'',
   'ReshteDRP': r'0'
}

INITIAL_FIELDS = {
   '__EVENTTARGET': r'',
   '__EVENTARGUMENT': r'',
   '__VIEWSTATE': r'UNDEF__VIEWSTAT',
   '__VIEWSTATEGENERATOR': r'900CEDFE',
   '__VIEWSTATEENCRYPTED': r'',
   '__EVENTVALIDATION': r'UNDEF__EVENTVALIDATION',
   'NameTXT': r'',
   'LnameTXT': r'',
   'MeliTXT': r'',
   'OzviatTXT': r'',
   'ParvaneTXT': r'',
   'txtTarahi': r'',
   'txtNezarat': r'',
   'ReshteDRP': r'0',
   'Button1': r'جستجو',
}



# https://docs.python.org/3/howto/logging.html
# https://docs.python.org/3/library/logging.html
# LOG_SETTING = {
    # 'LEVEL' = ,
    # 'FILENAME' = ,
    # 'PATH' = ,
    # 'DATETIME' = ,
    # 'FORMAT' = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s',
    # 'MESSAGE' = ,
# }

