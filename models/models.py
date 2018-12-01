from enum import Enum
from datetime import datetime

# использовать в будущем (SQLAlchemy)

class UserRecord():
    id: int = None
    name: str = None
    url: str = None

class SensorRecord():
   id: str = None,
   address: str = None

class SensorUser():
  user_id: int = None,
  sensor_id: str = None,


class NotificationType(Enum):
    status_change = 'status_change'
    connection_status = 'connection_status'

class sensor_data_log():
  sensor_id: str = None,
  data: int = None,
  time: datetime = None

class notifications_log():
  type: NotificationType = None
  locked: bool = None,
  stable: bool = None
  address: str = None
  sensor_id: str = None,
  sensor_address: str = None,
  user_id: int = None,
  user_name: str = None,
  time: datetime = None
