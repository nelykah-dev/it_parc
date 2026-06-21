from odoo import models, fields, api

class ItIntervention(models.Model):
    _name = 'it.intervention'
    _description = 'Intervention Technique'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Titre', required=True, tracking=True)
    reference = fields.Char(string='Référence', required=False, copy=False,
                            default=lambda self: self.env['ir.sequence'].next_by_code('it.intervention'))
    equipement_id = fields.Many2one('it.equipement', string='Équipement', required=True, tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Technicien', tracking=True)
    type_intervention = fields.Selection([
        ('maintenance', 'Maintenance Préventive'),
        ('reparation', 'Réparation'),
        ('installation', 'Installation'),
        ('configuration', 'Configuration'),
        ('autre', 'Autre'),
    ], string="Type d'Intervention", required=True)
    date_debut = fields.Datetime(string='Date Début', required=True)
    date_fin = fields.Datetime(string='Date Fin')
    duree = fields.Float(string='Durée (h)', compute='_compute_duree', store=True)
    state = fields.Selection([
        ('planifie', 'Planifiée'),
        ('en_cours', 'En Cours'),
        ('termine', 'Terminée'),
        ('annule', 'Annulée'),
    ], string='État', default='planifie', tracking=True)
    description = fields.Text(string='Description')
    rapport = fields.Text(string='Rapport')
    cout = fields.Float(string='Coût (FCFA)')

    @api.depends('date_debut', 'date_fin')
    def _compute_duree(self):
        for rec in self:
            if rec.date_debut and rec.date_fin:
                delta = rec.date_fin - rec.date_debut
                rec.duree = delta.total_seconds() / 3600
            else:
                rec.duree = 0.0

    def action_demarrer(self):
        self.state = 'en_cours'

    def action_terminer(self):
        self.state = 'termine'

    def action_annuler(self):
        self.state = 'annule'