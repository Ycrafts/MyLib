from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Category, Book, FavoriteList, Author
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView,DetailView, ListView
from django.shortcuts import get_object_or_404
from django.views.static import serve
from django.core.files.storage import default_storage
from django.http import FileResponse, HttpResponse
import os
from django.contrib.auth.decorators import login_required
from .forms import SearchForm


class BookListView(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = 'books'
    
    def get_queryset(self):
        return Book.objects.order_by('-download_count') #highest download_count first
    
    
def serve_pdf_open(request, pk):
    book = get_object_or_404(Book, pk=pk)
    pdf_file = book.pdfLink
    return FileResponse(pdf_file.open('rb'), content_type='application/pdf')

@login_required(login_url="/users/login")
def serve_pdf_download(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.download_count += 1
    book.save()
    pdf_file = book.pdfLink  # Assuming this is a FileField or similar
    pdf_data = default_storage.open(pdf_file.name, 'rb').read()
    response = HttpResponse(pdf_data, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(pdf_file.name))
    return response

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class FavoriteBookListView(LoginRequiredMixin, ListView): #favorite related
    model = FavoriteList
    template_name = "books/favorites.html"
    context_object_name = "favorites"
    login_url = 'login'

@login_required(login_url="/users/login")  
def add_to_fav(request, pk):            #favorite related
    book = get_object_or_404(Book, pk=pk)
    user = request.user
    if user.is_authenticated:
        if FavoriteList.objects.filter(user=user, book=book).exists():
            return redirect('favorites')
        else:
            fav_list = FavoriteList(user=user, book=book)
            fav_list.save()
            return redirect('home')
        return redirect('login')
    return redirect('login')

class DeleteFavoriteView(LoginRequiredMixin, DeleteView):  #favorite related
    model = FavoriteList
    template_name = 'books/delete_favorite.html'
    success_url = reverse_lazy('favorites')
    login_url = 'login'
    def get_object(self, queryset=None):
        book_pk = self.kwargs.get('pk')
        return FavoriteList.objects.get(book_id=book_pk, user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = self.get_object()
        book = context['book'].book
        context['book'] = book
        return context
    
class SearchView(ListView):
    model = Book
    form_class = SearchForm
    template_name = 'books/search_results.html'
    context_object_name = "book_search_list"
    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['q']
            queryset = queryset.filter(
                title__icontains=query) | queryset.filter(
                author__name__icontains=query) | queryset.filter(
                category__name__icontains=query) | queryset.filter(
                publicationDate__icontains=query)
                
        return queryset
    