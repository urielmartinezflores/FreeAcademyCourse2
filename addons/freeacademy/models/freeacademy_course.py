# -*- coding: utf-8 -*-
from odoo import fields, models


class FreeacademyCourse(models.Model):
    _name = "freeacademy.course"
    _description = "FreeAcademy Courses"

    name = fields.Char(
        string="Nombre",
        required=True,
    )
    description = fields.Text()

    costo = fields.Integer(
        string="Costo del curso",
        required=True,
    )
