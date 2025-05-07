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

    @http.route("/persons/add", type="http", auth="public", website=True)
    def person_form(self, **kw):
        companies = request.env["res.company"].sudo().search([])
        return request.render("my_website_module.person_add_form_template", {
            "companies": companies
        })

    @http.route("/persons/create", type="http", auth="public", website=True, methods=["POST"])
    def person_create(self, **post):
        if post.get("first_name") and post.get("last_name") and post.get("company_id"):
            company_id = int(post.get("company_id"))

            person_values = {
                "first_name": post.get("first_name"),
                "last_name": post.get("last_name"),
                "company_id": company_id,
                "sex": post.get("sex") or False,
            }

            if post.get("birthday"):
                person_values["birthday"] = post.get("birthday")

            request.env["my_website.person"].sudo().create(person_values)

            return request.redirect("/persons")

        companies = request.env["res.company"].sudo().search([])
        return request.render("my_website_module.person_add_form_template", {
            "companies": companies,
            "error": "Please fill all required fields.",
            "post": post,
        })
