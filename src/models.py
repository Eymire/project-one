from datetime import datetime

from sqlalchemy import DateTime, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.settings import APP_LINK_TTL_DAYS


class Base(DeclarativeBase):
    id: Mapped[str] = mapped_column(primary_key=True)


class ShortLinkModel(Base):
    __tablename__ = 'short-links'

    original_link: Mapped[str]
    ends_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text(f"CURRENT_TIMESTAMP + interval '{APP_LINK_TTL_DAYS} days'"),
    )
