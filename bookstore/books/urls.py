from django.urls import path
from books.views import IndexView, BookView

urlpatterns = [
    path('', IndexView.as_view(template_name="index.html")),
    path('/<str:isbn13>', BookView.as_view(template_name="books.html"))
]   