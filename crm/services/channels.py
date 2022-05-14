from telethon.sync import TelegramClient
from telethon.tl.functions.channels import CreateChannelRequest, CheckUsernameRequest, UpdateUsernameRequest, EditTitleRequest, DeleteChannelRequest
from telethon.tl.functions.messages import CreateChatRequest
from telethon.tl.types import InputPeerChannel

import asyncio


def create_channel(namechannel, descrchannel, linkchannel):
    """Создание канала"""
    client = _get_client()

    createdPrivateChannel = client(CreateChannelRequest(namechannel,descrchannel,megagroup=False))

    newChannelID = createdPrivateChannel.__dict__["chats"][0].__dict__["id"]
    newChannelAccessHash = createdPrivateChannel.__dict__["chats"][0].__dict__["access_hash"]
    desiredPublicUsername = linkchannel

    checkUsernameResult = client(CheckUsernameRequest(InputPeerChannel(channel_id=newChannelID, access_hash=newChannelAccessHash), desiredPublicUsername))
    if(checkUsernameResult==True):
        publicChannel = client(UpdateUsernameRequest(InputPeerChannel(channel_id=newChannelID, access_hash=newChannelAccessHash), desiredPublicUsername))


def change_channel(namechannel, username):
    """Редактирование канала"""
    client = _get_client()
    client(
        EditTitleRequest(
            channel=username,
            title=namechannel
        )
    )


def delete_channel(username):
    """Редактирование канала"""
    client = _get_client()
    client(
        DeleteChannelRequest(
            channel=username
        )
    )


def create_chat(title, users):
    """Создание чата"""
    client = _get_client()
    client(
        CreateChatRequest(
            users=users,
            title=title
        )
    )


def _get_client(): 
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    api_id=17780534
    api_hash='96fd2fa9cca58b34eafb5bd51ba342b2'
    name='TeleSender'

    client = TelegramClient(name, api_id, api_hash, loop=loop)
    client.start()

    return client
