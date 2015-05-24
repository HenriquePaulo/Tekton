# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from product_app.product_model import Product
from routes.products.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Product.query().get())
        redirect_response = save(titulo='titulo_string', preco='preco_string', descricao='descricao_string', imagem='imagem_string', nome='nome_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_product = Product.query().get()
        self.assertIsNotNone(saved_product)
        self.assertEquals('titulo_string', saved_product.titulo)
        self.assertEquals('preco_string', saved_product.preco)
        self.assertEquals('descricao_string', saved_product.descricao)
        self.assertEquals('imagem_string', saved_product.imagem)
        self.assertEquals('nome_string', saved_product.nome)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['titulo', 'preco', 'descricao', 'imagem', 'nome']), set(errors.keys()))
        self.assert_can_render(template_response)
