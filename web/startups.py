from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from web.config import DATABASE_URL


async def setup_database(app):
    engine = create_async_engine(DATABASE_URL)
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    app['db'] = engine
    app['db_session'] = async_session
