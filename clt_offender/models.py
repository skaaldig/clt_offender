from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings


DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


class Offender():
    __tablename__ = "offender"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    alias = Column(String)
    dob = Column(Date)
    sex = Column(String)
    height_feet = Column(Integer)
    height_inches = Column(Integer)
    weight = Column(Integer)
    address = Column(Text)
    mugshot = Column(Text)
    arrests = relationship("Arrest")

    def __repr__(self):
        return f'<Offender: {self.name} - {self.sex} - {self.dob}>'


class Arrest():
    __tablename__ = "arrest"
    offender_id = Column(Integer, ForeignKey('offender.id'))
    arrest_number = Column(Integer, primary_key=True)
    # Combination of arrest date in time
    arrest_date = Column(DateTime)
    arrested_by = Column(Text)
    charges = relationship("Charge")

    def __repr__(self):
        return f'<Arrest: {self.arrest_number} - {self.arrest_date}>'


class Charge():
    __tablename__ = "charge"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    arrest_id = Column(Integer, ForeignKey('arrest.arrest_number'))
    description = Column(Text)
    bond_type = Column(String)
    bond_amount = Column(Float)
    case_number = Column(String)
    process = Column(String)
    magistrate_initials = Column(String)
    arrest_type = Column(String)
    record_id = Column(Integer)

    def __repr__(self):
        return f'<Charge: {self.arrest_id} - {self.description}>'