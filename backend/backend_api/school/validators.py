from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import School



def validate_location_only_nigeria(value):
	states = "OYO-STATE OGUN-STATE ANAMBRA-STATE LAGOS-STATE OSUN-STATE EKITI-STATE EDO-STATE DELTA-STATE BORNO-STATE KANO-STATE \
	SOKOTO-STATE ABIA-STATE IMO-STATE".split()

	if value.upper() not in states:
		raise serializers.ValidationError(f"{value} is not a state in Nigeria!")


unique_school_location = UniqueValidator(queryset=School.objects.all())
