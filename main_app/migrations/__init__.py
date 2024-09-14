from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_auto_20210101_1200'),  # This is an example, it may differ.
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('Entrepreneur', 'Entrepreneur'), ('RevenueOfficer', 'Revenue Authority Officer'), ('Investor', 'Investor/Normal User')], max_length=20)),
                ('business_name', models.CharField(blank=True, max_length=100, null=True)),
                ('business_owner_name', models.CharField(blank=True, max_length=100, null=True)),
                ('business_location', models.CharField(blank=True, max_length=100, null=True)),
                ('business_registration_number', models.CharField(blank=True, max_length=50, null=True)),
                ('passkey', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital', models.DecimalField(decimal_places=2, max_digits=10)),
                ('daily_sales', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profit_loss', models.DecimalField(decimal_places=2, max_digits=10)),
                ('performance_graph', models.ImageField(blank=True, null=True, upload_to='performance_graphs/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='TaxReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_paid', models.BooleanField(default=False)),
                ('report_date', models.DateField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.businessdata')),
                ('officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
        # Other migrations here...
    ]
