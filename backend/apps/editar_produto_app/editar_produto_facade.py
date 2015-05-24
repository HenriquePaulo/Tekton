# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from editar_produto_app.editar_produto_commands import ListEditar_produtoCommand, SaveEditar_produtoCommand, UpdateEditar_produtoCommand, Editar_produtoForm,\
    GetEditar_produtoCommand, DeleteEditar_produtoCommand


def save_editar_produto_cmd(**editar_produto_properties):
    """
    Command to save Editar_produto entity
    :param editar_produto_properties: a dict of properties to save on model
    :return: a Command that save Editar_produto, validating and localizing properties received as strings
    """
    return SaveEditar_produtoCommand(**editar_produto_properties)


def update_editar_produto_cmd(editar_produto_id, **editar_produto_properties):
    """
    Command to update Editar_produto entity with id equals 'editar_produto_id'
    :param editar_produto_properties: a dict of properties to update model
    :return: a Command that update Editar_produto, validating and localizing properties received as strings
    """
    return UpdateEditar_produtoCommand(editar_produto_id, **editar_produto_properties)


def list_editar_produtos_cmd():
    """
    Command to list Editar_produto entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListEditar_produtoCommand()


def editar_produto_form(**kwargs):
    """
    Function to get Editar_produto's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return Editar_produtoForm(**kwargs)


def get_editar_produto_cmd(editar_produto_id):
    """
    Find editar_produto by her id
    :param editar_produto_id: the editar_produto id
    :return: Command
    """
    return GetEditar_produtoCommand(editar_produto_id)



def delete_editar_produto_cmd(editar_produto_id):
    """
    Construct a command to delete a Editar_produto
    :param editar_produto_id: editar_produto's id
    :return: Command
    """
    return DeleteEditar_produtoCommand(editar_produto_id)

