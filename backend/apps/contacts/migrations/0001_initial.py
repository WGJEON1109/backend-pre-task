# Generated by Django 3.2.20 on 2023-07-27 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'label',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('memo', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'profile',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProfileLabel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.label')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.profile')),
            ],
            options={
                'db_table': 'profile_label',
                'managed': True,
                'unique_together': {('profile', 'label')},
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='labels',
            field=models.ManyToManyField(through='contacts.ProfileLabel', to='contacts.Label'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
