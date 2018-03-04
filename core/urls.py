from django.conf.urls import url
from jsonview.decorators import json_view

from core.views import ProjectRequestCreate

urlpatterns = [
    url(r'^projectRequest.create$', json_view(ProjectRequestCreate.as_view())),
]