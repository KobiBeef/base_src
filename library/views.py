from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import ListView, DetailView

from django.core.urlresolvers import reverse
# from forms
from django.views.generic import FormView, View
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from library.forms import TestCommentForm
from library.models import Publisher, Book, Author, Contact, TestComment

# Create your views here.
class PublisherList(ListView):
	model = Publisher
	context_object_name = 'Publisher_list'
	template_name = "library/index.html"

class PublisherBookList(ListView):
	template_name = 'library/books_by_publisher.html'

	def get_queryset(self):
		# self.publisher = get_object_or_404(Publisher, name=self.args[0])
		# FUCK YEAH e2 hinahanap ko!!!!
		self.publisher = get_object_or_404(Publisher, name=self.kwargs['name'])
		return Book.objects.filter(publisher=self.publisher)

	def get_context_data(self, **kwargs):
		context = super(PublisherBookList, self).get_context_data(**kwargs)
		context['by_publisher'] = Book.objects.filter(publisher=self.publisher)
		return context

class PublisherDetail(DetailView):
	model = Publisher
	template_name = "library/index.html"

	def get_context_data(self, **kwargs):
		context = super(PublisherDetail, self).get_context_data(**kwargs)
		context['Publisher_Detail'] = Book.objects.all()
		return context

class BookList(ListView):
	queryset = Book.objects.order_by('-publication_date')
	context_object_name = 'book_list'
	template_name = "library/index.html"

# testing multiple models on one template
class MultipleView(ListView):
	model = Publisher
	template_name = "library/index.html"

	def get_context_data(self, **kwargs):
		context = super(MultipleView, self).get_context_data(**kwargs)
		context["Publisher_list"] = Publisher.objects.all()
		context["Author_list"] = Author.objects.all()
		context["Book_list"] = Book.objects.all()
		return context

# testing form/s in class based views
class ContactDetailView(DetailView):
	model = Contact
	# template_name = 'library/contactdetail.html'

	def get_context_data(self, **kwargs):
		context = super(ContactDetailView, self).get_context_data(**kwargs)
		context['Contact_ViewDetail'] = Contact.objects.all()
		return context

class ContactListView(ListView):
	model = Contact
	template_name = 'library/contact.html'
	context_object_name = 'Contact_ListView'

# testing forms in function based views

def contact_detail_with_comments(request, pk):
	contact_pk = Contact.objects.filter(pk=pk)
	contact_fk = get_object_or_404(Contact, pk=pk)
	comment = TestComment.objects.filter(contact=contact_pk)
	form = TestCommentForm(request.POST)

	if form.is_valid():	
		test = form.save(commit=False)
		test.contact = contact_fk
		test.save()

	# problem with save. Does not save corresponding foreignkey
	# dont know how to get or set the foriegnkey of the selected object 
	# when selected the TestComment
	# but this is almost it

	# SOLUTION FOUND

	context = {
		'form': form,
		'comment': comment,
		'contact': contact_pk,
	}
	return render(request, 'library/contactdetail.html', context)
	














# FAIL ####################################################################
# class TestCommentView(FormMixin, DetailView):
# 	model = TestComment
# 	form_class = TestCommentForm

# 	def get_success_url(self):
# 		return reverse('contact_detail', kwargs={'pk': self.object.pk})

# 	def get_context_data(self, **kwargs):
# 		context = super(TestCommentView, self).get_context_data(**kwargs)
# 		context['form'] = self.get_form()

# 	def post(self, request, *args, **kwargs):
# 		self.object = self.get_object()
# 		form = self.get_form
# 		if form.is_valid():
# 			form.save()
# 		return self.form_valid(form)

# Somewhat fail ###############################################################
# class ContactFormViewTest(FormMixin, DetailView):
# 	model = Contact
# 	form_class = ContactForm
# 	template_name = 'library/contact.html'

# 	def post(self, request, *args, **kwargs):
# 		form = self.form_class(request.POST)
# 		# self.object = self.get_object()
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/library/contact/')
# 		return render(request, self.template_name, {'form': form})
	
# 	def get_context_data(self, **kwargs):
# 		context = super(ContactFormViewTest, self).get_context_data(**kwargs)
# 		context['form'] = self.get_form()
# 		return contex

# for post
# def post(self, request, *args, **kwargs):
# 		form = self.form_class(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/library/contact/')
# 		return render(request, self.template_name, {'form': form})