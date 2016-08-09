form rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@api_view(['GET', 'POST'])
def snippet_list(request):
	"""
	List all code snippets, or create a new snippet.
	"""
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		data = JSONParser.parse(request)
		serializer = SnippetSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.error, status=400)



@csrf_exempt
def snippet_detail(request, pk):
	"""
	Retrieve, update or delete a code snippet.
	"""
	try:
		snippet = Snippet.objects.get(pk=pk)
	except snippet.DoesnotExist:
		return HttpResponse(status=404)
	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		return JSONResponse(serializer.data)
	if request.method == 'POST':
		data = JSONParser.parse(request)
		serializer = SnippetSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(snippet.data)
		return JSONResponse(serializer.errors, status=400)
	if request.method == 'DELETE':
		snippet.delete()
		return HttpResponse(status=204)

