import asyncio
import logging

logger = logging.getLogger('alive_log_check_file')


async def alive_log_check():
    while True:
        logger.debug('alive_log_check')
        await asyncio.sleep(3)
