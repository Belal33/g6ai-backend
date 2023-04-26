from django.contrib import admin
from .models import ChatBox,ChatMessage


# to make chatboxes accessible from user
class ChatBoxInline(admin.TabularInline):
  model = ChatBox
  extra=0
  
  def has_add_permission(self, request,obj):
    return False

  def has_change_permission(self, request, obj=None):
    return False


# to make chatmessages accessible from chatbox
class ChatMessageInline(admin.TabularInline):
  model = ChatMessage
  fk_name = "chatbox"
  extra=0
  def has_add_permission(self, request,obj):
    return False

  def has_change_permission(self, request, obj=None):
    return False


class ChatBoxAdmin(admin.ModelAdmin):
  model=ChatBox
  list_display = ('name', 'user', 'temperature', 'sys_message', 'created_at')
  search_fields = ('name', 'user__username')
  inlines = [ChatMessageInline]


class ChatMessageAdmin(admin.ModelAdmin):
  model=ChatMessage
  list_display = ( 
                  'user',
                  'chatbox',
                  'prompt_tokens',
                  'prompt_tokens',
                  'voice_message',
                  'finish_reason',
                  'created_at',
                )
  search_fields = ('chatbox__name', 'user__username')




  
admin.site.register(ChatMessage,ChatMessageAdmin)
admin.site.register(ChatBox,ChatBoxAdmin)