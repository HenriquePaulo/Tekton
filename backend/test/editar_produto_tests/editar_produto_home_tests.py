# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from editar_produto_app.editar_produto_model import Editar_produto
from routes.editar_produtos.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Editar_produto)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        editar_produto = mommy.save_one(Editar_produto)
        redirect_response = delete(editar_produto.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(editar_produto.key.get())

    def test_non_editar_produto_deletion(self):
        non_editar_produto = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_editar_produto.key.id())
        self.assertIsNotNone(non_editar_produto.key.get())

