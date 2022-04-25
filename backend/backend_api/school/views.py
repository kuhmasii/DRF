from rest_framework import generics
from rest_framework.response import Response
from .models import School
from api.mixins import StaffEditorPermissionMixin
from school.serializers import SchoolSerializer


class SchoolListCreateAPIView(StaffEditorPermissionMixin,
                              generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    # adding additional data
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        name = serializer.validated_data.get('name').upper()
        location = serializer.validated_data.get('location').lower()
        serializer.save(name=name, location=location)

    # can also send a django signal

# school_create_apiview = SchoolCreateAPIView.as_view()


class SchoolDetailAPIView(StaffEditorPermissionMixin,
                          generics.RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'pk'

# school_detail_apiview = SchoolDetailAPIView.as_view()


class SchoolUpdateAPIView(StaffEditorPermissionMixin,
                          generics.UpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

        instance.name = instance.name.capitalize()
        instance.save()

# school_update_apiview = SchoolUpdateAPIView.as_view()


class SchoolDeleteAPIView(StaffEditorPermissionMixin,
                          generics.DestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # do anything you wana do before deleting
        super().perform_destroy(instance)

# school_delete_apiview = SchoolDeleteAPIView.as_view()
