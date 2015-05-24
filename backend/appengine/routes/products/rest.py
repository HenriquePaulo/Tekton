# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from product_app import product_facade


def index():
    cmd = product_facade.list_products_cmd()
    product_list = cmd()
    product_form = product_facade.product_form()
    product_dcts = [product_form.fill_with_model(m) for m in product_list]
    return JsonResponse(product_dcts)


def new(_resp, **product_properties):
    cmd = product_facade.save_product_cmd(**product_properties)
    return _save_or_update_json_response(cmd, _resp)


def edit(_resp, id, **product_properties):
    cmd = product_facade.update_product_cmd(id, **product_properties)
    return _save_or_update_json_response(cmd, _resp)


def delete(_resp, id):
    cmd = product_facade.delete_product_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


def _save_or_update_json_response(cmd, _resp):
    try:
        product = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    product_form = product_facade.product_form()
    return JsonResponse(product_form.fill_with_model(product))

