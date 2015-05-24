# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from Product_app import Product_facade
from routes.Products import new, edit
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    cmd = Product_facade.list_products_cmd()
    products = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    product_form = Product_facade.product_form()

    def localize_product(product):
        product_dct = product_form.fill_with_model(product)
        product_dct['edit_path'] = router.to_path(edit_path, product_dct['id'])
        product_dct['delete_path'] = router.to_path(delete_path, product_dct['id'])
        return product_dct

    localized_products = [localize_product(product) for product in products]
    context = {'products': localized_products,
               'new_path': router.to_path(new)}
    return TemplateResponse(context, 'Products/Product_home.html')


def delete(product_id):
    Product_facade.delete_product_cmd(product_id)()
    return RedirectResponse(router.to_path(index))

