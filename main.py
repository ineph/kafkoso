
import asyncio
from confluent_kafka import Consumer, TopicPartition

from creator import create
from consumer import consume
from producer import produce


async def main():
    await create()
    await produce()
    await consume()


if __name__ == "__main__":
    asyncio.run(main())
