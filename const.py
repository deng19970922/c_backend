# encoding: utf-8
"""Define const variable in here"""
from enum import Enum as BaseEnum


class Enum(BaseEnum):
    @classmethod
    def choice(cls):
        return [(i.value, i.name) for i in cls]

    @classmethod
    def values(cls):
        return [i.value for i in cls]

    @classmethod
    def names(cls):
        return [i.name for i in cls]

    @classmethod
    def map(cls):
        return {i.name: i.value for i in cls}


class UserRole(Enum):
    """用户角色"""
    ROOT = 0
    ADMIN = 1
    MEMBER = 2


class UserGroupStatus(Enum):
    """用户组状态"""
    ACTIVE = 0
    DELETED = 1
    PAUSED = 2


class PermissionRole(Enum):
    """权限角色"""
    CREATOR = 0
    EXECUTOR = 1
    EDITOR = 2
    READER = 3


class BrandStatus(Enum):
    """品牌状态"""
    DISABLE = 0
    ENABLE = 1


class AudienceStatus(Enum):
    """数据源状态"""
    DISABLE = 0
    ENABLE = 1


class TargetAudienceStatus(Enum):
    """目标数据源状态"""
    DISABLE = 0
    ENABLE = 1


class ChannelType(Enum):
    """渠道类型"""
    SMS = 0
    Email = 1
    WeChat = 2


class AudienceSource(Enum):
    """数据源来源"""
    FILE_IMPORT = 0
    INSIGHT = 1
    OFFICIAL_ACCOUNT = 2


class CampaignStatus(Enum):
    """活动状态"""
    TEST = 0  # 测试
    PROCESSING = 1  # 进行中
    DEACTIVATE = 2  # 停用
    OVERDUE = 3  # 逾期


class JourneyCategory(Enum):
    """旅程分类"""
    START = 0  # 触发器
    QUERY = 1  # 过滤器
    FORK = 2  # 分流
    WAIT = 3  # 等待
    AUDIENCE = 4  # 人群
