# Generated by Django 3.0.3 on 2020-02-19 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_article_comment_like_source_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.Source'),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.PositiveIntegerField(choices=[(1, 'BBC'), (2, 'CNN'), (3, 'Ukraine news')]),
        ),
    ]
