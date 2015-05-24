# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from product_app import product_facade
from routes import products
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(product_id):
    product = product_facade.get_product_cmd(product_id)()
    product_form = product_facade.product_form()
    context = {'save_path': router.to_path(save, product_id), 'product': product_form.fill_with_model(product)}
    return TemplateResponse(context, 'products/product_form.html')


def save(product_id, **product_properties):
    cmd = product_facade.update_product_cmd(product_id, **product_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors, 'product': product_properties}

        return TemplateResponse(context, 'products/product_form.html')
    return RedirectResponse(router.to_path(products))

