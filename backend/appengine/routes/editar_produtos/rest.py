# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse
from editar_produto_app import editar_produto_facade



@no_csrf
def index():
    cmd = editar_produto_facade.list_editar_produtos_cmd()
    editar_produto_list = cmd()
    editar_produto_form = editar_produto_facade.editar_produto_form()
    editar_produto_dcts = [editar_produto_form.fill_with_model(m) for m in editar_produto_list]
    return JsonResponse(editar_produto_dcts)


def new(_resp, **editar_produto_properties):
    cmd = editar_produto_facade.save_editar_produto_cmd(**editar_produto_properties)
    return _save_or_update_json_response(cmd, _resp)

@no_csrf
@login_not_required
def edit(_resp, id, **editar_produto_properties):
    cmd = editar_produto_facade.update_editar_produto_cmd(id, **editar_produto_properties)
    return _save_or_update_json_response(cmd, _resp)


# def delete(product_id):
#     editar_produto_facade.delete_editar_produto_cmd(product_id)

def delete(_resp, product_id):
    cmd = editar_produto_facade.delete_editar_produto_cmd(product_id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)



def _save_or_update_json_response(cmd, _resp):
    try:
        editar_produto = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    editar_produto_form = editar_produto_facade.editar_produto_form()
    return JsonResponse(editar_produto_form.fill_with_model(editar_produto))

