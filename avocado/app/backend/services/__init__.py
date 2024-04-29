from avocado.models import AsyncSession


class BaseService:
    def __init__(self, dbsession: AsyncSession) -> None:
        self._dbsession = dbsession

    @property
    def dbsession(self) -> AsyncSession:
        return self._dbsession
