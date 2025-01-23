import asyncio
from logging.config import fileConfig
from typing import Literal, MutableMapping

from alembic import context
from sqlalchemy import AdaptedConnection, Connection, pool
from sqlalchemy.ext.asyncio import async_engine_from_config

from modules.database.core import Base
from modules.database.models import *  # Import all models
from modules.envs.settings import settings

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", settings.database.link)
target_metadata = Base.metadata


def include_name(
    name: str | None,
    type_: Literal[
        "schema",
        "table",
        "column",
        "index",
        "unique_constraint",
        "foreign_key_constraint",
    ],
    _: MutableMapping[
        Literal["schema_name", "table_name", "schema_qualified_table_name"], str | None
    ],
) -> bool:
    if type_ == "table":
        return name not in ["spatial_ref_sys"]
    else:
        return True


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        include_name=include_name,
        include_schemas=False,
        render_as_batch=True,
    )

    with context.begin_transaction():
        if connection.dialect.name == "postgresql":
            context.execute("SET search_path TO public")
        # elif connection.dialect.name == 'sqlite':
        #     context.execute(
        #         "select iif((SELECT count(name) FROM sqlite_master WHERE type='table' AND name='spatial_ref_sys'),\
        #           0, InitSpatialMetadata(1))"
        #     )

        context.run_migrations()


async def load_extensions(connection: AdaptedConnection, _) -> None:
    await connection.driver_connection.enable_load_extension(True)


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


if context.is_offline_mode():
    print("Оффлайн миграции не поддерживаются")
else:
    asyncio.run(run_migrations_online())
