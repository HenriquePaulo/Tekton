# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from editar_produto_app.editar_produto_model import Editar_produto
from routes.editar_produtos.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        editar_produto = mommy.save_one(Editar_produto)
        template_response = index(editar_produto.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        editar_produto = mommy.save_one(Editar_produto)
        old_properties = editar_produto.to_dict()
        redirect_response = save(editar_produto.key.id(), titulo='titulo_string', preco='preco_string', descricao='descricao_string', imagem='imagem_string', nome='nome_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_editar_produto = editar_produto.key.get()
        self.assertEquals('titulo_string', edited_editar_produto.titulo)
        self.assertEquals('preco_string', edited_editar_produto.preco)
        self.assertEquals('descricao_string', edited_editar_produto.descricao)
        self.assertEquals('imagem_string', edited_editar_produto.imagem)
        self.assertEquals('nome_string', edited_editar_produto.nome)
        self.assertNotEqual(old_properties, edited_editar_produto.to_dict())

    def test_error(self):
        editar_produto = mommy.save_one(Editar_produto)
        old_properties = editar_produto.to_dict()
        template_response = save(editar_produto.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['titulo', 'preco', 'descricao', 'imagem', 'nome']), set(errors.keys()))
        self.assertEqual(old_properties, editar_produto.key.get().to_dict())
        self.assert_can_render(template_response)
