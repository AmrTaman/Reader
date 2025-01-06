from django.urls import path
from books.views import home, BookDeleteView, BookDetailView, CreateBook, UpdateBook, CategoryCreateView, CategoryListView, CategoryDetailView, UpdateCategory
urlpatterns = [
    path('',home, name="home"),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book.details'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book.delete'),
    path('add_book/', CreateBook.as_view(), name='book.add'),
    path('edit_book/<int:pk>', UpdateBook.as_view(), name='book.edit'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category.details'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('edit_category/<int:pk>', UpdateCategory.as_view(), name='edit_category'),
]
