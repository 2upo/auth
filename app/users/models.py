import uuid
from ..database import Database
from sqlalchemy import TIMESTAMP, Column, String, Boolean, text
from sqlalchemy.dialects.postgresql import UUID
from ..utils.base_model import CustomBaseModel

Base = Database().Base

#tests
class User(Base, CustomBaseModel):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    name = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    verified = Column(Boolean, nullable=False, server_default='False')
    role = Column(String, server_default='user', nullable=False)
    #remove server_default 
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    

    