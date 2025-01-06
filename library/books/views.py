from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView, ListView
from .forms import BookForm, CategoryForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views import View
from .models import Book, Category
from django.contrib import messages
from django.utils import timezone


def home(request):
    books = Book.objects.all().order_by('id')
    return render(request, 'books/index.html', {"books": books})

def is_superuser(user):
    return user.is_superuser

@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_details.html'
    context_object_name = 'book'

    

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_superuser, login_url=reverse_lazy('home')), name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('home') 


@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_superuser, login_url=reverse_lazy('home')), name='dispatch')
class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/add_book.html'

    def form_valid(self, form):
        if form.is_valid():
            book = form.save(commit=False)
            book.user = self.request.user 
            book.save()
            return redirect('home')
        
@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_superuser, login_url=reverse_lazy('home')), name='dispatch')
class UpdateBook(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/edit_book.html'
    success_url = reverse_lazy('home')
    

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'

@method_decorator(login_required, name='dispatch')
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_details.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(user_passes_test(is_superuser, login_url=reverse_lazy('home')), name='dispatch')
class UpdateCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/edit_category.html'
    success_url = reverse_lazy('category_list')

