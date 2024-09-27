from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorList,
    ActorDetail,
    GenreDetail,
    GenreList,
    CinemaHallViewSet
)
from .views import MovieViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="actor-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="actor-detail"),
    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view(
            {
                "get": "list", "post": "create"
            }
        ),
        name="cinema_hall-list"
    ),
    path(
        "cinema_halls/<int:pk>/",
        CinemaHallViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ), name="cinema_hall-detail"
    ),
]

app_name = "cinema"
