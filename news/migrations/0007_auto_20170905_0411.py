# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 04:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0040_page_draft_title'),
        ('news', '0006_blogcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('author', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('date', models.DateField(verbose_name='Post date')),
                ('intro', models.CharField(max_length=250)),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NewsPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='news.NewsPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_newspagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='BlogCategory',
            new_name='NewsCategory',
        ),
        migrations.RenameModel(
            old_name='BlogIndexPage',
            new_name='NewsIndexPage',
        ),
        migrations.RenameModel(
            old_name='BlogPageGalleryImage',
            new_name='NewsPageGalleryImage',
        ),
        migrations.RenameModel(
            old_name='BlogTagIndexPage',
            new_name='NewsTagIndexPage',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='tag',
        ),
        migrations.AlterModelOptions(
            name='newscategory',
            options={'verbose_name_plural': 'news categories'},
        ),
        migrations.AlterField(
            model_name='newspagegalleryimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='news.NewsPage'),
        ),
        migrations.DeleteModel(
            name='BlogPage',
        ),
        migrations.DeleteModel(
            name='BlogPageTag',
        ),
        migrations.AddField(
            model_name='newspage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='news.NewsCategory'),
        ),
        migrations.AddField(
            model_name='newspage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='news.NewsPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
