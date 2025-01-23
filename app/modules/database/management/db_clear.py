import asyncio

from sqlalchemy import delete, text

from ..connect import async_session
from ..core import Base
from ..seeders.all_seeds import all_seeds


async def remove_data_by_model_table(model):
    async with async_session() as session:
        # remove data.
        await session.execute(delete(model))

        # setup sequence value to start.
        if type(model) == type(Base):
            await session.execute(
                text(
                    "select setval('{}_id_seq', 1, false);".format(model.__tablename__)
                )
            )
        await session.commit()


async def main():
    for model, _, _ in all_seeds:
        await remove_data_by_model_table(model)


if __name__ == "__main__":
    asyncio.run(main())
