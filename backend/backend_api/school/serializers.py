from rest_framework import serializers
from rest_framework.reverse import reverse
from .validators import (
    validate_location_only_nigeria,
    unique_school_location
)
from .models import School


class SchoolSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(
        view_name='school-edit',
        lookup_field='pk'
    )
    location = serializers.CharField(
        validators=[validate_location_only_nigeria, unique_school_location])
    places = serializers.CharField(source='location', read_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = School
        fields = [
            'pk',
            'edit_url',
            'url',
            "name",
            "location",
            "places",
            "founded",
            '_price',
            "discount",
            "email"
        ]

    # one way of validating perfectly if request is needed

    def validate_name(self, value):
        qs = School.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                f'This school {value} already exists')
        return value

    def create(self, validated_data):
        email = validated_data.pop("email")
        print(f"Hellow welcome to my website @ {email}")
        # this how create function returns a serializer obj
        # return School.objects.create(**validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        # no need to call the save method it auto saves
        return instance

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, School):
            return None
        return obj.get_price_discount

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('school-detail',
                       kwargs={'pk': obj.pk}, request=request)
