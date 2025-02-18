"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from strawberry.django.views import AsyncGraphQLView, GraphQLView

from . import async_schema, schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path("arg_schema", csrf_exempt(GraphQLView.as_view(schema=schema.arg_schema))),
    path("relay_schema", csrf_exempt(GraphQLView.as_view(schema=schema.relay_schema))),
    path("async_arg_schema", csrf_exempt(AsyncGraphQLView.as_view(schema=async_schema.arg_schema))),
    path(
        "async_relay_schema",
        csrf_exempt(AsyncGraphQLView.as_view(schema=async_schema.relay_schema)),
    ),
]
