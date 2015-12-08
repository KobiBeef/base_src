import json
import urllib
from urllib.request import urlopen

url = 'https://api.flickr.com/services/rest/?method=flickr.photosets.getList&api_key=3c76b6b882164694d0a47353d0e74d58&format=json&nojsoncallback=1&auth_token=72157658955848635-e6e54f84bd64fcf2&api_sig=11e9248395edc065a852133a293d2303'

json_obj = urlopen(url).read()

data = json.loads(json_obj.decode('utf-8'))

print (data['photosets'])

photosets = data['photosets']

print (photosets['photoset'])

for item in photosets['photoset']:
	print (item['photos	'])

# for item in data['photosets']:
# 	print (item)

# { "photosets": { "cancreate": 1, "page": 1, "pages": 1, "perpage": 2, "total": 2, 
#     "photoset": [
#       { "id": "72157656611518554", "primary": "20997961923", "secret": "a24404bec8", "server": "5695", "farm": 6, "photos": 2, "videos": 0, 
#         "title": { "_content": "Test Album" }, 
#         "description": { "_content": "Test Album Description" }, "needs_interstitial": 0, "visibility_can_see_set": 1, "count_views": 5, "count_comments": 0, "can_comment": 1, "date_create": "1442906576", "date_update": "1442933993" },
#       { "id": "72157658893475746", "primary": "21439230920", "secret": "d9fbc63379", "server": "5638", "farm": 6, "photos": 2, "videos": 0, 
#         "title": { "_content": "test album 2" }, 
#         "description": { "_content": "test album 2 desciption" }, "needs_interstitial": 0, "visibility_can_see_set": 1, "count_views": 0, "count_comments": 0, "can_comment": 1, "date_create": "1442932668", "date_update": "1442933993" }
#     ] }, "stat": "ok" }