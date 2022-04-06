import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from school.models import School
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SchoolSerializer


def api_home(request, *args, **kwargs):

    body = request.body  # string of a json byte
    data = {}
    try:
        data = json.loads(body)  # takes a string of json -> python dict
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)


def api_home(request, *args, **kwargs):

    model_data = School.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['name', 'founded'])
    return JsonResponse(data)

# using DRF serializers and Response


@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):

    if request.method == 'GET':
        queryset = School.objects.all()
        serializers = SchoolSerializer(queryset, many=True)
        print(dir(serializers))
        return Response(serializers.data)

    if request.method == 'POST':

        serializers = SchoolSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            # instance = serializers.save()
            return Response(serializers.data)
