import secrets

from fastapi import HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import ShortLinkModel
from src.settings import APP_LINK_LENGTH


async def get_link(session: AsyncSession, short_link_id: str) -> str:
    stmt = select(ShortLinkModel.original_link).where(ShortLinkModel.id == short_link_id)
    result = await session.execute(stmt)
    result = result.scalar_one_or_none()

    if not result:
        raise HTTPException(
            status_code=404,
            detail='Link not found.',
        )
    return result


async def add_link(session: AsyncSession, original_link: str) -> str:
    stmt = select(ShortLinkModel.id).where(ShortLinkModel.original_link == original_link)
    result = await session.execute(stmt)
    result = result.scalar_one_or_none()

    if result:
        return result

    while True:
        short_link_id = secrets.token_urlsafe(APP_LINK_LENGTH)
        stmt = select(ShortLinkModel).where(ShortLinkModel.id == short_link_id)
        result = await session.execute(stmt)
        result = result.scalar_one_or_none()

        if not result:
            break

    stmt = (
        insert(ShortLinkModel)
        .values(
            id=short_link_id,
            original_link=original_link,
        )
        .returning(ShortLinkModel.id)
    )
    result = await session.execute(stmt)
    result = result.scalar_one()
    await session.commit()

    return result
