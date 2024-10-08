from rest_framework import generics
from .models import Livro, Autor, Categoria
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer
from .filters import LivroFilter, AutorFilter, CategoriaFilter

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    name = 'livros-list'
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    name = 'livro-detail'
    serializer_class = LivroSerializer

    
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filterset_class = AutorFilter
    name = 'autor-list'
    ordering_fields = ['nome']

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    name = 'Autor-detail'
    serializer_class = AutorSerializer


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = 'categoria-list'
    filterset_class = CategoriaFilter
    ordering_fields = ['nome']
    

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    name = 'categoria-detail'
    serializer_class = CategoriaSerializer
