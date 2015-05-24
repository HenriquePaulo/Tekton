# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from product_app.product_model import Product



class ProductSaveForm(ModelForm):
    """
    Form used to save and update Product
    """
    _model_class = Product
    _include = [Product.titulo, 
                Product.preco, 
                Product.descricao, 
                Product.imagem, 
                Product.nome]


class ProductForm(ModelForm):
    """
    Form used to expose Product's properties for list or json
    """
    _model_class = Product


class GetProductCommand(NodeSearch):
    _model_class = Product


class DeleteProductCommand(DeleteNode):
    _model_class = Product


class SaveProductCommand(SaveCommand):
    _model_form_class = ProductSaveForm


class UpdateProductCommand(UpdateNode):
    _model_form_class = ProductSaveForm


class ListProductCommand(ModelSearchCommand):
    def __init__(self):
        super(ListProductCommand, self).__init__(Product.query_by_creation())

