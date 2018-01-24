# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-23 10:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u533a\u57df\u540d\u79f0')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u533b\u9662\u540d\u79f0')),
            ],
        ),
        migrations.CreateModel(
            name='IllnessImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=500, upload_to=b'', verbose_name='\u75c5\u60c5\u56fe\u7247')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u60a3\u8005\u59d3\u540d')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='\u51fa\u751f\u65e5\u671f')),
                ('sex', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u6027\u522b')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u624b\u673a')),
                ('wantTime', models.DateTimeField(null=True, verbose_name='\u9884\u7ea6\u65f6\u95f4')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='\u75c5\u60c5\u63cf\u8ff0')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u63d0\u4ea4\u65f6\u95f4')),
                ('nextcalldate', models.DateField(null=True, verbose_name='\u4e0b\u6b21\u7535\u8bdd\u65f6\u95f4')),
                ('status', models.IntegerField(choices=[(1, '\u672a\u8ba4\u9886'), (2, '\u5df2\u8ba4\u9886\u672a\u786e\u8ba4'), (3, '\u786e\u8ba4\u53bb\u5c31\u8bca'), (4, '\u786e\u8ba4\u4e0d\u5c31\u8bca'), (5, '\u5ef6\u671f\u9884\u7ea6'), (6, '\u5df2\u5b89\u6392\u6cbb\u7597'), (7, '\u5b8c\u6210\u9996\u6b21\u968f\u8bbf'), (8, '\u5b8c\u621015\u65e5\u968f\u8bbf'), (9, '\u5b8c\u621030\u65e5\u968f\u8bbf'), (10, '\u5b8c\u621045\u65e5\u968f\u8bbf'), (11, '\u5ef6\u540e\u6cbb\u7597'), (12, '\u6682\u505c\u8ddf\u8fdb'), (13, '\u8f6c\u9662'), (14, '\u786e\u8ba4\u672a\u5230\u8bca')], default=1, verbose_name='\u5f53\u524d\u72b6\u6001')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apoint.Area', verbose_name='\u533a\u57df')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u64cd\u4f5c\u65f6\u95f4')),
                ('status', models.IntegerField(choices=[(1, '\u672a\u8ba4\u9886'), (2, '\u5df2\u8ba4\u9886\u672a\u786e\u8ba4'), (3, '\u786e\u8ba4\u53bb\u5c31\u8bca'), (4, '\u786e\u8ba4\u4e0d\u5c31\u8bca'), (5, '\u5ef6\u671f\u9884\u7ea6'), (6, '\u5df2\u5b89\u6392\u6cbb\u7597'), (7, '\u5b8c\u6210\u9996\u6b21\u968f\u8bbf'), (8, '\u5b8c\u621015\u65e5\u968f\u8bbf'), (9, '\u5b8c\u621030\u65e5\u968f\u8bbf'), (10, '\u5b8c\u621045\u65e5\u968f\u8bbf'), (11, '\u5ef6\u540e\u6cbb\u7597'), (12, '\u6682\u505c\u8ddf\u8fdb'), (13, '\u8f6c\u9662'), (14, '\u786e\u8ba4\u672a\u5230\u8bca')], default=0, verbose_name='\u72b6\u6001')),
                ('remark', models.CharField(max_length=1000, null=True, verbose_name='\u63cf\u8ff0')),
                ('nextcalldate', models.DateField(null=True, verbose_name='\u4e0b\u6b21\u7535\u8bdd\u65f6\u95f4')),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u64cd\u4f5c\u4eba')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apoint.Order', verbose_name='\u6240\u5c5e\u9884\u7ea6')),
            ],
        ),
        migrations.CreateModel(
            name='ZJUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.IntegerField(choices=[(1, '\u5ba2\u670d'), (2, '\u9500\u552e'), (3, '\u7ba1\u7406\u5458')], default=1, verbose_name='\u7528\u6237\u7c7b\u578b')),
                ('openid', models.CharField(max_length=100, unique=True, verbose_name='openid')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='sales',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apoint.ZJUser', verbose_name='\u6240\u5c5e\u9500\u552e'),
        ),
        migrations.AddField(
            model_name='order',
            name='wanthospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apoint.Hospital', verbose_name='\u533b\u9662\u540d\u79f0'),
        ),
        migrations.AddField(
            model_name='illnessimage',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apoint.ZJUser', verbose_name='\u4e0a\u4f20\u4eba'),
        ),
    ]
