from django.contrib.syndication.views import Feed
from portfolio.models import Entry

class LatestEntry(Feed):
	title = "Portfolio Entry"
	link = "/feed/"
	description = "Latest Entry"

	def Items(self):
		return Entry.objects.published()[:5]