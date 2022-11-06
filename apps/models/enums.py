from enum import Enum


class AbstractChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [
            (member.value[0], member.value[1]) for name, member, in cls.__members__.items()
        ]

    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]


class BooleanEnums(AbstractChoiceEnum):
    YES = ('y', 'Yes')
    NO = ('n', 'N')


class StatusEnum(AbstractChoiceEnum):
    ACTIVE = ('active', 'Active')
    EMPLOYED = ('employed', 'Employed')
    ARCHIVED = ('archived', 'Archived')


class JobTypeEnum(AbstractChoiceEnum):
    FULL_TIME = ('full-time', 'Full-Time')
    CONTRACT = ('contract', 'Contract')


class CategoryEnum(AbstractChoiceEnum):
    FULL_STACK = ('full-stack', 'Full-Stack Programming')
    FRONT_END = ('front-end', 'Front-End Programming')
    BACK_END = ('back-end', 'Back-End Programming')
    OTHER = ('other', 'Other')


class NotificationTypeEnum(AbstractChoiceEnum):
    MESSAGE = ('message', 'Message'),
    APPLICATION = ('application', 'Application')