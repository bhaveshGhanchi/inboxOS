from sqlalchemy import (
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from datetime import datetime

from app.models.base import Base


class EmailAccount(Base):
    __tablename__ = "email_accounts"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    provider: Mapped[str] = mapped_column(
        String(50),
        default="google"
    )

    gmail_address: Mapped[str] = mapped_column(
        String(255)
    )

    access_token_encrypted: Mapped[str | None] = mapped_column(
        String(1000)
    )

    refresh_token_encrypted: Mapped[str | None] = mapped_column(
        String(1000)
    )

    token_expiry: Mapped[datetime | None] = mapped_column(
        DateTime
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    user = relationship("User")