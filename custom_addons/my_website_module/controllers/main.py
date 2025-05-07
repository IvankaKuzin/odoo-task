# noinspection PyUnresolvedReferences
from odoo import http
# noinspection PyUnresolvedReferences
from odoo.http import request


class PersonsController(http.Controller):

    @http.route("/persons", type="http", auth="public", website=True)
    def persons_page(self, **kw):
        persons = request.env["my_website.person"].sudo().search([], limit=5, order="create_date desc")

        return request.render("my_website_module.persons_page_template", {
            "persons": persons
        })
