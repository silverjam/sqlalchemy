import uuid
from uuid import UUID as _py_uuid

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "test_table_user_uuid"
    id = Column(UUID(as_uuid=True), primary_key=True)


class Test(Base):
    __tablename__ = "test_table_uuid"

    id = Column(Integer, primary_key=True)
    ident = Column(UUID(as_uuid=True), ForeignKey("test_table_user_uuid.id"), index=True, nullable=False)


def test_1(u: uuid.UUID) -> None:
    Test(ident=u)


test_1(uuid.uuid4())
