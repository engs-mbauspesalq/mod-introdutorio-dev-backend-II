from rest_framework import serializers
from restaurantes.models import Restaurante, Prato
from django.contrib.auth.models import User

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'

class PratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prato
        fields = '__all__'


class ListaPratosDeUmRestauranteSerializer(serializers.ModelSerializer):
    restaurante_nome = serializers.ReadOnlyField(source='restaurantes.nome')
    class Meta:
        model = Prato
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, user, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            user.set_password(password)
        for field, value in validated_data.items():
            setattr(user, field, value)
        user.save()
        return user