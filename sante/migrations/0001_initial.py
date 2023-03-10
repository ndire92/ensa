# Generated by Django 4.1.6 on 2023-02-20 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GouvernanceSante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeCommune', models.IntegerField()),
                ('CodeDomaine', models.IntegerField()),
                ('CodeTemps', models.IntegerField()),
                ('DepenseDeFonctionnement', models.IntegerField()),
                ('DepenseInvistissement', models.IntegerField()),
                ('MasseSalariale', models.IntegerField()),
                ('PersonnelMedical', models.IntegerField()),
                ('PersonnelDappui', models.IntegerField()),
                ('MasseSalarialePersonnelSanitaireEtAppui', models.IntegerField()),
                ('DepenseEnEauDansLeDomaineDeLaSante', models.IntegerField()),
                ('DepenseEnElectriciteDansLeDomaineDeLaSante', models.IntegerField()),
                ('AchatDeMedicamentAideSociale', models.IntegerField()),
                ('TotalDesDepensesEnSante', models.IntegerField()),
                ('DepensesInvestissementSante', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlanificationFamiliale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('CodeDomaine', models.IntegerField()),
                ('CodeTemps', models.IntegerField()),
                ('R20TauxdeRecrutementPF', models.IntegerField()),
                ('R20TauxdAbandonPF', models.IntegerField()),
                ('R20TotalAbandonsPF', models.IntegerField()),
                ('R20PourcentagedeFemmesde15a49ansSousMethodeContraceptiveapresAvortement', models.IntegerField()),
                ('R20PourcentagedUtilisatricesPF', models.IntegerField()),
                ('R20PourcentagedUtilisatricesPFchezles15a49ans', models.IntegerField()),
                ('R20TauxdePrevalencecontraceptive', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReproductionEtJeune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('CodeDomaine', models.IntegerField()),
                ('CodeTemps', models.IntegerField()),
                ('R20PourcentageAdolescentes15a19anSousMethodeContraceptiveApresAvortement', models.IntegerField()),
                ('R20PourcentageAdolescentes20a24ansSousMethodeContraceptiveApresAvortement', models.IntegerField()),
                ('R20PourcentageDAvortementsChezLesAdolescentesDe15a19ansPrisEnChargeParAmiuAuPremierTrimestre', models.IntegerField()),
                ('R20PourcentageAvortementsChezLesJeunesFemmesDe20a24ansPrisEnChargeAuPremierTrimestreParMisoprostol', models.IntegerField()),
                ('R20PourcentageAvortementsChezLesAdolescentesDe20a24ansPrisEnChargeParAmiuAuPremierTrimestre', models.IntegerField()),
                ('R20PourcentageAvortementsChezLesAdolescentesDe15a19ansPrisEnChargeAuPremierTrimestreParMisoprostol', models.IntegerField()),
                ('R20PourcentageAccouchementsDesAdolescentesDe15a19ansAssistesParUnPersonnelQalifie', models.IntegerField()),
                ('R20PourcentageAccouchementsDesAdolescentesDe20a24ansAssistesParUnPersonnelQualifie', models.IntegerField()),
                ('R20PourcentageUtilisatricesPFchezLes15a49ans', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SanteAlimentationEtNutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('CodeTemps', models.IntegerField()),
                ('PourcentageEnfantsDemoinsDe5ansAyantUneInsuffisancePonderale1', models.IntegerField()),
                ('PourcentageDeFemmesEnceintesPresentantUneAnemie', models.IntegerField()),
                ('PourcentageEnfantsDemoinsDe5ansAyantUneInsuffisancePonderale', models.IntegerField()),
                ('PourcentageEnfantsDemoinsDe5ansAyantUneInsuffisancePonderaleModeree', models.IntegerField()),
                ('PourcentageEnfantsDemoinsDe5ansAyantUneInsuffisancePonderaleGrave', models.IntegerField()),
                ('PourcentageEnfantsDemoinsDe5ansAyantUneInsuffisancePonderaleGlobale', models.IntegerField()),
                ('PourcentageEnfantsDemoinsDe5ansAyantUneMASsansComplication', models.IntegerField()),
                ('PourcentageEnfantsDemoinsDe5ansSouffrantDeMAM', models.IntegerField()),
                ('R20PourcentageEnfantsDeMoinsDe5ansDepistesPourLaMalnutritionAigue', models.IntegerField()),
                ('R20PourcentageFemmeEnceintePresentantUneMalnutritionAigue', models.IntegerField()),
                ('R20pourcentageEnfantsDeMoinsDe5ansPresentantUneAnemie', models.IntegerField()),
                ('R20PourcentageEnfantsDemoinsDe5ansAyantUnRetardDeCroissanceSevereTA', models.IntegerField()),
                ('R20PourcentageEnfantsDeMoinsDe5ansAyantunRetardDeCroissanceTA', models.IntegerField()),
                ('R20TauxAbandonDesEnfantsMoins5ansMASAuCREN', models.IntegerField()),
                ('PourcentageEnfants6a59moisDepistesPourMAM', models.IntegerField()),
                ('NouvellesAdmissionsLieesALaRechuteCREN', models.IntegerField()),
                ('NouvellesAdmissionsLieesALaRechuteUREN', models.IntegerField()),
                ('R20TAuxDeGuerisonDesEnfants6a59MoisMASaLUREN', models.IntegerField()),
                ('TotalEnfantsMAM6a59MoisDepistes', models.IntegerField()),
                ('TauxDeGuerisonUREN', models.IntegerField()),
                ('R20ProportionEnfantsDeMoinsDe5ansSouffrantDeMalnutritionAigueMod??r??eMAM', models.IntegerField()),
                ('R20TauxDeMASTraiteAvecSuccesAuCREN', models.IntegerField()),
                ('R20ProportionEnfantsDeMoinsDe5ansAyantUneInsuffisancePonderaleSevere', models.IntegerField()),
                ('R20ProportionDesEnfantsDeMoinsDe5ansMASGueris', models.IntegerField()),
                ('MalnutritionChroniqueOuRetardDeCroissanceSevereTA', models.IntegerField()),
                ('MalnutritionChroniqueOuRetardDeCroissanceModereeTA', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SantePaludisme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('CodeDomaine', models.IntegerField()),
                ('CodeTemps', models.IntegerField()),
                ('TauxDeMorbiditeProportionnellePalustreTousAge', models.IntegerField()),
                ('TauxDeMorbiditeProportionnellePalustreChezLesFemmesEnceintes', models.IntegerField()),
                ('TauxDemorbiditeProportionnellePalustreChezLesMoinsDe5ans', models.IntegerField()),
                ('IND20IncidenceDuPaludismePour1000Habitants', models.IntegerField()),
                ('IncidenceDuPaludismegGraveTotal', models.IntegerField()),
                ('R20CasPaludismeConfirmesTotal', models.IntegerField()),
                ('ombreTotalDeCasPaludismeSimpleConfirmesEnregistreesSurLaP??riodeParLesDSDOMQuiOntRe??uUnTraitemen', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SurvieEnfant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('CodeDomaine', models.IntegerField()),
                ('CodeTemps', models.IntegerField()),
                ('PourcentageEnfants0a59MoisAyantFaitUneDiarrhe', models.IntegerField()),
                ('R20ProportionDeCasDePneuMonie0a59Mois', models.IntegerField()),
                ('R20ProportionEnfantsAvecPneumonieGraveDontLaSaturationEnoxyg??neAEtemesuree', models.IntegerField()),
                ('R20ProportionEnfantsDe0a59MoisSouffrantAnemie', models.IntegerField()),
                ('R20ProportionEnfantsDe0a59moisPresentantUneAnemie', models.IntegerField()),
                ('SAVEDeCasEnfantsDeMoinsDe5ansCorrectementSoignesContreLaDiarrheeDansLesCentresDeSanteCommunautairesM', models.IntegerField()),
                ('NombreDeCasDeDiarrheeReferesParleNiveauCommunautaire', models.IntegerField()),
                ('R20PourcentageEnfantsDe6a11MoisSupplementesEnVitamineAEnRoutine', models.IntegerField()),
                ('R20PourcentageEnfantsDe12a59MoisSupplementesEnVitamineAEnRoutine', models.IntegerField()),
                ('R20PourcentageEnfantsDe12a59MoisDeParasit??sEnRoutine', models.IntegerField()),
                ('R20ProportionEnfantsDe0a59MoisAyantUnNum??roEtatcivil', models.IntegerField()),
                ('R20EnfantsDe0a59MoisRe??usPourTraumatismeDuSaUnAccidentEtOuAUnActedeViolenceNombreTotalEnfants0a59MoisVusenConsultation', models.IntegerField()),
                ('DiarrheeReferesParleNiveauCommunautaire0a59mois', models.IntegerField()),
                ('SupplementationSystematiqueEnVitamineADesEnfantsDe6a59Mois', models.IntegerField()),
                ('R20PourcentageEnfantsDe6a59MoisSupplementesEnVitamineAEnRoutine', models.IntegerField()),
                ('PourcentageEnfants12a59MoisDeparasitesEnRoutineOK', models.IntegerField()),
                ('R20NombreDeCasDePneumonies0a59mois', models.IntegerField()),
                ('R20NombreEnfantsDe0a59MoisPresentantUnePneumonieGraveAvechypoxietraiteeParoxyg??noTh??rapieAuNiveauDesPPSFeminin', models.IntegerField()),
                ('R20NombreEnFantsDe0a59MoisPresentantUnePneumonieGraveAvecHypoxieTraiteeParoxyg??noTh??rapieAuNiveauDesPPSMasculin', models.IntegerField()),
                ('R20NombreEnfantsDe0a59MoisPresentantUnePneumonieGravecHezquilaSaturationEnOxyg??neAEteMesureeAuNiveauDesPPSFeminin', models.IntegerField()),
                ('R20NombreEnfantsDe0a59MoisPresentantUnePneumonieGravecHezquiLaSaturationEnOxyg??neAEteMesureeAuNiveauDesPPSMasculin', models.IntegerField()),
                ('R20PourcentageEnfantsde0a59MoisPresentantUnePneumonieGravechezquiLaSaturationEnOxyg??neAEteMesureeAuNiveauDesPPS', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationEtRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeDistrict', models.IntegerField()),
                ('CodeDomaine', models.IntegerField()),
                ('CodeTemps', models.IntegerField()),
                ('TauxDeCouvertureAuPenta3', models.IntegerField()),
                ('TauxDeCouvertureAuRR1', models.IntegerField()),
                ('TauxDeCouvertureAuHepBInferieurOuEgal24heures', models.IntegerField()),
                ('Total0A11MoisNbreEnfantCompletementVaccine', models.IntegerField()),
                ('RR2Couverture12A23Mois', models.IntegerField()),
                ('Total12A23MoisF??mininNbreEnfantCompletementVaccine', models.IntegerField()),
                ('Total12A23MoisMasculinNbreEnfantCompletementVaccine', models.IntegerField()),
            ],
        ),
    ]
