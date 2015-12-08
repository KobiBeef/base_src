from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models
from . import forms

# Create your views here.
########################## OVERVIEW/DASHBOARD PAGE VIEWS ##########################
class OverviewListView(generic.TemplateView):
	template_name = 'testprograms/index.html'

	def get_context_data(self, **kwargs):
		# BRUTE FORCING COUNT ON ALL THE MODEL OBJECTS
		# UGLY BUT THATS THE EASIEST SOLUTION
		# WILL THINK OF A BETTER WAY TO IMPLEMENT THIS
		context = super(OverviewListView, self).get_context_data(**kwargs)
		# MAINN OBJECTS
		context['entry_list'] = models.Entry.objects.all()
		context['entry_comment'] = models.EntryComment.objects.all()
		context['hardware_category'] = models.HardwareCategory.objects.all()
		context['hardware_item'] = models.HardwareDetail.objects.all()
		context['hardware_post'] = models.HardwarePost.objects.all()
		context['interweb_category'] = models.WebThemeCategory.objects.all()
		context['interwebs_list'] = models.WebTheme.objects.all()
		context['multimedia_category'] = models.MultiMediaCategory.objects.all()
		context['multimedia_list'] = models.MultiMediaContent.objects.all()
		context['program_language'] = models.ProgramLanguage.objects.all()
		context['program_list'] = models.ProgramTutorial.objects.all()
		
		context['tag_list_count'] = models.Tag.objects.all().count()
		return context

########################## ENTRY PAGE VIEWS ##########################
class EntryListView(generic.ListView):
	model = models.Entry
	related_name = "testuser"
	# template_name = 'testprograms/index.html'
	template_name = 'testprogram/entry_list.html'
	paginate_by = 3

	def get_context_data(self, **kwargs):
		context = super(EntryListView, self).get_context_data(**kwargs)
		context['latest_entry'] = models.Entry.objects.all()[:3]
		return context

def entryDetailView(request, category, slug):
	header = models.Entry.objects.filter(slug=slug)
	entry = models.Entry.objects.filter(slug=slug)
	comment = models.EntryComment.objects.filter(post=entry)
	entry_slug = get_object_or_404(models.Entry, slug=slug)

	if request.method == 'POST':
		form = forms.CommentForm(request.POST or None)
		if form.is_valid():
			form_comment = form.save(commit=False)
			form_comment.post = entry_slug
			form_comment.save()
			form = forms.CommentForm()
	else:
		form = forms.CommentForm()

	context = {
		'entryDetailView_header': header,
		'form': form,
		'comment_detail': comment,
		'entry_detail': entry
	}

	# return render(request, 'testprograms/post.html', context)
	return render(request, 'testprograms/entry_detail.html', context)

########################## ABOUT PAGE VIEWS ##########################
class AboutDetailView(generic.TemplateView):
	template_name = 'testprograms/about.html'

########################## PROGRAM PAGE VIEWS ##########################
class ProgramTutorialListView(generic.ListView):
	model = models.ProgramTutorial
	template_name = 'testprograms/programming_list.html'
	context_object_name = 'programtutorial_list'

def programTutorialDetailView(request, category, slug):
	header = models.ProgramTutorial.objects.filter(slug=slug)
	body = models.ProgramTutorialContent.objects.filter(program_tutorial=header)
	other_tutorials = models.ProgramTutorial.objects.all()

	context = {
		'ProgramTutorial_header': header,
		'ProgramTutorial_all': other_tutorials,
		'ProgramTutorialDetail_body': body,
	}

	return render(request, 'testprograms/programming_detail.html', context)

########################## INTERWEBS PAGE VIEWS ##########################
class WebThemeListView(generic.ListView):
	model = models.WebTheme
	template_name = 'testprograms/webtheme_list.html'
	context_object_name = 'webtheme_testprograms_list'

class WebThemeDetailView(generic.DetailView):
	model = models.WebTheme
	template_name = 'testprograms/webtheme_detail.html'

########################## MULTIMEDIA PAGE VIEWS ##########################
class MultimediaListView(generic.ListView):
	model = models.MultiMediaContent
	template_name = 'testprograms/multimedia_list.html'
	context_object_name = 'multimedia_testprograms_list'


########################## HARDWARE PAGE VIEWS ##########################
class HardwarePostListView(generic.ListView):
	model = models.HardwarePost
	related_name = "testuserhardware"
	template_name = 'testprograms/hardware_list.html'
	paginate_by = 3

	def get_context_data(self, **kwargs):
		context = super(HardwarePostListView, self).get_context_data(**kwargs)
		context['hardware_list'] = models.HardwarePost.objects.all()
		context['latest_hardware_post'] = models.HardwarePost.objects.all()[:3]
		return context

def hardwarePostDetailView(request, category, slug):
	post = models.HardwarePost.objects.filter(slug=slug)
	comment = models.HardwareComment.objects.filter(hardware_comment_post=post)
	post_slug = get_object_or_404(models.HardwarePost, slug=slug)

	if request.method == 'POST':
		form = forms.HardwareCommentForm(request.POST)
		if form.is_valid():
			form_comment = form.save(commit=False)
			form_comment.hardware_comment_post = post_slug
			form_comment.save()
			form = forms.HardwareCommentForm()
	else:
		form = forms.HardwareCommentForm()

	context = {
		'form': form,
		'comment_detail': comment,
		'entry_detail': post
	}
	return render(request, 'testprograms/hardware_detail.html', context)

########################## CONTACT VIEW ##########################
def contact(request):
	form = forms.ContactForm(request.POST or None)
	if form.is_valid():
		full_name = form.cleaned_data.get("full_name")
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		subject = 'test contact email'
		from_email = email
		to_email = [settings.EMAIL_HOST_USER]
		
		contact_message = "%s: %s via %s"%(
			full_name, 
			message,
			email)

		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				fail_silently=False)
	
	context = {
		"form": form,
	}

	return render(request, 'testprograms/contact.html', context)

########################## TEST VIEWS ##########################
# class TutorialListView(generic.ListView):
# 	template_name = 'testprograms/by_category.html'

# 	def get_queryset(self, *args, **kwargs):
# 		self.category = get_object_or_404(models.Category, name=self.kwargs['category'])
# 		return models.Entry.objects.filter(category=self.category)

# 	def get_context_data(self, **kwargs):
# 		context = super(TutorialListView, self).get_context_data(**kwargs)
# 		context['by_category'] = models.Entry.objects.filter(category=self.category)
# 		return context