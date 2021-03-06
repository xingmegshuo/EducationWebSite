# Generated by Django 2.1.5 on 2021-03-12 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20210206_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('push_url', models.CharField(help_text='推流地址', max_length=1000, verbose_name='推流地址')),
                ('pull_url', models.CharField(help_text='拉流地址', max_length=1000, verbose_name='拉流地址')),
                ('push_img', models.ImageField(help_text='推流二维码', upload_to='pic', verbose_name='推流二维码')),
                ('user', models.ForeignKey(help_text='主播', on_delete=django.db.models.deletion.CASCADE, to='video.User', verbose_name='主播')),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(help_text='视频', upload_to='video', verbose_name='视频'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_pic',
            field=models.ImageField(help_text='视频封面', upload_to='pic', verbose_name='视频封面'),
        ),
    ]
