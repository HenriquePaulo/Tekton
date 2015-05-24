# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from Product_app import Product_facade
from routes import Products
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(product_id):
    product = Product_facade.get_product_cmd(product_id)()
    product_form = Product_facade.product_form()
    context = {'save_path': router.to_path(save, product_id), 'product': product_form.fill_with_model(product)}
    return TemplateResponse(context, 'Products/Product_form.html')


def save(product_id, **product_properties):
    cmd = Product_facade.update_product_cmd(product_id, **product_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors, 'product': product_properties}

        return TemplateResponse(context, 'Products/Product_form.html')
    return RedirectResponse(router.to_path(Products))

