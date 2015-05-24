# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from editar_produto_app.editar_produto_model import Editar_produto
from routes.editar_produtos.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Editar_produto.query().get())
        redirect_response = save(titulo='titulo_string', preco='preco_string', descricao='descricao_string', imagem='imagem_string', nome='nome_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_editar_produto = Editar_produto.query().get()
        self.assertIsNotNone(saved_editar_produto)
        self.assertEquals('titulo_string', saved_editar_produto.titulo)
        self.assertEquals('preco_string', saved_editar_produto.preco)
        self.assertEquals('descricao_string', saved_editar_produto.descricao)
        self.assertEquals('imagem_string', saved_editar_produto.imagem)
        self.assertEquals('nome_string', saved_editar_produto.nome)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['titulo', 'preco', 'descricao', 'imagem', 'nome']), set(errors.keys()))
        self.assert_can_render(template_response)
