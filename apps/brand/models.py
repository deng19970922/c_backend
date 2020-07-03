from django.db import models

from const import BrandStatus
from django.utils.translation import ugettext as _


class Brand(models.Model):
    name = models.CharField(_("名称"), max_length=50, unique=True)
    status = models.SmallIntegerField(verbose_name=_("状态"), choices=BrandStatus.choice(),
                                      default=BrandStatus.ENABLE.value)
    description = models.CharField(_("描述"), max_length=200, null=True, blank=True)

    created = models.DateTimeField(_('创建时间'), auto_now_add=True)
    updated = models.DateTimeField(_('更新时间'), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("品牌")
        app_label = 'brand'
