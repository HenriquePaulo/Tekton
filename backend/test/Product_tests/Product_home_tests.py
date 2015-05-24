# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from Product_app.Product_model import product
from routes.Products.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(product)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        product = mommy.save_one(product)
        redirect_response = delete(product.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(product.key.get())

    def test_non_product_deletion(self):
        non_product = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_product.key.id())
        self.assertIsNotNone(non_product.key.get())

