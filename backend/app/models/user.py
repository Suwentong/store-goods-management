import enum

from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey, Boolean, func
from sqlalchemy.orm import relationship

from . import Base


class UserRole(enum.Enum):
    CASHIER = "CASHIER"
    WAREHOUSE = "WAREHOUSE"
    ADMIN = "ADMIN"


class UserStatus(enum.Enum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(Enum(UserRole))
    name = Column(String)
    phone_number = Column(String, nullable=False)
    status = Column(Enum(UserStatus), default=UserStatus.ACTIVE)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    sessions = relationship("SessionDB", back_populates="user")


class SessionDB(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    ip_address = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    last_active = Column(DateTime, server_default=func.now())
    is_active = Column(Boolean, default=True)

    user = relationship("UserDB", back_populates="sessions", lazy="selectin")
