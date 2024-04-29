from collections.abc import AsyncGenerator
from collections.abc import Callable

from fastapi import Depends

from avocado.app.backend.services import BaseService
from avocado.models import AsyncSession


async def get_dbsession() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession() as session:
        yield session


def get_service(
    service_type: type[BaseService],
) -> Callable[[AsyncSession], BaseService]:
    def _get_service(
        dbsession: AsyncSession = Depends(get_dbsession),
    ) -> BaseService:
        return service_type(dbsession)

    return _get_service
