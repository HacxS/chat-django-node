from rest_framework import serializers

from chat.models import Chat, Contact
from chat.views import get_user_contact


class ContactSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


'''class ChatSerializer(serializers.ModelSerializer):
    participants = ContactSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants')
        read_only = ('id')

    def create(self, validated_data):
        current_user = self.context['request'].user
        participants = validated_data.pop('participants')
        friends = ''
        for ii in participants:
            if current_user.username != ii:
                friends = ii
                break
        participants1=get_user_contact(current_user,friends=friends)
        participants2=get_user_contact(friends,friends=current_user)
        try:
            chat = None
            chat1 = Chat.objects.filter()
            chat2 = Chat.objects.filter()
            print(chat)
            if len(chat1)==1:
                chat = chat1
            else:
                chat = chat2
            return chat[0]
        except:
            chat = Chat()
            chat.save()
            #for username in participants:
            contact = get_user_contact(current_user,friends=friends)
            chat.participants.add(contact)
            chat.save()
        return chat

'''
class ChatSerializer(serializers.ModelSerializer):
    participants = ContactSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants')
        read_only = ('id')

    def create(self, validated_data):
        print(validated_data)
        participants = validated_data.pop('participants')
        chat = Chat()
        chat.save()
        for username in participants:
            contact = get_user_contact(username)
            chat.participants.add(contact)
        chat.save()
        return chat
# do in python shell to see how to serialize data

# from chat.models import Chat
# from chat.api.serializers import ChatSerializer
# chat = Chat.objects.get(id=1)
# s = ChatSerializer(instance=chat)
# s
# s.data
