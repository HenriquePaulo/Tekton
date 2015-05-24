# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from product_app.product_model import Product
from routes.products import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Product)
        mommy.save_one(Product)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        product_dct = context[0]
        self.assertSetEqual(set(['id', 'creation', 'titulo', 'preco', 'descricao', 'imagem', 'nome']), set(product_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Product.query().get())
        json_response = rest.new(None, titulo='titulo_string', preco='preco_string', descricao='descricao_string', imagem='imagem_string', nome='nome_string')
        db_product = Product.query().get()
        self.assertIsNotNone(db_product)
        self.assertEquals('titulo_string', db_product.titulo)
        self.assertEquals('preco_string', db_product.preco)
        self.assertEquals('descricao_string', db_product.descricao)
        self.assertEquals('imagem_string', db_product.imagem)
        self.assertEquals('nome_string', db_product.nome)
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
        product = mommy.save_one(Product)
        old_properties = product.to_dict()
        json_response = rest.edit(None, product.key.id(), titulo='titulo_string', preco='preco_string', descricao='descricao_string', imagem='imagem_string', nome='nome_string')
        db_product = product.key.get()
        self.assertEquals('titulo_string', db_product.titulo)
        self.assertEquals('preco_string', db_product.preco)
        self.assertEquals('descricao_string', db_product.descricao)
        self.assertEquals('imagem_string', db_product.imagem)
        self.assertEquals('nome_string', db_product.nome)
        self.assertNotEqual(old_properties, db_product.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        product = mommy.save_one(Product)
        old_properties = product.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, product.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['titulo', 'preco', 'descricao', 'imagem', 'nome']), set(errors.keys()))
        self.assertEqual(old_properties, product.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        product = mommy.save_one(Product)
        rest.delete(None, product.key.id())
        self.assertIsNone(product.key.get())

    def test_non_product_deletion(self):
        non_product = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_product.key.id())
        self.assertIsNotNone(non_product.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

