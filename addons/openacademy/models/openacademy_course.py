# -*- coding: utf-8 -*-
from odoo import fields, models


class OpenacademyCourse(models.Model):
    _name = "openacademy.course"
    _description = "OpenAcademy Courses"

    name = fields.Char(
        string="Nombre",
        required=True,
    )
    description = fields.Text()
