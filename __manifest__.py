{
    'name': 'IT Parc - Gestion de Parc Informatique',
    'version': '18.0.1.0.0',
    'category': 'Information Technology',
    'summary': 'Gestion complète du parc informatique de TECHPARK CI',
    'description': """
        Module de gestion de parc informatique pour TECHPARK CI.
        Fonctionnalités : équipements, affectations, interventions,
        contrats fournisseurs, alertes, rapports PDF/Excel, dashboard OWL.
    """,
    'author': 'Nelikah',
    'depends': [
        'base', 'hr', 'stock', 'purchase',
        'account', 'maintenance', 'mail', 'contacts', 'web'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/it_equipement_views.xml',
        'views/it_intervention_views.xml',
        'views/it_contrat_views.xml',
        'views/it_alerte_views.xml',
        'views/menu_views.xml',
        'data/it_parc_cron.xml',
        'data/it_parc_demo.xml',
        'report/it_parc_reports.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'it_parc/static/src/components/dashboard.js',
            'it_parc/static/src/components/dashboard.xml',
            'it_parc/static/src/components/dashboard.css',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}