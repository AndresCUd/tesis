from __future__ import unicode_literals
import django_tables2 as tables
from django_tables2.utils import A
from .models import lista


class lista(tables.Table)
    archivo =tables.LinkColumn(args=[A('pk')])
    tamano = tables.Column(orderable=True,accessor='tamano')
    nombre =tables.Column(orderable=True,accessor='nombre')