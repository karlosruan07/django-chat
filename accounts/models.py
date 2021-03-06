
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Usuário', max_length=50,
    unique=True, help_text='Um nome curto que será usado para identificar de forma única você na plataforma')
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Equipe', default=False)#verifica se o usuário é ou não membro da equipe
    is_active = models.BooleanField('Ativo', default=True)#com isso podemos ativar ou desativar o usuario em vez de apagar a conta dele    
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)#captura a data e a hora do ultimo login
    phone = models.CharField('Telefone', max_length=11, unique=True)
    avatar = models.ImageField(upload_to='uploads/', blank=True)#esta pasta é criada automaticament.


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]

