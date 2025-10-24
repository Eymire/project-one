from pydantic import BaseModel, HttpUrl


class Schema(BaseModel):
    id: int


class ShortLinkAddSchema(BaseModel):
    original_url: HttpUrl


class ShortLinkShowSchema(BaseModel):
    short_url: HttpUrl
