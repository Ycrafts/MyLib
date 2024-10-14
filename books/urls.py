from django.urls import path
from .views import BookListView
from django.views.static import serve
from .views import serve_pdf_download, serve_pdf_open, add_to_fav, BookDetailView, FavoriteBookListView, DeleteFavoriteView


urlpatterns = [
    
    path('', BookListView.as_view(), name="book_list"),
    path('<int:pk>/pdf_download/', serve_pdf_download, name='book_pdf_download'),
    path('<int:pk>/pdf_display/', serve_pdf_open, name="book_pdf_open"),
    path('<int:pk>/add_to_fav/', add_to_fav, name="add_to_fav"),
    path('favorites/<int:pk>/remove',DeleteFavoriteView.as_view(), name="remove_favorite" ),
    path('<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('favorites/', FavoriteBookListView.as_view(), name="favorites"),
]
