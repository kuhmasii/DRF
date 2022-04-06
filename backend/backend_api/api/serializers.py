from rest_framework import serializers
from school.models import School


class SchoolSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = School
        fields = [
            "name",
            "location",
            "founded",
            "discount",
        ]

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, School):
            return None
        return obj.get_price_discount
