from django.urls import path
from .views import KeyWordsAPIView, VideoDataAPIView


app_name = "web_app"


urlpatterns = [
    path('words', KeyWordsAPIView.as_view()),
    path('words/<int:pk>', KeyWordsAPIView.as_view()),
    path('words/<int:pk>/video', VideoDataAPIView.as_view()),
]
