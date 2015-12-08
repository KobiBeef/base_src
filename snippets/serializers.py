from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedIdentityField(many=True, view_name='snippet-detail', read_only=True)

	class Meta:
		fields = ('id', 'snippets', 'username', )
		model = User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
	owner = serializers.ReadOnlyField(source="owner.username")

	class Meta:
		fields = ('code', 'highlight', 'language', 'linenos', 'owner', 'style', 'title', 'url', )
		model = Snippet

	def create(self, validated_data):
		# create and return a new 'Snippet' instance, given the validated data.
		return Snippet.objects.create(**validated_data)

	def update(self, instance, validated_data):
		# Update and return an existing 'Snippet' instace, given the validated data.
		instance.code = validated_data.get('code', instance.code)
		instance.language = validated_data.get('language', instance.language)
		instance.linenos = validated_data.get('linenos', instance.linenos)
		instance.style = validated_data.get('style', instance.style)
		instance.title = validated_data.get('title', instance.title)
		instance.save()
		return instance