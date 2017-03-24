from sqlalchemy import Column
from sqlalchemy import DateTime, func

from sqlalchemy.ext.declarative import declared_attr, declarative_base


class BaseModel(object):

    created_at = Column(DateTime, default=func.now())

    def create_or_update(self, data):
        '''Create new entity in database
        Args:
            data: values for new entity (dict)
        '''
        for value in data:
            if value in self.__table__.columns:
                setattr(self, value, data[value])

    def to_json(self, field):
        '''Represent data to json compacibility'''
        if field.name not in self.to_repr:
            return getattr(self, field.name)
        factory = self.to_repr.get(field, str)
        return factory(getattr(self, field.name))

    def as_dict(self):
        return {c.name: self.to_json(c) for c in self.__table__.columns}

    to_repr = {
        'created_at': str,
    }


Base = declarative_base(cls=BaseModel)
