from django.forms import ModelForm
from django import forms
from . import models

class TestCommentForm(forms.ModelForm):
	class Meta:
		model = models.TestComment
		fields = ['name', 'message']