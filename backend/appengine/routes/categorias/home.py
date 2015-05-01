# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from google.appengine.api import users
from routes.produtos.home import *


@login_not_required
@no_csrf
def index(categorias):


    query = Produtos.query(Produtos.nome == categorias)#constroi a query para enviar pro banco

    biblioteca = {'categorias': categorias , 'produto_lista':query.fetch()}

    return TemplateResponse(biblioteca)
