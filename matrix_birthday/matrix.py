from nio import AsyncClient, MatrixRoom, RoomMessageText

from .config import ENV_DICT, MESSAGES


async def send_messages_from_file() -> None:
    client = AsyncClient(ENV_DICT["homeserver"], ENV_DICT["user_id"])

    print(await client.login(ENV_DICT["password"], device_name=ENV_DICT["device_name"]))
    # "Logged in as @alice:example.org device id: RANDOMDID"

    # If you made a new room and haven't joined as that user, you can use
    # await client.join("your-room-id")

    for message in MESSAGES:
        await client.room_send(
            **message
        )

    await client.close()
