from django import forms
from django.utils.translation import ugettext_lazy as _
from . import models

# put forms class here

class CommentForm(forms.ModelForm):
	class Meta:
		model = models.Comment
		fields = ('name', 'body',)
		error_messages = {
			'name': {'required': _('This Field is required')},
			'body': {'required': _('This Field is required')} 
		}

		labels = {
			'name': _('Name:'), 
			'body': _('Message:')
		}
		
		# help_texts = {
  #           'name': _('Some useful help text.'),
  #       }
