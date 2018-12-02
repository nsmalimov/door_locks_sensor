create database door_lock_sensor;

CREATE TABLE USER_TABLE(
   ID SERIAL PRIMARY KEY    NOT NULL,
   URL           TEXT    UNIQUE  NOT NULL,
   NAME TEXT
);

CREATE TABLE SENSOR(
  ID TEXT PRIMARY KEY     NOT NULL,
  ADDRESS TEXT
);

CREATE TABLE SENSOR_USER(
  USER_ID INT REFERENCES USER_TABLE(id),
  SENSOR_ID TEXT REFERENCES SENSOR(id)
);

CREATE TYPE notification_type AS ENUM ('status_change','connection_status');

CREATE TABLE SENSOR_DATA_LOG(
  sensor_id TEXT REFERENCES SENSOR(id),
  sensor_data_data int,
  sensor_data_time TIMESTAMP
);

CREATE TABLE NOTIFICATION_LOG(
  notification_type notification_type,
  locked BOOLEAN,
  stable BOOLEAN,
  sensor_id TEXT REFERENCES SENSOR(id),
  user_id INT REFERENCES USER_TABLE(id),
  notification_time TIMESTAMP
);

