# -*- coding: utf-8 -*-
from odoo import fields, models


class OpenacademySession(models.Model):
    _name = "openacademy.session"
    _description = "OpenAcademy Session"

    name = fields.Char(
        required=True,
    )
    start_date = fields.Date()
    duration = fields.Float(
        digits=(6, 2),
        help="Duration in days",
    )
    seats = fields.Integer(
        string="Number of seat",
    )
    instructor_id = fields.Many2one(
        comodel_name="res.partner",
    )
    course_id = fields.Many2one(
        comodel_name="openacademy.course",
        ondelete="cascade",
        required=True,
    )
