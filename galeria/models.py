from django.db import models

class Fotografia(models.Model):
    OPCOES_CATEGORIA = [
        ("Nebulosa", "Nebulosa"),
        ("Estrela", "Estrela"),
        ("Galáxia", "Galáxia"),
        ("Planeta", "Planeta")
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=150, null=False, blank=False)
    publicada = models.BooleanField(default=False)#publicação das fotos

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
    
