from odoo import models, fields, api

class ItAlerte(models.Model):
    _name = 'it.alerte'
    _description = 'Alerte Parc Informatique'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Titre', required=True, tracking=True)
    type_alerte = fields.Selection([
        ('contrat_expire', 'Contrat Expirant'),
        ('maintenance_due', 'Maintenance Due'),
        ('equipement_obsolete', 'Équipement Obsolète'),
        ('autre', 'Autre'),
    ], string="Type d'Alerte", required=True)
    date_alerte = fields.Date(string="Date d'Alerte", required=True)
    state = fields.Selection([
        ('nouveau', 'Nouveau'),
        ('lu', 'Lu'),
        ('traite', 'Traité'),
    ], string='État', default='nouveau', tracking=True)
    equipement_id = fields.Many2one('it.equipement', string='Équipement concerné')
    contrat_id = fields.Many2one('it.contrat', string='Contrat concerné')
    description = fields.Text(string='Description')
    priorite = fields.Selection([
        ('0', 'Normale'),
        ('1', 'Importante'),
        ('2', 'Urgente'),
    ], string='Priorité', default='0')

    def action_marquer_lu(self):
        self.state = 'lu'

    def action_traiter(self):
        self.state = 'traite'

    @api.model
    def _cron_generer_alertes(self):
        """Cron job pour générer les alertes automatiquement"""
        from datetime import date, timedelta
        today = date.today()
        seuil = today + timedelta(days=30)

        # Alertes contrats expirants
        contrats = self.env['it.contrat'].search([
            ('date_fin', '<=', seuil),
            ('date_fin', '>=', today),
            ('state', '=', 'actif'),
        ])
        for contrat in contrats:
            existing = self.search([
                ('contrat_id', '=', contrat.id),
                ('type_alerte', '=', 'contrat_expire'),
                ('state', '!=', 'traite'),
            ])
            if not existing:
                self.create({
                    'name': f'Contrat expirant : {contrat.name}',
                    'type_alerte': 'contrat_expire',
                    'date_alerte': today,
                    'contrat_id': contrat.id,
                    'description': f'Le contrat {contrat.name} expire le {contrat.date_fin}',
                    'priorite': '1',
                })