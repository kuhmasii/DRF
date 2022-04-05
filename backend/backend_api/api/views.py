import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from school.models import School
# def api_home(request, *args, **kwargs):

# 	body = request.body # string of a json byte
# 	data = {}
# 	try:
# 		data = json.loads(body) # takes a string of json -> python dict
# 	except:
# 		pass
# 	data['params'] = dict(request.GET)
# 	data['headers'] = dict(request.headers)
# 	data['content_type'] = request.content_type
# 	return JsonResponse(data)

def api_home(request, *args, **kwargs):

	model_data = School.objects.all().order_by("?").first()
	data = {}
	if model_data:
		data = model_to_dict(model_data, fields=['name', 'founded'])
	return JsonResponse(data)