# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from Product_app.Product_commands import ListproductCommand, SaveproductCommand, UpdateproductCommand, productForm,\
    GetproductCommand, DeleteproductCommand


def save_product_cmd(**product_properties):
    """
    Command to save product entity
    :param product_properties: a dict of properties to save on model
    :return: a Command that save product, validating and localizing properties received as strings
    """
    return SaveproductCommand(**product_properties)


def update_product_cmd(product_id, **product_properties):
    """
    Command to update product entity with id equals 'product_id'
    :param product_properties: a dict of properties to update model
    :return: a Command that update product, validating and localizing properties received as strings
    """
    return UpdateproductCommand(product_id, **product_properties)


def list_products_cmd():
    """
    Command to list product entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListproductCommand()


def product_form(**kwargs):
    """
    Function to get product's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return productForm(**kwargs)


def get_product_cmd(product_id):
    """
    Find product by her id
    :param product_id: the product id
    :return: Command
    """
    return GetproductCommand(product_id)



def delete_product_cmd(product_id):
    """
    Construct a command to delete a product
    :param product_id: product's id
    :return: Command
    """
    return DeleteproductCommand(product_id)

