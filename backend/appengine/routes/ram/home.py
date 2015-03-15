from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required

@login_not_required
@no_csrf
def index(nome='paulo',sobrenome='henrique'):
    dct = {'name':nome,'lastname':sobrenome}
    return TemplateResponse(dct)
    #return TemplateResponse(template_path='/home.html')#chamo o arquivo "home.html" da pasta templates