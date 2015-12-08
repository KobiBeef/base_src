from django import forms
from django.utils.translation import ugettext_lazy as _
from . import models

class CommentForm(forms.ModelForm):
	class Meta:
		model = models.EntryComment
		fields = ('name', 'email', 'body' )
		error_messages = {
			'name': {'required': _('This Field is required')},
			'email': {'required': _('This Field is required')},
			'body': {'required': _('This Field is required')}
		}

		labels = {
			'name': _('Name:'), 
			'email': _('Email:'),
			'body': _('Message:'),
		}


class HardwareCommentForm(forms.ModelForm):
	class Meta:
		model = models.HardwareComment
		fields = ('name', 'email', 'body',)
		error_messages = {
			'name': {'required': _('This field is requred')},
			'email': {'required': _('This Field is required')},
			'body': {'required': _('This Field is required')}
		}

		labels = {
			'name': _('Name:'), 
			'email': _('Email:'),
			'body': _('Message:'),
		}

class ContactForm(forms.Form):
	full_name = forms.CharField(max_length=100)
	email = forms.EmailField()
	message = forms.CharField(max_length=1000)