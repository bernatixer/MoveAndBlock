# Generated by Django 2.2.4 on 2019-09-14 20:29

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_message_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image_description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='message',
            name='image_tags',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='message',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(upload_to='files/message', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=versatileimagefield.fields.VersatileImageField(upload_to='files/user', verbose_name='Image'),
        ),
    ]
