# Generated by Django 4.1.6 on 2023-02-20 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DimPecheArtisan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActPech_Artisan', models.CharField(max_length=250)),
                ('GroupPecheur', models.CharField(max_length=250)),
                ('GroupMareyeur', models.CharField(max_length=250)),
                ('TypePirogu', models.CharField(max_length=250)),
                ('TypProdPechPirogBois', models.CharField(max_length=250)),
                ('TypProdPechPirogFibr', models.CharField(max_length=250)),
                ('TypProdPechPirogAlumin', models.CharField(max_length=250)),
                ('TypeProdHalieuHiver', models.CharField(max_length=250)),
                ('TypeProdHalieuInterSaison', models.CharField(max_length=250)),
                ('TypeProdHalieuSaisFroid', models.CharField(max_length=250)),
                ('TypeProdHalieuPrimptem', models.CharField(max_length=250)),
                ('IntrantPech', models.CharField(max_length=250)),
                ('MatUtilisePech', models.CharField(max_length=250)),
                ('SourcApprovis_Intran', models.CharField(max_length=250)),
                ('SourcApprovis_Materiel', models.CharField(max_length=250)),
                ('NivCaptMoyenHiver', models.CharField(max_length=250)),
                ('NivCaptMoyenInterSaison', models.CharField(max_length=250)),
                ('NivCaptMoyenSaisFroid', models.CharField(max_length=250)),
                ('NivCaptMoyenPrintem', models.CharField(max_length=250)),
                ('NivCaptMoyenSortTypProd', models.CharField(max_length=250)),
                ('NivPertPostCaptHiver', models.CharField(max_length=250)),
                ('NivPertPostCaptInterSaison', models.CharField(max_length=250)),
                ('NivPertPostCaptSaisFroid', models.CharField(max_length=250)),
                ('NivPertPostCaptPrintem', models.CharField(max_length=250)),
                ('NivPertPostCaptTypProd', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheAssure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeAssurancPech', models.CharField(max_length=25)),
                ('OffreAssureExistPech', models.CharField(max_length=25)),
                ('BesoinFormatPech', models.CharField(max_length=250)),
                ('ActeurSensibilisePech', models.CharField(max_length=250)),
                ('ActeurFormatPech', models.CharField(max_length=250)),
                ('BesoinSensibilisePech', models.CharField(max_length=250)),
                ('ContraintGlobPech', models.CharField(max_length=250)),
                ('ContrainMajFilier', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheCommerce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdVendType', models.IntegerField()),
                ('ProdVendCampgnInterSais', models.IntegerField()),
                ('ProdVendCampgnHiver', models.IntegerField()),
                ('ProdVendCampSaisFroid', models.IntegerField()),
                ('ProdVendCampPrintem', models.IntegerField()),
                ('Type_VentPech', models.CharField(max_length=250)),
                ('Mod_ecoulement', models.CharField(max_length=250)),
                ('ClientPech', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheFinance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OffrServicFinancPech', models.CharField(max_length=25)),
                ('TypGaranExige', models.CharField(max_length=250)),
                ('LongProcedCredi', models.CharField(max_length=250)),
                ('DemandApportPech', models.CharField(max_length=25)),
                ('TauInteret', models.CharField(max_length=250)),
                ('DelaiRemboursMinMax', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheInnovat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TechnoIntrod', models.CharField(max_length=250)),
                ('TechnoAdopte', models.CharField(max_length=25)),
                ('CausNoAdoption', models.CharField(max_length=250)),
                ('CausTechnoNoAdop', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DimPecheTAInnovat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TechnoIntroTA', models.CharField(max_length=250)),
                ('TechnoAdoptTA', models.CharField(max_length=25)),
                ('CausNoAdoptTA', models.CharField(max_length=250)),
                ('CausTechnoNoAdop', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DimPechTAAssurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OffreAssurTA', models.CharField(max_length=250)),
                ('TypAssurTA', models.CharField(max_length=250)),
                ('NivPrimTA', models.CharField(max_length=250)),
                ('BesoinformTA', models.CharField(max_length=250)),
                ('ContraintGlobTA', models.CharField(max_length=250)),
                ('ContrainMajFilierTA', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DimPechTACommerc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdVenduCampagTA', models.IntegerField()),
                ('TypVentTA', models.IntegerField()),
                ('ModEcoulmtTA', models.IntegerField()),
                ('ClientTA', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DimPechTAFinance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OffrServicFinancTA', models.CharField(max_length=25)),
                ('DemandApportTA', models.CharField(max_length=25)),
                ('TypGaranExigeTA', models.CharField(max_length=250)),
                ('LongProcedCrditTA', models.CharField(max_length=250)),
                ('TauInterTA', models.CharField(max_length=250)),
                ('DelaiRemboursMinMaxTA', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='DimPechTransformArtisan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActTransfArtisan', models.CharField(max_length=25)),
                ('GrptTransformtrTA', models.CharField(max_length=25)),
                ('TypServicOffrGIE', models.CharField(max_length=250)),
                ('TypServicOffrAssocia', models.CharField(max_length=250)),
                ('TypServicOffrOrgProf', models.CharField(max_length=250)),
                ('MatEquipTransExist', models.CharField(max_length=250)),
                ('TypProdTransfPeriod', models.CharField(max_length=250)),
                ('SourcApproIntranMatTA', models.CharField(max_length=250)),
                ('QteProdPeriodTA', models.IntegerField()),
                ('QteProdTypeTA', models.IntegerField()),
                ('TauxTransformArtisan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FactPeche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QteProdPeriodTA', models.IntegerField()),
                ('TauxTransformArtisan', models.IntegerField()),
                ('IdGeographie', models.IntegerField()),
                ('NbrActeur', models.IntegerField()),
                ('NbreGIEPecheur', models.IntegerField()),
                ('NbrOrganiProfessPecheur', models.IntegerField()),
                ('Nbr_AssociatPecheur', models.IntegerField()),
                ('NbrOrganiProfessMarey', models.IntegerField()),
                ('Nbr_AssociatMarey', models.IntegerField()),
                ('NbreQuaiPech', models.IntegerField()),
                ('NbrPirogBois', models.IntegerField()),
                ('NbrePirogFibVer', models.IntegerField()),
                ('NbrPirogAlumin', models.IntegerField()),
                ('NbrePirogImmatri', models.IntegerField()),
                ('NbreSouscripPech', models.IntegerField()),
                ('NbrePrimePech', models.IntegerField()),
                ('Qteannuel_debarq', models.IntegerField()),
                ('NbrSouscripTA', models.IntegerField()),
                ('QteProdTypeTA', models.IntegerField()),
                ('PrixVentMoyProdTA', models.IntegerField()),
                ('IdPechArtisan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peche.dimpecheartisan')),
                ('IdPechAssure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peche.dimpecheassure')),
                ('IdPechComm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peche.dimpechecommerce')),
                ('IdPechFinance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peche.dimpechefinance')),
                ('IdPechInnov', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peche.dimpecheinnovat')),
                ('IdPechInnovTA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peche.dimpechetainnovat')),
                ('IdPechTAAssure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peche.dimpechtaassurance')),
                ('IdPechTAComm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peche.dimpechtacommerc')),
                ('IdPechTAFinance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peche.dimpechtafinance')),
                ('IdPechTransFormArtisan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peche.dimpechtransformartisan')),
            ],
        ),
    ]
