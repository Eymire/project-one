from re import sub as re_sub

from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(self) -> str:
        temp = re_sub('(.)([A-Z][a-z]+)', r'\1-\2', self.__name__[:-5])
        result = re_sub('([a-z0-9])([A-Z])', r'\1-\2', temp).lower() + 's'

        return result

    id: Mapped[int] = mapped_column(primary_key=True)
