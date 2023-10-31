from django.db import models
from django.db.models.deletion import CASCADE

class Restaurante(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Prato(models.Model):
    TAGS = (
        ('Doces', 'Doces'),
        ('Caldos', 'Caldos'),
        ('Americana', 'Americana'),
        ('Baiana', 'Baiana'),
        ('Coreana', 'Coreana'),
        ('Espanhola','Espanhola' ),
        ('Francesa', 'Francesa'),
        ('Italiana', 'Italiana'),
        ('Japonesa', 'Japonesa'),
        ('Mexicana', 'Mexicana'),
        ('Mineira', 'Mineira'),
        ('Vegetariana', 'Vegetariana'),
        ('Massas', 'Massas'),
        ('Molhos', 'Molhos'),
        ('Salada','Salada' ),
        ('Light','Light' ),
    )
    nome = models.CharField(max_length=50)
    tag = models.CharField(max_length=15, choices=TAGS, blank=False, null=False, default='Doces')
    imagem = models.ImageField(blank=True)
    descricao = models.TextField(max_length=500)
    restaurante = models.ForeignKey(Restaurante, on_delete=CASCADE)

    def __str__(self):
        return self.nome