from schema_graph.views import Schema

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("schema/", Schema.as_view()),
]
