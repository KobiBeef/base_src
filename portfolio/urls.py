from django.conf.urls import patterns, url, include
# from portfolio.views import *
from . import views, feed

urlpatterns = patterns(
	'',
	########################
	# decommissioning this #
	########################
	# url(r'^$', views.IndexView.as_view(), name='index,'),
	# replaced by this #
	####################
	url(r'^$', views.IndexView.as_view(), name="new_index"),

	url(r'^about/$', views.AboutView.as_view(), name='about'),
	url(r'^entry/(?P<category>\S+)/(?P<slug>\S+)$', views.entrydetail, name='entry_detail'),

	###############################
	# will be decommissioning this#
	###############################
	# url(r'^programming/$', views.ProgramListView.as_view(), name='program_list'),
	# will be REPLACED by this #
	############################
	url(r'^programming/$', views.ProgramTutorialListView.as_view(), name='program_tutorial_list'),

	###############################
	# will be decommissioning this#
	###############################
	# url(r'^programming/(?P<category>\S+)/(?P<slug>\S+)$', views.ProgramDetailView.as_view(), name='program_detail'),
	# will be REPLACED by this #
	############################
	url(r'^programming/(?P<category>\S+)/(?P<slug>\S+)$', views.programTutorialDetailView, name='program_tutorial_detail'),

	##################
	# InterWebs URLs #
	##################
	url(r'^webthemes/$', views.WebTheme.as_view(), name="webthemes"),
	url(r'^webthemes/(?P<slug>\S+)$', views.WebThemeDetail.as_view(), name="webtheme_detail"),
	
	# TESTING FIELD ######################################################
	# for testing 
	# url(r'^programming/pagedream/$', views.TestProgrammingView.as_view()),
	######################################################################
	url(r'^feed/$', feed.LatestEntry(), name='feed'),

	#########################
	# testing new IndexView #
	#########################
	# try to test with entries, result: O
	# try to test with less css, result: O
	# testing stylesheet/js links, result: O
	# url(r'^testindex/$', views.TestIndexView.as_view(), name="test_index"),

	###############################
	# testing for web theme views #
	###############################
	# TEMPORARY and TEST URLs #
	# url(r'^testwebthemes$', views.TestWebThemes.as_view(), name="web_themes"),
	# url(r'^testwebthemes/testwebdetails$', views.TestWebThemeDetail.as_view(), name="web_detail")

	# url(r'^testwebthemes/(?P<theme_name>)$', views.WebThemesDetail.as_view(), name="web_theme_detail")
	# url(r'^testwebthemes/(?P<theme_name>)/livepreview)$', )
) 