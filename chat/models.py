from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Chat(models.Model):#o compo de username do usuário será capturado automaticamente quando logado
    sender = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='sender')
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='recipient',
    )
    message = models.TextField('Digite a sua mensagem ')
    subject = models.CharField('Título do Chat',max_length=255)
    created_at = models.DateTimeField('Criado em : ', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em : ', auto_now=True)

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

    def __str__(self):
        return self.subject

