from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ItEquipement(models.Model):
    _name = 'it.equipement'
    _description = 'Équipement Informatique'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nom', required=True, tracking=True)
    reference = fields.Char(string='Référence', required=False, copy=False,
                            default=lambda self: self.env['ir.sequence'].next_by_code('it.equipement'))
    type_equipement = fields.Selection([
        ('ordinateur', 'Ordinateur'),
        ('imprimante', 'Imprimante'),
        ('serveur', 'Serveur'),
        ('reseau', 'Équipement Réseau'),
        ('telephone', 'Téléphone'),
        ('autre', 'Autre'),
    ], string='Type', required=True, tracking=True)
    marque = fields.Char(string='Marque')
    modele = fields.Char(string='Modèle')
    numero_serie = fields.Char(string='Numéro de Série')
    date_acquisition = fields.Date(string="Date d'Acquisition")
    valeur_achat = fields.Float(string="Valeur d'Achat")
    state = fields.Selection([
        ('disponible', 'Disponible'),
        ('affecte', 'Affecté'),
        ('maintenance', 'En Maintenance'),
        ('hors_service', 'Hors Service'),
    ], string='État', default='disponible', tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Employé Affecté', tracking=True)
    date_affectation = fields.Date(string="Date d'Affectation")
    localisation = fields.Char(string='Localisation')
    note = fields.Text(string='Notes')
    intervention_ids = fields.One2many('it.intervention', 'equipement_id', string='Interventions')
    intervention_count = fields.Integer(string='Nb Interventions', compute='_compute_intervention_count')

    @api.depends('intervention_ids')
    # Calcule le nombre d'interventions liées à cet équipement
    def _compute_intervention_count(self):
        for rec in self:
            rec.intervention_count = len(rec.intervention_ids)
# Change l'état de l'équipement à "affecté"
    def action_affecter(self):
        self.state = 'affecte'

    def action_maintenance(self):
        self.state = 'maintenance'

    def action_disponible(self):
        self.state = 'disponible'
        self.employee_id = False

    def action_hors_service(self):
        self.state = 'hors_service'