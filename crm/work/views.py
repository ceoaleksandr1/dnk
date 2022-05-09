from accounts.models import User
from .models import Channel

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from services.channels import create_channel, change_channel, delete_channel


def main(req, page=None):
    """Главноя страница со всеми меню"""
    if req.user.is_authenticated:
        if page == 'manage':
            users = User.objects.all()
            return render(req, 'work/main.html', {'page': page, 'users': users})
        
        elif page == 'channels':
            channels = Channel.objects.all()
            return render(req, 'work/main.html', {'page': page, 'channels': channels})

    else:
        return redirect('login')


def staf(req, id=None):
    """Страница редактирования данных персонала"""
    messages = []
    if req.user.is_authenticated:
        user = User.objects.get(id=id)
        if user:
            if req.method == 'POST':
                data = req.POST.dict()

                if 'delete' in data:
                    user.delete()
                    return redirect('main', 'manage')

                user.name = data['name']
                user.phone = data['phone']
                user.manage = True if data['manage'] == 'true' else False
                user.user_manage = True if data['user_manage'] == 'true' else False
                user.chat_manage = True if data['chat_manage'] == 'true' else False
                user.channel_manage = True if data['channel_manage'] == 'true' else False
                user.save()
                messages.append('Изменения сохранены!')

            return render(req, 'work/staf.html', {'user': user, 'messages': messages})


def create_staf(req):
    """Создание персонала"""
    messages = []
    if req.method == 'POST':
        user = User()
        data = req.POST.dict()
        user.name = data['name']
        user.phone = data['phone']
        user.username = data['phone']
        user.manage = True if data['manage'] == 'true' else False
        user.user_manage = True if data['user_manage'] == 'true' else False
        user.chat_manage = True if data['chat_manage'] == 'true' else False
        user.channel_manage = True if data['channel_manage'] == 'true' else False
        user.password = make_password(data['psswd'])
        user.save()
        return redirect('staf', user.id)

    return render(req, 'work/createstaf.html', {'messages': messages})


def create_channel_view(req):
    """Создание канала"""
    if req.method == 'POST':
        data = req.POST.dict()
        channel = Channel()
        channel.name = data['name']
        channel.desc = data['desc']
        channel.link = data['username']
        channel.save()
        create_channel(namechannel=data['name'], descrchannel=data['desc'], linkchannel=data['username'])
        return redirect('channel', channel.id)

    return render(req, 'work/createchannel.html')


def channel_view(req, id):
    """Просмотр и редактирование канала"""
    channel = Channel.objects.get(id=id)

    if req.method == 'POST':
        data = req.POST.dict()

        if 'delete' in data:
            delete_channel(channel.link)
            channel.delete()
            return redirect('main', 'channels')
        else:
            channel.name = data['name']
            channel.save()
            change_channel(data['name'], channel.link)
            return render(req, 'work/channel.html', {'channel': channel})
    
    else:
        return render(req, 'work/channel.html', {'channel': channel})
