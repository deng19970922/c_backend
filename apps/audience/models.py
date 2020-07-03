from django.db import models

from const import AudienceSource, AudienceStatus, TargetAudienceStatus
from django.utils.translation import ugettext_lazy as _


class Audience(models.Model):
    name = models.CharField(_('数据源名称'), max_length=50)
    description = models.CharField(_('数据源描述'),
                                   max_length=200,
                                   null=True,
                                   blank=True)
    status = models.SmallIntegerField(_('状态'),
                                      default=AudienceStatus.ENABLE.value,
                                      choices=AudienceStatus.choice())
    source = models.SmallIntegerField(_('来源'),
                                      default=AudienceSource.OFFICIAL_ACCOUNT.value,
                                      choices=AudienceSource.choice())  # 文件导入，insight， 公众号
    # 更新频次

    brand = models.ForeignKey('brand.Brand', verbose_name=_('品牌'), on_delete=models.CASCADE)

    created = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated = models.DateTimeField(_('更新时间'), auto_now=True)

    class Meta:
        verbose_name = _('数据源')
        app_label = 'audience'


class WechatUsers(models.Model):
    # 公众号ID
    openid = models.CharField(_('用户的标识'), max_length=200, unique=True, primary_key=True)
    subscribe = models.IntegerField(_('是否关注公众号'), default=1)  # 为0时没有关注，不会拉取到以下信息
    nickname = models.CharField(_('昵称'), max_length=50)
    sex = models.IntegerField(_('性别'), default=0)  # 1为男性，2为女性，0为未知
    city = models.CharField(_('所在城市'), max_length=30)
    country = models.CharField(_('所在国家'), max_length=30)
    province = models.CharField(_('所在省份'), max_length=30)
    language = models.CharField(_('用户的语言'), max_length=30)
    head_img_url = models.CharField(_('用户头像URL'),
                                    max_length=200,
                                    null=True,
                                    blank=True)
    remark = models.CharField(_('公众号运营者对粉丝的备注'),
                              max_length=50,
                              null=True,
                              blank=True)
    union_id = models.CharField(_('微信平台唯一ID'), max_length=200, null=True, blank=True)
    group_id = models.IntegerField(_('分组ID'))
    tag_id_list = models.CharField(_('标签List'), max_length=200)
    subscribe_time = models.DateTimeField(_('用户关注的时间'))
    subscribe_scene = models.CharField(_('用户关注的渠道来源'), max_length=50)
    qr_scene = models.IntegerField(_('二维码扫码场景'))
    qr_scene_str = models.CharField(_('二维码扫码场景描述'), max_length=100)

    audience = models.OneToOneField(Audience, on_delete=models.CASCADE)

    created = models.DateTimeField(_("创建时间"), auto_now_add=True)
    updated = models.DateTimeField(_("更新时间"), auto_now=True)

    class Meta:
        verbose_name = _('微信用户')
        app_label = 'audience'
        unique_together = (('openid', "audience"),)


class TargetAudience(models.Model):
    name = models.CharField(_('目标受众名称'), max_length=50)
    rule = models.CharField(_('规则'), max_length=100)
    status = models.SmallIntegerField(_('状态'),
                                      default=TargetAudienceStatus.ENABLE.value,
                                      choices=TargetAudienceStatus.choice())
    # 更新频次

    audience = models.ForeignKey(Audience, verbose_name=_("数据源"), on_delete=models.CASCADE)

    created = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated = models.DateTimeField(_('更新时间'), auto_now=True)
