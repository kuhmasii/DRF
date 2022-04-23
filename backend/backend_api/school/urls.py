from django.urls import path
from . import views

urlpatterns= [
	path("", views.SchoolListCreateAPIView.as_view()),
	path("<int:pk>/update/", views.SchoolUpdateAPIView.as_view()),
	path("<int:pk>/delete/", views.SchoolDeleteAPIView.as_view()),
	path("<int:pk>/", views.SchoolDetailAPIView.as_view()),
]
