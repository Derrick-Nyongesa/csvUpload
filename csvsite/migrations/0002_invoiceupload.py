# Generated by Django 3.2.7 on 2021-09-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='invoices/')),
            ],
        ),
    ]
