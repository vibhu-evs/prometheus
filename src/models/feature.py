from sqlalchemy import (Column, Integer, String, Text, DateTime)
from sqlalchemy_utils.types.choice import ChoiceType
from sqlalchemy.ext.declarative import declarative_base
from src.utils import OutputMixin


Base = declarative_base()


class FeatureRequest(OutputMixin, Base):
    __tablename__ = 'feature_request'

    CLIENT_TYPES = [
        ('client a', 'Client A'),
        ('client b', 'Client B'),
        ('client c', 'Client C')
    ]

    PRODUCT_TYPES = [
        ('Policies', 'Policies'),
        ('Billing', 'Billing'),
        ('Claims', 'Claims'),
        ('Reports', 'Reports'),
    ]

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text(), nullable=False)
    priority = Column(Integer(), nullable=False)
    client = Column(ChoiceType(CLIENT_TYPES), nullable=False)
    product_area = Column(ChoiceType(PRODUCT_TYPES), nullable=False)
    target_date = Column(DateTime(), nullable=False)
