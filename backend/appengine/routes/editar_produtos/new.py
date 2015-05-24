# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from editar_produto_app import editar_produto_facade
from routes import editar_produtos
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)}, 'editar_produtos/editar_produto_form.html')


def save(**editar_produto_properties):
    cmd = editar_produto_facade.save_editar_produto_cmd(**editar_produto_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'editar_produto': editar_produto_properties}

        return TemplateResponse(context, 'editar_produtos/editar_produto_form.html')
    return RedirectResponse(router.to_path(editar_produtos))

