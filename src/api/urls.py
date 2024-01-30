from django.urls import include, path

from api.router import router

urlpatterns = [
    path('', include(router.urls)),
]