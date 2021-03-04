# Generated by Django 3.1.6 on 2021-02-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='desc',
            name='desc_en',
            field=models.TextField(help_text='图片介绍', null=True, verbose_name='图片介绍'),
        ),
        migrations.AddField(
            model_name='desc',
            name='desc_zh_hans',
            field=models.TextField(help_text='图片介绍', null=True, verbose_name='图片介绍'),
        ),
        migrations.AlterField(
            model_name='desc',
            name='pic',
            field=models.ImageField(help_text='图片', upload_to='pic', verbose_name='图片'),
        ),
    ]
