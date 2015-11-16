import feedparser, json, urllib2

# search term will only return one entry, as being specific (above-beyond-group-therapy) & podcast entity
BASE_URL = "https://itunes.apple.com/search?term=above-beyond-group-therapy&country=GB&entity=podcast"

# load JSON data from base url into a dict obj
abgt_dict = json.load(urllib2.urlopen(BASE_URL))

if abgt_dict['resultCount'] == 1 :
    # knowing abgt search is one entry returned, ok to use [0]
    feedUrl = abgt_dict['results'][0]['feedUrl']
    artworkUrl30 = abgt_dict['results'][0]['artworkUrl30']
    artworkUrl60 = abgt_dict['results'][0]['artworkUrl60']
    artworkUrl100 = abgt_dict['results'][0]['artworkUrl100']

# parse RSS feed URL
feed = feedparser.parse(feedUrl)
list = feed['entries']


