# Generated by Django 5.0.6 on 2024-08-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Delta', '0002_article_uploadedfile_delta_detail_delta_idea_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.RemoveField(
            model_name='delta',
            name='profile',
        ),
        migrations.AlterField(
            model_name='delta',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]