# Generated by Django 2.0.2 on 2018-03-23 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excuses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_text', models.CharField(max_length=500)),
                ('rootcause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actionplan', to='excuses.RootCause')),
            ],
        ),
    ]
