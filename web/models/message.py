from datetime import datetime
from uuid import uuid4

import sqlalchemy as sa

from web.models import Base


class Message(Base):
    __tablename__ = 'messages'
    id = sa.Column(sa.String(36), primary_key=True, default=lambda: str(uuid4()))
    created_at = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    text = sa.Column(sa.String(1024), nullable=False)
    username = sa.Column(sa.String(32), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'text': self.text,
            'username': self.username,
        }
