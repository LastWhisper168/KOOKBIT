"""type enums"""
from enum import IntEnum, Enum
from typing import Dict, Any


class MessageTypes(IntEnum):
    """
    消息类型，type==SYS 将被解释为 `Event`，其他的为 `Message`
    """
    TEXT = 1     # 普通文本消息
    IMG = 2      # 图片消息
    VIDEO = 3    # 视频消息
    FILE = 4     # 文件消息
    AUDIO = 8    # 音频消息
    KMD = 9      # KMarkdown 消息
    CARD = 10    # 卡片消息
    SYS = 255    # 系统消息（事件类型）


class ChannelTypes(IntEnum):
    """
    频道类型
    """
    CATEGORY = 0  # 频道分类
    TEXT = 1      # 文字频道
    VOICE = 2     # 语音频道


class ChannelPrivacyTypes(Enum):
    """
    频道隐私类型
    """
    GROUP = 'GROUP'   # 群组频道
    PERSON = 'PERSON' # 私人频道


class EventTypes(Enum):
    """
    系统事件类型（type == 255）
    """
    MESSAGE_BTN_CLICK = 'message_btn_click'  # 消息按钮点击事件
    ADDED_REACTION = 'added_reaction'       # 添加反应表情事件
    DELETED_REACTION = 'deleted_reaction'   # 删除反应表情事件
    UPDATED_MESSAGE = 'updated_message'     # 更新消息事件
    DELETED_MESSAGE = 'deleted_message'     # 删除消息事件
    MESSAGE_UPDATED = 'message_updated'     # 消息已更新事件
    DELETED_MESSAGE = 'deleted_message'     # 消息被删除事件

    PRIVATE_ADDED_REACTION = 'private_added_reaction'   # 私人反应表情添加事件
    PRIVATE_DELETED_REACTION = 'private_deleted_reaction'  # 私人反应表情删除事件
    UPDATED_PRIVATE_MESSAGE = 'updated_private_message'  # 更新私人消息事件
    DELETED_PRIVATE_MESSAGE = 'deleted_private_message'  # 删除私人消息事件

    UPDATED_GUILD = 'updated_guild'  # 更新公会事件
    DELETED_GUILD = 'deleted_guild'  # 删除公会事件
    ADDED_BLOCK_LIST = 'added_block_list'  # 添加封锁列表
    DELETED_BLOCK_LIST = 'deleted_block_list'  # 删除封锁列表

    ADDED_ROLE = 'added_role'  # 添加角色事件
    DELETED_ROLE = 'deleted_role'  # 删除角色事件
    UPDATED_ROLE = 'updated_role'  # 更新角色事件

    JOINED_GUILD = 'joined_guild'  # 加入公会事件
    EXITED_GUILD = 'exited_guild'  # 退出公会事件
    GUILD_MEMBER_ONLINE = 'guild_member_online'  # 公会成员在线事件
    GUILD_MEMBER_OFFLINE = 'guild_member_offline'  # 公会成员离线事件

    UPDATED_GUILD_MEMBER = 'updated_guild_member'  # 更新公会成员信息事件

    UPDATED_CHANNEL = 'updated_channel'  # 更新频道事件
    ADDED_CHANNEL = 'added_channel'  # 添加频道事件
    DELETED_CHANNEL = 'deleted_channel'  # 删除频道事件

    JOINED_CHANNEL = 'joined_channel'  # 加入频道事件
    EXITED_CHANNEL = 'exited_channel'  # 退出频道事件
    USER_UPDATED = 'user_updated'  # 用户信息更新事件
    SELF_JOINED_GUILD = 'self_joined_guild'  # 机器人自己加入公会事件
    SELF_EXITED_GUILD = 'self_exited_guild'  # 机器人自己退出公会事件

    PINNED_MESSAGE = 'pinned_message'  # 固定消息事件
    UNPINNED_MESSAGE = 'unpinned_message'  # 取消固定消息事件

    ADDED_EMOJI = 'added_emoji'  # 添加表情事件
    DELETED_EMOJI = 'deleted_emoji'  # 删除表情事件
    UPDATED_EMOJI = 'updated_emoji'  # 更新表情事件


class GuildMuteTypes(IntEnum):
    """
    公会禁言类型
    """
    MIC = 1    # 禁言麦克风
    HEADSET = 2  # 禁言耳机


class SlowModeTypes(IntEnum):
    """
    慢速模式类型（单位：毫秒）
    """
    FIVE_SEC = 5000      # 5秒
    TEN_SEC = 10000      # 10秒
    FIFTEEN_SEC = 15000  # 15秒
    THIRTY_SEC = 30000   # 30秒
    ONE_MIN = 60000      # 1分钟
    TWO_MIN = 120000     # 2分钟
    FIVE_MIN = 300000    # 5分钟
    TEN_MIN = 600000     # 10分钟
    FIFTEEN_MIN = 900000 # 15分钟
    THIRTY_MIN = 1800000 # 30分钟
    ONE_HOUR = 3600000   # 1小时
    TWO_HOUR = 7200000   # 2小时
    SIX_HOUR = 21600000  # 6小时

    @classmethod
    def possible_value(cls) -> Dict[Any, Enum]:
        """返回所有枚举名称和值的字典"""
        return cls._value2member_map_  # pylint: disable=no-member


class RoleTypes(IntEnum):
    """
    角色类型
    """
    UserCreated = 0   # 用户创建的角色
    BotSpecified = 1  # 机器人指定的角色
    Booster = 2       # 提升者角色
    Everyone = 255    # 每个人角色


class SoftwareTypes(Enum):
    """用于收听音乐的软件类型"""
    CLOUD_MUSIC = "cloudmusic"  # 云音乐
    QQ_MUSIC = "qqmusic"        # QQ音乐
    KUGOU_MUSIC = "kugou"       # 酷狗音乐


class BadgeTypes(IntEnum):
    """公会徽章类型"""
    NAME = 0       # 名称徽章
    ONLINE = 1     # 在线徽章
    ONLINE_MAX = 2 # 最大在线徽章


class MessageFlagModes(Enum):
    """消息标志模式类型"""
    BEFORE = 'before'  # 消息在前
    AFTER = 'after'    # 消息在后
    AROUND = 'around'  # 消息在周围


class GameTypes(Enum):
    """游戏类型"""
    ALL = '0'            # 所有游戏
    USER_CREATED = '1'   # 用户创建的游戏
    SYSTEM_CREATED = '2' # 系统创建的游戏


class FriendTypes(Enum):
    """朋友类型"""
    REQUEST = "request"  # 朋友请求
    FRIEND = "friend"    # 朋友
    BLOCKED = "blocked"  # 被屏蔽的朋友
