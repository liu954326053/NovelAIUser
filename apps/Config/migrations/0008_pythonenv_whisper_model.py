# Generated by Django 3.0.3 on 2023-08-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Config', '0007_pythonenv'),
    ]

    operations = [
        migrations.AddField(
            model_name='pythonenv',
            name='whisper_model',
            field=models.CharField(choices=[('large-v2', 'large-v2 需要 14 GB'), ('large-v1', 'large-v1 需要12 GB'), ('large', 'large 需要 10 GB'), ('medium', 'medium 需要 5 GB'), ('small', 'small 需要 2 GB'), ('base', 'base 需要 1 GB')], default='large', help_text='根据自己的显存选择', max_length=20, verbose_name='语音转文本模型'),
        ),
    ]
