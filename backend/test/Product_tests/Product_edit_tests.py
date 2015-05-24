# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from Product_app.Product_model import product
from routes.Products.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        product = mommy.save_one(product)
        template_response = index(product.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        product = mommy.save_one(product)
        old_properties = product.to_dict()
        redirect_response = save(product.key.id(), titulo='titulo_string', preco='preco_string', descricao='descricao_string', imagem='imagem_string', nome='nome_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_product = product.key.get()
        self.assertEquals('titulo_string', edited_product.titulo)
        self.assertEquals('preco_string', edited_product.preco)
        self.assertEquals('descricao_string', edited_product.descricao)
        self.assertEquals('imagem_string', edited_product.imagem)
        self.assertEquals('nome_string', edited_product.nome)
        self.assertNotEqual(old_properties, edited_product.to_dict())

    def test_error(self):
        product = mommy.save_one(product)
        old_properties = product.to_dict()
        template_response = save(product.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['titulo', 'preco', 'descricao', 'imagem', 'nome']), set(errors.keys()))
        self.assertEqual(old_properties, product.key.get().to_dict())
        self.assert_can_render(template_response)
