# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from Product_app.Product_model import product



class productSaveForm(ModelForm):
    """
    Form used to save and update product
    """
    _model_class = product
    _include = [product.titulo, 
                product.preco, 
                product.descricao, 
                product.imagem, 
                product.nome]


class productForm(ModelForm):
    """
    Form used to expose product's properties for list or json
    """
    _model_class = product


class GetproductCommand(NodeSearch):
    _model_class = product


class DeleteproductCommand(DeleteNode):
    _model_class = product


class SaveproductCommand(SaveCommand):
    _model_form_class = productSaveForm


class UpdateproductCommand(UpdateNode):
    _model_form_class = productSaveForm


class ListproductCommand(ModelSearchCommand):
    def __init__(self):
        super(ListproductCommand, self).__init__(product.query_by_creation())

