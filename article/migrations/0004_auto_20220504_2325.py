# Generated by Django 3.2 on 2022-05-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': (('publish_article', 'Can publish article'),)},
        ),
        migrations.AddField(
            model_name='article',
            name='is_published',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateTimeField(null=True),
        ),
    ]
