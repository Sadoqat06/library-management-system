from django.urls import path
from .views import BookOrderModelGetView,BookOrderModelCreateView

urlpatterns= [
    path("get/",BookOrderModelGetView.as_view()), 
    path('create/',BookOrderModelCreateView.as_view()),
    path("get/<int:pk>/",BookOrderModelGetView.as_view()), 
]