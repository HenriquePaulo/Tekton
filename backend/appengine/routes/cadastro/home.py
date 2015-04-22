# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from config.template_middleware import TemplateResponse
from tekton import router


@login_not_required
@no_csrf
def index():
    return form()


@login_not_required
@no_csrf
def form():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)


@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    _resp.write(propriedades)
