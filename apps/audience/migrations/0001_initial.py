# Generated by Django 2.2.6 on 2020-07-03 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='数据源名称')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='数据源描述')),
                ('status', models.SmallIntegerField(choices=[(0, 'DISABLE'), (1, 'ENABLE')], default=1, verbose_name='状态')),
                ('source', models.SmallIntegerField(choices=[(0, 'FILE_IMPORT'), (1, 'INSIGHT'), (2, 'OFFICIAL_ACCOUNT')], default=2, verbose_name='来源')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.Brand', verbose_name='品牌')),
            ],
            options={
                'verbose_name': '数据源',
            },
        ),
        migrations.CreateModel(
            name='TargetAudience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='目标受众名称')),
                ('rule', models.CharField(max_length=100, verbose_name='规则')),
                ('status', models.SmallIntegerField(choices=[(0, 'DISABLE'), (1, 'ENABLE')], default=1, verbose_name='状态')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('audience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audience.Audience', verbose_name='数据源')),
            ],
        ),
        migrations.CreateModel(
            name='WechatUsers',
            fields=[
                ('openid', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='用户的标识')),
                ('subscribe', models.IntegerField(default=1, verbose_name='是否关注公众号')),
                ('nickname', models.CharField(max_length=50, verbose_name='昵称')),
                ('sex', models.IntegerField(default=0, verbose_name='性别')),
                ('city', models.CharField(max_length=30, verbose_name='所在城市')),
                ('country', models.CharField(max_length=30, verbose_name='所在国家')),
                ('province', models.CharField(max_length=30, verbose_name='所在省份')),
                ('language', models.CharField(max_length=30, verbose_name='用户的语言')),
                ('head_img_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='用户头像URL')),
                ('remark', models.CharField(blank=True, max_length=50, null=True, verbose_name='公众号运营者对粉丝的备注')),
                ('union_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='微信平台唯一ID')),
                ('group_id', models.IntegerField(verbose_name='分组ID')),
                ('tag_id_list', models.CharField(max_length=200, verbose_name='标签List')),
                ('subscribe_time', models.DateTimeField(verbose_name='用户关注的时间')),
                ('subscribe_scene', models.CharField(max_length=50, verbose_name='用户关注的渠道来源')),
                ('qr_scene', models.IntegerField(verbose_name='二维码扫码场景')),
                ('qr_scene_str', models.CharField(max_length=100, verbose_name='二维码扫码场景描述')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('audience', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='audience.Audience')),
            ],
            options={
                'verbose_name': '微信用户',
                'unique_together': {('openid', 'audience')},
            },
        ),
    ]
