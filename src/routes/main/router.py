from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from src.dependencies import session_dep
from src.schemas import ShortLinkAddSchema, ShortLinkShowSchema

from . import services


router = APIRouter()


@router.get('/{short_link_id}')
async def get_link(
    session: session_dep,
    short_link_id: str,
):
    result = await services.get_link(session, short_link_id)

    return RedirectResponse(result)


@router.post('/')
async def add_link(
    request: Request,
    session: session_dep,
    data: ShortLinkAddSchema,
) -> ShortLinkShowSchema:
    result = await services.add_link(session, str(data.original_url))

    return {'short_url': str(request.base_url) + result}  # type: ignore
