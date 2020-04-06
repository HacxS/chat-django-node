from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .models import Chat, Contact

User = get_user_model()


def get_last_10_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    return chat.messages.order_by('-timestamp').all()[:10]


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    try:
        inst = Contact.objects.get(user=user)
    except Exception as e:
        inst = Contact(user=user)
        inst.save()
    return inst


def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)


'''from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from .models import Chat, Contact

User = get_user_model()


def get_last_10_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    return chat.messages.order_by('-timestamp').all()[:10]


def get_user_contact(username,friends=None):
    user = get_object_or_404(User, username=username)
    if friends:
        friends = get_object_or_404(User, username=friends)
        inst = None
        try:
            inst1 = Contact.objects.filter(user=user,friends=friends)
            inst2 = Contact.objects.filter(user=friends,friends=user)
            if len(inst1)==1:
                inst = inst1[0]
            else:
                inst = inst2[0]
        except:
        	inst = Contact(user=user,friends=friends)
        	inst.save()
        return inst#get_object_or_404(Contact, user=user)
    else:
        inst1 = Contact.objects.filter(user=user)
        inst2 = Contact.objects.filter(friends=user)
        print(inst2,inst1)
        if len(inst1)==1:
            inst = inst1[0]
        else:
            inst = inst2[0]
        return inst


def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)
'''