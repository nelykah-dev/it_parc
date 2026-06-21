from odoo import models, fields, api
from datetime import date

class ItContrat(models.Model):
    _name = 'it.contrat'
    _description = 'Contrat Fournisseur'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Intitulé du Contrat', required=True, tracking=True)
    reference = fields.Char(string='Référence', required=False, copy=False,
                            default=lambda self: self.env['ir.sequence'].next_by_code('it.contrat'))
    partner_id = fields.Many2one('res.partner', string='Fournisseur', required=False, tracking=True)
    type_contrat = fields.Selection([
        ('maintenance', 'Maintenance'),
        ('licence', 'Licence Logiciel'),
        ('support', 'Support Technique'),
        ('assurance', 'Assurance'),
        ('autre', 'Autre'),
    ], string='Type de Contrat', required=True)
    date_debut = fields.Date(string='Date Début', required=True)
    date_fin = fields.Date(string='Date Fin', required=True, tracking=True)
    montant = fields.Float(string='Montant (FCFA)')
    jours_restants = fields.Integer(string='Jours Restants', compute='_compute_jours_restants', store=True)
    state = fields.Selection([
        ('actif', 'Actif'),
        ('expire', 'Expiré'),
        ('renouvele', 'Renouvelé'),
        ('resilie', 'Résilié'),
    ], string='État', default='actif', tracking=True)
    description = fields.Text(string='Description')
    equipement_ids = fields.Many2many('it.equipement', string='Équipements Couverts')

    @api.depends('date_fin')
    def _compute_jours_restants(self):
        for rec in self:
            if rec.date_fin:
                delta = rec.date_fin - date.today()
                rec.jours_restants = delta.days
            else:
                rec.jours_restants = 0

    def action_renouveler(self):
        self.state = 'renouvele'

    def action_resilier(self):
        self.state = 'resilie'