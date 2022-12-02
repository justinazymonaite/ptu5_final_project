# Generated by Django 4.1.3 on 2022-12-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewellery', '0002_alter_category_options_alter_category_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pearl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel', models.CharField(max_length=30, verbose_name='parcel')),
                ('shape', models.CharField(max_length=30, verbose_name='shape')),
                ('color', models.CharField(max_length=30, verbose_name='color')),
                ('size', models.CharField(max_length=30, verbose_name='size')),
                ('type_name', models.CharField(max_length=30, verbose_name='type_name')),
            ],
            options={
                'ordering': ['parcel'],
            },
        ),
        migrations.AlterModelOptions(
            name='metaltype',
            options={'ordering': ['alloy']},
        ),
        migrations.RemoveField(
            model_name='metaltype',
            name='metal_type',
        ),
        migrations.AddField(
            model_name='metaltype',
            name='alloy',
            field=models.CharField(blank=True, max_length=30, verbose_name='alloy'),
        ),
        migrations.AddField(
            model_name='orderline',
            name='pearl',
            field=models.ManyToManyField(to='jewellery.pearl', verbose_name='pearl(s)'),
        ),
    ]
