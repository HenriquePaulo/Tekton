# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
#from google.appengine.ext import ndb
from google.appengine.ext import ndb
from gaecookie.decorator import no_csrf
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node
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


class Login(Node):
    name = ndb.StringProperty(required=True)#required = true significa que é obrigatório
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)

class LoginForm(ModelForm):
    _model_class = Login
@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    login_form = LoginForm(**propriedades)
    erros = login_form.validate()
    if erros:
       contexto = {'salvar_path': router.to_path(salvar),
                   'erros': erros,
                   'login' : login_form}
       return TemplateResponse(contexto,'/cadastro/home.html')

    else:
        pass
        login=LoginForm.fill_model()

        login.put()
        #_resp.write(propriedades)

        #feito para mostrar o que esta sendo salvo no banco


