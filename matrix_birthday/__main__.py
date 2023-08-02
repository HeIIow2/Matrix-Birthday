import asyncio

from .matrix import send_messages_from_file


def main():
    asyncio.run(send_messages_from_file())


main()
