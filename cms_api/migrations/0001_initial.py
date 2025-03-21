# Generated by Django 5.1.4 on 2025-03-21 13:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_api.country')),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('referral_code', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In-progress', 'In-progress'), ('Converted', 'Converted'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_api.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_api.country')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_api.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_api.country')),
                ('managed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='devices/')),
                ('currency', models.CharField(max_length=10)),
                ('offer_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=True)),
                ('sourced_from', models.ManyToManyField(to='cms_api.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='WalkIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=10)),
                ('offer_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('walk_in_datetime', models.DateTimeField(auto_now_add=True)),
                ('token_number', models.PositiveIntegerField(unique=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_api.device')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_api.lead')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_api.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('allowed_devices', models.ManyToManyField(blank=True, to='cms_api.device')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
        ),
        migrations.CreateModel(
            name='PageSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='sections/')),
                ('html_content', models.TextField()),
                ('order', models.PositiveIntegerField()),
                ('active', models.BooleanField(default=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_api.webpage')),
            ],
        ),
    ]
