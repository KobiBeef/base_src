import json
import os
import urllib.request

def api_populate():
	url_raw = 'https://api.flickr.com/services/rest/?'
	method = 'method=flickr.photosets.getList&'
	api_key = 'api_key=a3dea358a147f92249be598f27ace739&'
	format = 'format=json&nojsoncallback=1&'
	auth_key = 'auth_token=72157656903966634-ca85d90751c3f2d2&'
	api_sig = 'api_sig=861d03dc5665d37896ef4f6d4a842592'
	url = url_raw + api_key + method +format + auth_key + api_sig
	
	response = urllib.request.urlopen(url).read().decode('utf-8')
	json_obj = json.loads(response)

	for items in json_obj['photosets']['photoset']:
		add_item(items['title']['_content'], items['photos'], items['count_views'])

def add_item(api_title, api_pic_count, api_view_count):
	flickr_api = MultiMediaApi.objects.get_or_create(api_title=api_title, api_pic_count=api_pic_count, api_view_count=api_view_count)
	return flickr_api

if __name__ == '__main__':
	# print ("Starting population script api testprograms..")
	print ("selecting objects..")
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
	from testprograms.models import MultiMediaApi
	api_populate()


# test comment for verification