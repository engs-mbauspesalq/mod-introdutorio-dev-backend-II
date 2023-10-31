from django.http.response import JsonResponse
from drf_yasg.openapi import Response
from rest_framework import generics, viewsets, filters
from rest_framework.views import APIView
from restaurantes.models import Restaurante, Prato
from restaurantes.serializers import RestauranteSerializer, PratoSerializer, ListaPratosDeUmRestauranteSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class=None

class RestauranteViewSet(viewsets.ModelViewSet):
    """Recurso de restaurantes"""
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']
    pagination_class=None

class PratoViewSet(viewsets.ModelViewSet):
    """Recurso de pratos de um restaurante"""
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    filterset_fields = ['tag']
    pagination_class=None

class ListaPratosDeUmRestauranteView(generics.ListAPIView):
    """Listando pratos de um restaurante"""
    def get_queryset(self):
        queryset = Prato.objects.filter(restaurante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPratosDeUmRestauranteSerializer
    pagination_class=None

class ListaRestaurantesView(generics.ListAPIView):
    """Listando restaurante"""
    def get_queryset(self):
        queryset = Restaurante.objects.all()
        return queryset
    serializer_class = RestauranteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome']

class ListaPratosView(generics.ListAPIView):
    """Listando restaurante"""
    def get_queryset(self):
        queryset = Prato.objects.all()
        return queryset
    serializer_class = PratoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    filterset_fields = ['tag']


class ListandoTagsView(APIView):
    def get(self, request):
        tags = {
        "tags": [
            {
            "value": "Italiana",
            "id": 1
            },
            {
            "value": "Japonesa",
            "id": 2
            },
            {
            "value": "Doces",
            "id": 3
            },
            {
            "value": "Diet",
            "id": 4
            },
            {
            "value": "Massas",
            "id": 5
            },
            {
            "value": "Caldos",
            "id": 6
            },
            {
            "value": "Light",
            "id": 7
            },
            {
            "value": "Vegetariana",
            "id": 8
            },
            {
            "value": "Mexicana",
            "id": 9
            },
            {
            "value": "Francesa",
            "id": 10
            },
            {
            "value": "Espanhola",
            "id": 11
            },
            {
            "value": "Mineira",
            "id": 12
            },
            {
            "value": "Baiana",
            "id": 13
            },
            {
            "value": "Molhos",
            "id": 14
            },
            {
            "value": "Saladas",
            "id": 15
            },
            {
            "value": "Americana",
            "id": 16
            }
        ]
        }
        return JsonResponse(tags, status=status.HTTP_200_OK)