from django.urls import include, path
from .views import (
    UcGradesToGpaView,
    TestView,
)


urlpatterns = [
    path('transform/', UcGradesToGpaView.as_view()),
    path('test/', TestView.as_view()),
]