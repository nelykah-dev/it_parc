/** @odoo-module **/
import { Component, useState, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

class ItParcDashboard extends Component {
    static template = "it_parc.Dashboard";

    setup() {
        this.orm = useService("orm");
        this.state = useState({
            total_equipements: 0,
            disponibles: 0,
            en_maintenance: 0,
            hors_service: 0,
            affectes: 0,
            interventions_en_cours: 0,
            contrats_expirants: 0,
            alertes_nouvelles: 0,
            chart_data: [],
        });

        onWillStart(async () => {
            await this.loadData();
        });
    }

    async loadData() {
        // KPI 1 - Total équipements
        const all = await this.orm.searchCount("it.equipement", []);
        this.state.total_equipements = all;

        // KPI 2 - Disponibles
        const dispo = await this.orm.searchCount("it.equipement", [["state", "=", "disponible"]]);
        this.state.disponibles = dispo;

        // KPI 3 - En maintenance
        const maint = await this.orm.searchCount("it.equipement", [["state", "=", "maintenance"]]);
        this.state.en_maintenance = maint;

        // KPI 4 - Hors service
        const hs = await this.orm.searchCount("it.equipement", [["state", "=", "hors_service"]]);
        this.state.hors_service = hs;

        // KPI 5 - Affectés
        const aff = await this.orm.searchCount("it.equipement", [["state", "=", "affecte"]]);
        this.state.affectes = aff;

        // KPI 6 - Interventions en cours
        const inter = await this.orm.searchCount("it.intervention", [["state", "=", "en_cours"]]);
        this.state.interventions_en_cours = inter;

        // KPI 7 - Contrats expirants (< 30 jours)
        const contrats = await this.orm.searchCount("it.contrat", [["jours_restants", "<=", 30], ["state", "=", "actif"]]);
        this.state.contrats_expirants = contrats;

        // KPI 8 - Alertes nouvelles
        const alertes = await this.orm.searchCount("it.alerte", [["state", "=", "nouveau"]]);
        this.state.alertes_nouvelles = alertes;

        // Données graphique
        this.state.chart_data = [
            { label: "Disponible", value: dispo, color: "#28a745" },
            { label: "Affecté", value: aff, color: "#007bff" },
            { label: "Maintenance", value: maint, color: "#ffc107" },
            { label: "Hors Service", value: hs, color: "#dc3545" },
        ];
    }

    getBarWidth(value) {
        const max = Math.max(...this.state.chart_data.map(d => d.value), 1);
        return Math.round((value / max) * 100);
    }
}

registry.category("actions").add("it_parc_dashboard", ItParcDashboard);