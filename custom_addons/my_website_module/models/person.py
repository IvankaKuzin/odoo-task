# noinspection PyUnresolvedReferences
from odoo import models, fields, api
from datetime import date

class Person(models.Model):
    _name = "my_website.person"
    _description = "Person Information"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    full_name = fields.Char(string="Full Name", compute="_compute_full_name", store=True)
    birthday = fields.Date(string="Birthday")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    sex = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("non-binary", "Non-Binary")
    ], string="Sex")
    company_id = fields.Many2one("res.company", string="Company", required=True, 
                                default=lambda self: self.env.company)

    @api.depends("first_name", "last_name")
    def _compute_full_name(self):
        for record in self:
            if record.first_name and record.last_name:
                record.full_name = f"{record.first_name} {record.last_name}"
            elif record.first_name:
                record.full_name = record.first_name
            elif record.last_name:
                record.full_name = record.last_name
            else:
                record.full_name = ""

    @api.depends("birthday")
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birthday:
                record.age = today.year - record.birthday.year - (
                    (today.month, today.day) < (record.birthday.month, record.birthday.day)
                )
            else:
                record.age = 0
