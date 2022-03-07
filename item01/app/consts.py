# python自身是没有枚举类型的，在python3.4以后引入了枚举类型

from enum import Enum

class MessageType(Enum):
    info = 'info'
    warning = 'warning'
    error = 'error'
    danger = 'danger'

MessageType.info.label = '信息'
MessageType.warning.label = '警告'
MessageType.error.label = '错误'
MessageType.danger.label = '危险'

MessageType.info.color = 'green'
MessageType.warning.color = 'orange'
MessageType.error.color = 'gray'
MessageType.danger.color = 'red'