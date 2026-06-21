from odoo import models
import io
import base64

class ItEquipementExcel(models.Model):
    _inherit = 'it.equipement'

    def action_export_excel(self):
        import xlsxwriter
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Équipements')

        # Styles
        header_format = workbook.add_format({
            'bold': True, 'bg_color': '#4B0082', 'font_color': 'white',
            'border': 1, 'align': 'center'
        })
        cell_format = workbook.add_format({'border': 1})

        # Headers
        headers = ['Référence', 'Nom', 'Type', 'Marque', 'Modèle',
                   'N° Série', 'Date Acquisition', 'Valeur (FCFA)',
                   'État', 'Employé', 'Localisation']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header, header_format)
            worksheet.set_column(col, col, 20)

        # Data
        equipements = self.env['it.equipement'].search([])
        for row, eq in enumerate(equipements, start=1):
            worksheet.write(row, 0, eq.reference or '-', cell_format)
            worksheet.write(row, 1, eq.name, cell_format)
            worksheet.write(row, 2, eq.type_equipement, cell_format)
            worksheet.write(row, 3, eq.marque or '-', cell_format)
            worksheet.write(row, 4, eq.modele or '-', cell_format)
            worksheet.write(row, 5, eq.numero_serie or '-', cell_format)
            worksheet.write(row, 6, str(eq.date_acquisition) if eq.date_acquisition else '-', cell_format)
            worksheet.write(row, 7, eq.valeur_achat, cell_format)
            worksheet.write(row, 8, eq.state, cell_format)
            worksheet.write(row, 9, eq.employee_id.name if eq.employee_id else '-', cell_format)
            worksheet.write(row, 10, eq.localisation or '-', cell_format)

        workbook.close()
        output.seek(0)
        data = base64.b64encode(output.read()).decode()

        attachment = self.env['ir.attachment'].create({
            'name': 'inventaire_equipements.xlsx',
            'type': 'binary',
            'datas': data,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }


class ItInterventionExcel(models.Model):
    _inherit = 'it.intervention'

    def action_export_excel(self):
        import xlsxwriter
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Interventions')

        header_format = workbook.add_format({
            'bold': True, 'bg_color': '#4B0082', 'font_color': 'white',
            'border': 1, 'align': 'center'
        })
        cell_format = workbook.add_format({'border': 1})

        headers = ['Référence', 'Titre', 'Équipement', 'Technicien',
                   'Type', 'Date Début', 'Date Fin', 'Durée (h)', 'Coût (FCFA)', 'État']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header, header_format)
            worksheet.set_column(col, col, 20)

        interventions = self.env['it.intervention'].search([])
        for row, inter in enumerate(interventions, start=1):
            worksheet.write(row, 0, inter.reference or '-', cell_format)
            worksheet.write(row, 1, inter.name, cell_format)
            worksheet.write(row, 2, inter.equipement_id.name, cell_format)
            worksheet.write(row, 3, inter.employee_id.name if inter.employee_id else '-', cell_format)
            worksheet.write(row, 4, inter.type_intervention, cell_format)
            worksheet.write(row, 5, str(inter.date_debut), cell_format)
            worksheet.write(row, 6, str(inter.date_fin) if inter.date_fin else '-', cell_format)
            worksheet.write(row, 7, inter.duree, cell_format)
            worksheet.write(row, 8, inter.cout, cell_format)
            worksheet.write(row, 9, inter.state, cell_format)

        workbook.close()
        output.seek(0)
        data = base64.b64encode(output.read()).decode()

        attachment = self.env['ir.attachment'].create({
            'name': 'rapport_interventions.xlsx',
            'type': 'binary',
            'datas': data,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }


class ItContratExcel(models.Model):
    _inherit = 'it.contrat'

    def action_export_excel(self):
        import xlsxwriter
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Contrats')

        header_format = workbook.add_format({
            'bold': True, 'bg_color': '#4B0082', 'font_color': 'white',
            'border': 1, 'align': 'center'
        })
        cell_format = workbook.add_format({'border': 1})

        headers = ['Référence', 'Nom', 'Fournisseur', 'Type',
                   'Date Début', 'Date Fin', 'Jours Restants', 'Montant (FCFA)', 'État']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header, header_format)
            worksheet.set_column(col, col, 20)

        contrats = self.env['it.contrat'].search([])
        for row, contrat in enumerate(contrats, start=1):
            worksheet.write(row, 0, contrat.reference or '-', cell_format)
            worksheet.write(row, 1, contrat.name, cell_format)
            worksheet.write(row, 2, contrat.partner_id.name if contrat.partner_id else '-', cell_format)
            worksheet.write(row, 3, contrat.type_contrat, cell_format)
            worksheet.write(row, 4, str(contrat.date_debut), cell_format)
            worksheet.write(row, 5, str(contrat.date_fin), cell_format)
            worksheet.write(row, 6, contrat.jours_restants, cell_format)
            worksheet.write(row, 7, contrat.montant, cell_format)
            worksheet.write(row, 8, contrat.state, cell_format)

        workbook.close()
        output.seek(0)
        data = base64.b64encode(output.read()).decode()

        attachment = self.env['ir.attachment'].create({
            'name': 'rapport_contrats.xlsx',
            'type': 'binary',
            'datas': data,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }