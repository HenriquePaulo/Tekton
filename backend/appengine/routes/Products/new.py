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
def index():
    return TemplateResponse({'save_path': router.to_path(save)}, 'Products/Product_form.html')


def save(**product_properties):
    cmd = Product_facade.save_product_cmd(**product_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'product': product_properties}

        return TemplateResponse(context, 'Products/Product_form.html')
    return RedirectResponse(router.to_path(Products))

