from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'data_criacao', 'data_modificacao')
    search_fields = ('nome', 'descricao')
    list_filter = ('data_criacao', 'data_modificacao')
