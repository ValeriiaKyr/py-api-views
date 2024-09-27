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
    path("actor/", ActorList.as_view(), name="actor-list"),
    path("actor/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genre/", GenreList.as_view(), name="actor-list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="actor-detail"),
    path(
        "cinema_hall/",
        CinemaHallViewSet.as_view(
            {
                "get": "list", "post": "create"
            }
        ),
        name="cinema_hall-list"
    ),
    path(
        "cinema_hall/<int:pk>/",
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
