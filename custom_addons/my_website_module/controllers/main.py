# noinspection PyUnresolvedReferences
from odoo import http
# noinspection PyUnresolvedReferences
from odoo.http import request


class PersonsController(http.Controller):

    @http.route("/persons", type="http", auth="public", website=True)
    def persons_page(self, **kw):
        persons = request.env["persons.person"].sudo().search([], limit=5, order="create_date desc")

        return request.render("persons_module.persons_page_template", {
            "persons": persons
        })
