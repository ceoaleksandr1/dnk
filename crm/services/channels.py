from telethon.sync import TelegramClient
from telethon.tl.functions.channels import CreateChannelRequest, CheckUsernameRequest, UpdateUsernameRequest, EditTitleRequest, DeleteChannelRequest
from telethon.tl.functions.messages import CreateChatRequest, SendMessageRequest, ExportChatInviteRequest
from telethon.tl.types import InputPeerChannel

import asyncio

from work.models import User_tg


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
    try:
        client = _get_client()
        id = client(
            CreateChatRequest(
                users=['Test_py_dnk_bot'],
                title=title
            )
        ).chats[0].id
        link = client(ExportChatInviteRequest(id)).link
        
        for el in users:
            try:
                user = User_tg.objects.get(phone = el)
                client.send_message(
                    'Test_py_dnk_bot',
                    f'/send {user.id} {link}'
                )

            except Exception as e:
                print(e)

    except:
        pass


# def delete_chat(title, users):
#     """Создание чата"""
#     client = _get_client()
#     client(
#         DeleteChatRequest(

#         )
#     )


def _get_client(): 
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    api_id=17780534
    api_hash='96fd2fa9cca58b34eafb5bd51ba342b2'
    name='TeleSender'

    client = TelegramClient(name, api_id, api_hash, loop=loop)
    client.start()

    return client
