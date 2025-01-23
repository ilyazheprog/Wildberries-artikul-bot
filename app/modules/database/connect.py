from sqlalchemy import MetaData, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

from modules.envs import settings

engine = create_async_engine(
    settings.database.link, pool_size=100, max_overflow=0, echo=settings.database.echo
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
)

sync_engine = create_engine(settings.database.link, echo=settings.database.echo)
sync_session = sessionmaker(bind=sync_engine, expire_on_commit=False)


async def drop_all_async():
    """
    Асинхронное удаление всех таблиц из базы данных.
    """
    try:
        async with engine.begin() as conn:
            metadata = MetaData()
            metadata.reflect(bind=engine)
            await conn.run_sync(metadata.drop_all)
        print("Все таблицы успешно удалены (асинхронно).")
    except SQLAlchemyError as e:
        print(f"Ошибка при удалении таблиц (асинхронно): {e}")


def drop_all_sync():
    """
    Синхронное удаление всех таблиц из базы данных.
    """
    try:
        with sync_engine.connect() as conn:
            metadata = MetaData()
            metadata.reflect(bind=sync_engine)
            metadata.drop_all(bind=conn)
        print("Все таблицы успешно удалены (синхронно).")
    except SQLAlchemyError as e:
        print(f"Ошибка при удалении таблиц (синхронно): {e}")


async def get_async_session():
    async with async_session() as session:
        yield session
