# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from editar_produto_app.editar_produto_model import Editar_produto



class Editar_produtoSaveForm(ModelForm):
    """
    Form used to save and update Editar_produto
    """
    _model_class = Editar_produto
    _include = [Editar_produto.titulo, 
                Editar_produto.preco, 
                Editar_produto.descricao, 
                Editar_produto.imagem, 
                Editar_produto.nome]


class Editar_produtoForm(ModelForm):
    """
    Form used to expose Editar_produto's properties for list or json
    """
    _model_class = Editar_produto


class GetEditar_produtoCommand(NodeSearch):
    _model_class = Editar_produto


class DeleteEditar_produtoCommand(DeleteNode):
    _model_class = Editar_produto


class SaveEditar_produtoCommand(SaveCommand):
    _model_form_class = Editar_produtoSaveForm


class UpdateEditar_produtoCommand(UpdateNode):
    _model_form_class = Editar_produtoSaveForm


class ListEditar_produtoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListEditar_produtoCommand, self).__init__(Editar_produto.query_by_creation())

