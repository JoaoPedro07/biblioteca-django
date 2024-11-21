from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Colecao, Livro, Autor, Categoria
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from . import views
# Create your tests here.
        
class ColecaoDetailTests(APITestCase):
    def create_user_and_set_token_credentials(self):
        self.user1 = User.objects.create_user("user01", "user01@example.com", "user01P4ssw0rD")
        self.client.force_authenticate(self.user1)

    
    def create_second_user_and_set_token_credentials(self):
        self.user2 = User.objects.create_user("user02", "user02@example.com", "user02P4ssw0rD")
        self.client.force_authenticate(self.user2)
        
    def setUp(self):
        autor = Autor.objects.create(nome="Carl Sagan")
        categoria = Categoria.objects.create(nome="Ficcção Científica")
        livro = Livro.objects.create(
            titulo="Fundação - Edição Revisada",
            autor= autor,
            categoria= categoria,
            publicado_em= "1951-06-01"
        )
    
    def test_create_colecao(self):
        self.create_user_and_set_token_credentials()
        url = reverse("colecao-list")
        data = {"nome":"colecao", 
                "descricao":"colecao de teste", 
                "livros":["Fundação - Edição Revisada"], 
                "colecionador":"1"}
        response = self.client.post(url, data, format="json")
        assert str(Colecao.objects.all().first().owner) == self.user1.username




    def test_permissions_colecao(self):
        self.create_user_and_set_token_credentials()
        url = reverse("colecao-list")
        url2 = reverse(views.ColecaoDetail.name, None, {1})
        data = {"nome":"colecao", 
                "descricao":"colecao de teste", 
                "livros":["Fundação - Edição Revisada"], 
                "colecionador":"1", }
        response = self.client.post(url, data, format="json")
        response2 = self.client.patch(url2, data, format="json")


        self.create_second_user_and_set_token_credentials()
        data = {"nome":"colecao2" }
        response3 = self.client.patch(url2, data, format="json")
        
        assert response.status_code == status.HTTP_201_CREATED
        assert response2.status_code == status.HTTP_200_OK
        assert response3.status_code == status.HTTP_403_FORBIDDEN
        
    def test_get_colecao(self):
        self.create_user_and_set_token_credentials()
        url = reverse("colecao-list")
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK