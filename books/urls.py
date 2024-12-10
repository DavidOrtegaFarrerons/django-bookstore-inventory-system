from django.urls import path

from books import views

app_name = "books"

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:book_id>/", views.detail, name="detail")
]
