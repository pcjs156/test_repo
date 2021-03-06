# /artist url 관리

from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_main, name="artist_main"),
    path('new', views.new_artist, name="new_artist"),
    path('edit/<int:artist_id>', views.artist_edit, name="artist_edit"),
    path('delete/<int:artist_id>/confirm', views.artist_delete_confirm, name="artist_delete_confirm"),
    path('delete/<int:artist_id>', views.artist_delete, name="artist_delete"),
    path('interest_up/<int:artist_id>', views.interest_up, name="interest_up"),
]