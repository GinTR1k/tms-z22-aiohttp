import logging
from asyncio import create_task

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from web.backgroud_jobs.alive_log_check import alive_log_check
from web.config import DATABASE_URL


logger = logging.getLogger(__name__)


async def setup_database(app):
    engine = create_async_engine(DATABASE_URL)
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    app['db'] = engine
    app['db_session'] = async_session


async def run_background_tasks(app):
    logger.info('Starting background tasks...')
    app['background_task'] = create_task(alive_log_check())
    logger.info('Started background tasks')
