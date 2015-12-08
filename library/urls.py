from django.conf.urls import patterns, url, include
from library import views
from library.views import PublisherList, PublisherDetail, BookList, PublisherBookList 
from library.views import MultipleView, ContactListView, ContactDetailView, contact_detail_with_comments

urlpatterns = patterns(
	'',
	url(r'^books/(?P<name>\S+)$', PublisherBookList.as_view(), name='booklist'),
	# Multiple object views #############################################################
	url(r'^all/$', MultipleView.as_view(), name='multiple_view'),
	url(r'^publishers/$', PublisherList.as_view()),
	url(r'^publishers/$', BookList.as_view()),
	url(r'^publishers/(?P<pk>\d+)$', PublisherDetail.as_view()),
	# testing forms class based views ###################################################
	url(r'^contact/$', ContactListView.as_view(), name='contact_list'),
	# testing forms function based views ################################################
	url(r'^contact/(?P<pk>\d+)$', views.contact_detail_with_comments, name="contact_detail_with_comments"),
)