# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Editar_produto(Node):
    nome = ndb.StringProperty(required=True)
    titulo = ndb.StringProperty(required=True)
    descricao = ndb.StringProperty(required=True)
    imagem = ndb.StringProperty(required=True)
    preco = ndb.StringProperty(required=True)

