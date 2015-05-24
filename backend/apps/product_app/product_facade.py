# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from product_app.product_commands import ListProductCommand, SaveProductCommand, UpdateProductCommand, ProductForm,\
    GetProductCommand, DeleteProductCommand


def save_product_cmd(**product_properties):
    """
    Command to save Product entity
    :param product_properties: a dict of properties to save on model
    :return: a Command that save Product, validating and localizing properties received as strings
    """
    return SaveProductCommand(**product_properties)


def update_product_cmd(product_id, **product_properties):
    """
    Command to update Product entity with id equals 'product_id'
    :param product_properties: a dict of properties to update model
    :return: a Command that update Product, validating and localizing properties received as strings
    """
    return UpdateProductCommand(product_id, **product_properties)


def list_products_cmd():
    """
    Command to list Product entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListProductCommand()


def product_form(**kwargs):
    """
    Function to get Product's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ProductForm(**kwargs)


def get_product_cmd(product_id):
    """
    Find product by her id
    :param product_id: the product id
    :return: Command
    """
    return GetProductCommand(product_id)



def delete_product_cmd(product_id):
    """
    Construct a command to delete a Product
    :param product_id: product's id
    :return: Command
    """
    return DeleteProductCommand(product_id)

