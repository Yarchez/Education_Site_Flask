from sqlalchemy import MetaData, Table, Integer, Column, String, ForeignKey, Text, Boolean

metadata = MetaData()

topics = Table("topics", metadata,
               Column('id', Integer(), primary_key=True, nullable=False, unique=True),
               Column("text", String(100), default="Тема отсутсвует"),
               Column("position_in_exam", Integer(), default=0),
               )

levels = Table('levels', metadata,
               Column('id', Integer(), primary_key=True, nullable=False, unique=True),
               Column('text', String(100), default="Легкая"),
               )

tasks = Table('tasks', metadata,
              Column('id', String(4), primary_key=True, nullable=False, unique=True),
              Column("topic_id", ForeignKey("topics.id"), default=0),
              Column('level_id', ForeignKey('levels.id'), default=0),
              Column('text', Text(), default="Описание отсутствует"),
              Column('answer', String(100)),
              Column("is_image", Boolean(), default=False)
              )