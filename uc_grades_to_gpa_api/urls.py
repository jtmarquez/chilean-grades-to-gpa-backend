from django.urls import include, path
from .views import (
    UcGradesToGpaView
)


urlpatterns = [
    path('transform/', UcGradesToGpaView.as_view()),
]