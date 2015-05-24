# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from editar_produto_app.editar_produto_model import Editar_produto
from routes.editar_produtos import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Editar_produto)
        mommy.save_one(Editar_produto)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        editar_produto_dct = context[0]
        self.assertSetEqual(set(['id', 'creation', 'titulo', 'preco', 'descricao', 'imagem', 'nome']), set(editar_produto_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Editar_produto.query().get())
        json_response = rest.new(None, titulo='titulo_string', preco='preco_string', descricao='descricao_string', imagem='imagem_string', nome='nome_string')
        db_editar_produto = Editar_produto.query().get()
        self.assertIsNotNone(db_editar_produto)
        self.assertEquals('titulo_string', db_editar_produto.titulo)
        self.assertEquals('preco_string', db_editar_produto.preco)
        self.assertEquals('descricao_string', db_editar_produto.descricao)
        self.assertEquals('imagem_string', db_editar_produto.imagem)
        self.assertEquals('nome_string', db_editar_produto.nome)
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        resp = Mock()
        json_response = rest.new(resp)
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['titulo', 'preco', 'descricao', 'imagem', 'nome']), set(errors.keys()))
        self.assert_can_serialize_as_json(json_response)


class EditTests(GAETestCase):
    def test_success(self):
        editar_produto = mommy.save_one(Editar_produto)
        old_properties = editar_produto.to_dict()
        json_response = rest.edit(None, editar_produto.key.id(), titulo='titulo_string', preco='preco_string', descricao='descricao_string', imagem='imagem_string', nome='nome_string')
        db_editar_produto = editar_produto.key.get()
        self.assertEquals('titulo_string', db_editar_produto.titulo)
        self.assertEquals('preco_string', db_editar_produto.preco)
        self.assertEquals('descricao_string', db_editar_produto.descricao)
        self.assertEquals('imagem_string', db_editar_produto.imagem)
        self.assertEquals('nome_string', db_editar_produto.nome)
        self.assertNotEqual(old_properties, db_editar_produto.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        editar_produto = mommy.save_one(Editar_produto)
        old_properties = editar_produto.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, editar_produto.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['titulo', 'preco', 'descricao', 'imagem', 'nome']), set(errors.keys()))
        self.assertEqual(old_properties, editar_produto.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        editar_produto = mommy.save_one(Editar_produto)
        rest.delete(None, editar_produto.key.id())
        self.assertIsNone(editar_produto.key.get())

    def test_non_editar_produto_deletion(self):
        non_editar_produto = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_editar_produto.key.id())
        self.assertIsNotNone(non_editar_produto.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

