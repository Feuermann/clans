from app.models import Base
from sqlalchemy import Column
from sqlalchemy import Integer, String, Boolean, func
from sqlalchemy.ext.declarative import declarative_base


class UserProfile(Base):
    __tablename__ = 'userprofile'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    battles_total = Column(Integer, nullable=False, default=0)
    wins_total = Column(Integer, nullable=False, default=0)
    vehicles_x = Column(Integer, nullable=False, default=0)
    exp_total = Column(Integer, nullable=False, default=0)
    is_hidden = Column(Boolean, default=False)

    def __rerp__(self):
        return "User {}".format(self.name)

    def __str__(self):
        return "User {}".format(self.name)
