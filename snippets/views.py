from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view, detail_route, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer

# Create your views here.
#######################################
# FROM Viewsets and Routers           #
#######################################
class UserViewSet(viewsets.ReadOnlyModelViewSet):
	# This viewset automatically provides 'list' and 'detail' actions.
	queryset = User.objects.all()
	serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
	# This viewset automatically provides 'list', 'create', 'retrive', 'update', and 'destroy' actions
	# Additionally we also provide an extra 'highlight' action.

	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

#######################################
# FROM HYPERLINKED APIS               #
#######################################
@api_view(('GET',))
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'snippets': reverse('snippet-list', request=request, format=format)
	})

# class SnippetHighlight(generics.GenericAPIView):
# 	queryset = Snippet.objects.all()
# 	renderer_classes = (renderers.StaticHTMLRenderer,)

# 	def get(self, request, *args, **kwargs):
# 		snippet = self.get_object()
# 		return Response(snippet.highlighted)

#######################################
# FROM AUTHENTICATION                 #
#######################################
# class UserList(generics.ListAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
	
#######################################
# FROM ClASS BASED VIEWS              #
#######################################
# class SnippetList(generics.ListCreateAPIView):
# 	# List all snippets, or create a new snippet
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

# 	def perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	# Retrieve, update or delete a snippet instance.
	# queryset = Snippet.objects.all()
	# serializer_class = SnippetSerializer
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

# TEST FOR GENERIC VIEWS
class SnippetListView(generic.ListView):
	model = Snippet
	template_name = "snippets/test.html"
	context_objet_name = "snippet_list"

#######################################
# FROM REQUEST AND RESPONSE           #
#######################################
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
	# List all code snippets, or create a new snippet
	# if request.method == 'GET':
	# 	snippets = Snippet.objects.all()
	# 	serializer = SnippetSerializer(snippets, many=True)
	# 	return Response(serializer.data)
		
	# elif request.method == 'POST':
	# 	serializer = SnippetSerializer(data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
	# Retrive , update or delete a code snippet.
	# try:
	# 	snippet = Snippet.objects.get(pk=pk)
	# except Snippet.DoesNotExist:
	# 	return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	# if request.method == 'GET':
	# 	serializer = SnippetSerializer(snippet)
	# 	return Response(serializer.data)
	
	# elif request.method == 'PUT':
	# 	serializer = SnippetSerializer(snippet, data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data)
	# 	return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# elif request.method == 'DELETE':
	# 	snippet.delete()
	# 	return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#######################################
# FROM SERIALIZERS                    #
#######################################
# class JSONResponse(HttpResponse):
	# An HttpResponse that renders its contents into JSON
	# def __init__(self, data, **kwargs):
	# 	content = JSONRenderer().render(data)
	# 	kwargs['content_type'] = 'application/json'
	# 	super(JSONResponse, self).__init__(content, **kwargs)

# @csrf_exempt
# def snippet_list(request):
	# List all code snippets, or create a new snippet
	# if request.method == 'GET':
	# 	snippets = Snippet.objects.all()
	# 	serializer = SnippetSerializer(snippets, many=True)
	# 	return JSONResponse(serializer.data)
		
	# elif request.method == 'POST':
	# 	data = JSONParser().parse(request)
	# 	serializer = SnippetSerializer(data=data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return JSONResponse(serializer.data, status=201)
	# 	return JSONResponse(serializer.errors, status=400)

# @csrf_exempt
# def snippet_detail(request, pk):
	# Retrive , update or delete a code snippet.
	# try:
	# 	snippet = Snippet.objects.get(pk=pk)
	# except Snippet.DoesNotExist:
	# 	return HttpResponse(status=404)

	# if request.method == 'GET':
	# 	serializer = SnippetSerializer(snippet)
	# 	return JSONResponse(serializer.data)
	
	# elif request.method == 'POST':
	# 	data = JSONParser().parse(request)
	# 	serializer = SnippetSerializer(snippet, data=data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return JSONResponse(serializer.data)
	# 	return  JSONResponse(serializer.errors, status=400)

	# elif request.method == 'DELETE':
	# 	snippet.delete()
	# 	return HttpResponse(status=404)
