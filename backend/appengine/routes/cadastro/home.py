# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
<<<<<<< HEAD
=======
#from google.appengine.ext import ndb
>>>>>>> refs/remotes/origin/master
from google.appengine.ext import ndb
from gaecookie.decorator import no_csrf
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node
from gaepermission.decorator import login_not_required
from config.template_middleware import TemplateResponse
from tekton import router


class Login(Node):
    name = ndb.StringProperty(required=True)#required = true significa que é obrigatório
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)

class LoginForm(ModelForm):
    _model_class = Login
    _include = [Login.name, Login.email, Login.password]


@login_not_required
@no_csrf
def index(_resp,**propriedades):
    login_form = LoginForm(**propriedades)
    erros = login_form.validate()
    if erros:
       contexto = {'salvar_path': router.to_path(index),
                   'erros': erros,
                   'form' : login_form}
       return TemplateResponse(contexto,'/cadastro/home.html')
    else:
        login=login_form.fill_model()
        login.put()
        _resp.write(propriedades)



