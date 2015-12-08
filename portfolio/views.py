from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from . import models
from . import forms

########################
# decommissioning this #
########################
# class IndexView(generic.ListView):
# 	template_name = 'portfolio/index.html'
# 	paginate_by = 3
#
# 	def get_queryset(self):
# 		return models.Entry.objects.filter(publish=True)
# replaced by this #
####################
class IndexView(generic.ListView):
	template_name = 'portfolio/new_index.html'
	paginate_by = 3

	def get_queryset(self):
		return models.Entry.objects.filter(publish=True)

# will edit the entry detail to accomodate the comments
def entrydetail(request, category, slug):
	entry = models.Entry.objects.filter(slug=slug)
	comment = models.Comment.objects.filter(entry_post=entry)
	entry_slug = get_object_or_404(models.Entry, slug=slug)

	if request.method == 'POST':
		form = forms.CommentForm(request.POST or None)
		if form.is_valid():
			form_comment = form.save(commit=False)
			form_comment.entry_post = entry_slug
			form_comment.save()
			form = forms.CommentForm()
	else:
		form = forms.CommentForm()

	context = {
		'form': form,
		'comment_detail': comment,
		'entry_detail': entry
	}
	return render(request, 'portfolio/post.html', context)

###############################
# will be decommissioning this#
###############################
# class ProgramListView(generic.ListView):
# 	model = models.Entry
# 	template_name = 'portfolio/program_list.html'
# 	context_object_name = 'Entry_list'
# replaced by this #
####################
class ProgramTutorialListView(generic.ListView):
	model = models.ProgramTutorial
	template_name = 'portfolio/program_tutorial_list.html'
	context_object_name = 'ProgramTutorial_list'

###############################
# will be decommissioning this#
###############################
# class ProgramDetailView(generic.DetailView):
# 	model = models.Entry
# 	template_name = 'portfolio/program_detail.html'
# replaced by this #
####################
def programTutorialDetailView(request, category, slug):
	header = models.ProgramTutorial.objects.filter(slug=slug)
	body = models.ProgramTutorialDetail.objects.filter(tutorial_name=header)

	context = {
		'ProgramTutorial_header': header,
		'ProgramTutorialDetail_body': body,
	}

	return render(request, 'portfolio/program_tutorial_detail.html', context)

# WebThemes Alpha
class WebTheme(generic.ListView):
	model = models.WebTheme
	template_name = 'portfolio/webtheme_list.html'
	context_object_name = 'webtheme_list'

class WebThemeDetail(generic.DetailView):
	model = models.WebTheme
	template_name = 'portfolio/webtheme_detail.html'

# class MultimediaView(TemplateView):
# 	pass

# class HardwareView(TemplateView):
# 	pass

# class ContactView(TemplateView):
# 	pass

# TESTING FIELD and EMPORARY VIEWS ################################################
# class TestProgrammingView(TemplateView):
# 	template_name = 'portfolio/programs.html'

class AboutView(TemplateView):
	template_name = 'portfolio/about.html'

#################################################################
# creating test views for webtheme list, detail and livepreview #
#################################################################
# class TestWebThemes(TemplateView):
# 	template_name = 'portfolio/webtheme_list.html'

# class TestWebThemeDetail(TemplateView):
# 	template_name = 'portfolio/webtheme_detail.html'

# class TestWebThemePreview(TemplateView):
	# pass