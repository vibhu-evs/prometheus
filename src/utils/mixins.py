from uuid import UUID
from datetime import datetime

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy_utils.types.choice import Choice


class OutputMixin(object):
    RELATIONSHIPS_TO_DICT = False

    def __iter__(self):
        return self.to_dict().iteritems()

    def to_dict(self, rel=None, backref=None):
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
        res = {column.key: getattr(self, attr)
               for attr, column in self.__mapper__.c.items()}
        for key, value in res.items():
            if isinstance(value, datetime):
                res[key] = value.isoformat()
            if isinstance(value, UUID):
                res[key] =  str(value)
            if isinstance(value, Choice):
                res[key] =  str(value.value)
        if rel:
            for attr, relation in self.__mapper__.relationships.items():
                # Avoid recursive loop between to tables.
                if backref == relation.table:
                    continue
                value = getattr(self, attr)
                if value is None:
                    res[relation.key] = None
                elif isinstance(value.__class__, DeclarativeMeta):
                    res[relation.key] = value.to_dict(backref=self.__table__)
                else:
                    res[relation.key] = [i.to_dict(backref=self.__table__)
                                         for i in value]
        return res
