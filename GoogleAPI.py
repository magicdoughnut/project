from googleapiclient.discovery import build
import pprint
import time
import datetime
import os.path

my_api_key = "xxxxxxxxxxxxxx"
my_cse_id = "xxxxxxxxxxxxx"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, dateRestrict = 'd1', **kwargs).execute()
    searchInfro = res['searchInformation']
    return searchInfro['totalResults']


results = google_search(
    'Washington DC Corrections Center bids', my_api_key, my_cse_id, num=10)

fname = '/work/WDC_Corrections_results.txt'
if os.path.isfile(fname):
	f = open(fname, 'a' )
else:
	f = open(fname, 'w' )
f.write(str(int(results))+',')
f.close()



results = google_search(
    'Washington DC Street Light Modernisation bids', my_api_key, my_cse_id, num=10)

fname = '/work/WDC_Streetlight_results.txt'
if os.path.isfile(fname):
	f = open( fname, 'a' )
else:
	f = open( fname, 'w' )
f.write(str(int(results))+',')
f.close()



results = google_search(
    'Washington DC Police Facilities bids', my_api_key, my_cse_id, num=10)

fname = '/work/WDC_Streetlight_results.txt'
if os.path.isfile(fname):
	f = open( fname, 'a' )
else:
	f = open( fname, 'w' )
f.write(str(int(results))+',')
f.close()



results = google_search(
    'Washington DC Parks and Recreation Facilities bids', my_api_key, my_cse_id, num=10)

if os.path.isfile('/Users/markdawson/Documents/Inspiratia/google/WDC_PandR_results.txt'):
	f = open( '/Users/markdawson/Documents/Inspiratia/google/WDC_PandR_results.txt', 'a' )
else:
	f = open( '/Users/markdawson/Documents/Inspiratia/google/WDC_PandR_results.txt', 'w' )
f.write(str(int(results))+',')
f.close()



f = open( '/Users/markdawson/Documents/Inspiratia/google/times.txt', 'w' )
f.write(str(datetime.datetime.now().time()))
f.close()

