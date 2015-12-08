from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns(
	'',
	################ INDEX URLS ################
	url(r'^$', views.OverviewListView.as_view(), name='index'),
	
	################ ENTRY URLS ################
	url(r'^entry/$', views.EntryListView.as_view(), name='entry_list'),
	url(r'^entry/(?P<category>\S+)/(?P<slug>\S+)$', views.entryDetailView, name='testprogram_entry_detail'),

	################ ABOUT URLS ################
	url(r'^about/$', views.AboutDetailView.as_view(), name='testprograms_about'),

	################ ABOUT URLS ################
	url(r'^programming/$', views.ProgramTutorialListView.as_view(), name='programming_list'),
	url(r'^programming/(?P<category>\S+)/(?P<slug>\S+)$', views.programTutorialDetailView, name='programning_detail'),

	################ INTERWEBS URLS ################
	url(r'^interwebs/$', views.WebThemeListView.as_view(), name='testprograms_webtheme_list'),
	url(r'^interwebs/(?P<category>\S+)/(?P<slug>\S+)$', views.WebThemeDetailView.as_view(), name='testprograms_webtheme_detail'),

	################ HARDWARE URLS ################
	url(r'^hardware/$', views.HardwarePostListView.as_view(), name='testprograms_hardwarepost_list'),
	url(r'^hardware/(?P<category>\S+)/(?P<slug>\S+)$', views.hardwarePostDetailView, name='testprograms_hardwarepost_detail'),

	################ MULTIMEDIA URLS ################
	url(r'^multimedia/$', views.MultimediaListView.as_view(), name='testprograms_multimedia_list'),

	################ CONTACT URLS ################
	url(r'^contact/$', views.contact, name='testprograms_contact'),

	################ TEST URLS ################
	# url(r'^test/$', views.overviewListView, name='testprograms_overview')
)