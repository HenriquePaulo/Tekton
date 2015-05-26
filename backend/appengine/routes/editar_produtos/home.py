# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from editar_produto_app import editar_produto_facade
from routes.editar_produtos import new, edit,rest
from tekton.gae.middleware.redirect import RedirectResponse



@no_csrf
def index():
    context = {'list_path': router.to_path(rest.index),
               'delete_path': router.to_path(rest.delete),
               'rest_new_path': router.to_path(rest.new)}
    return TemplateResponse(context, 'editar_produtos/editar_produto_home.html')


def delete(editar_produto_id):
    editar_produto_facade.delete_editar_produto_cmd(editar_produto_id)()
    return RedirectResponse(router.to_path(index))

