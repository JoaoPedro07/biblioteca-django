from rest_framework import generics, permissions
from .models import Livro, Autor, Categoria, Colecao
from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer, ColecaoSerializer
from .filters import LivroFilter, AutorFilter, CategoriaFilter
from core import custom_permissions
from rest_framework.authentication import TokenAuthentication

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

class ColecaoList(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    name = 'colecao-list'
    ordering_fields = ['nome']
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsCurrentUserOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

    

class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    name = 'colecao-detail'
    serializer_class = ColecaoSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsCurrentUserOwnerOrReadOnly,
    )

