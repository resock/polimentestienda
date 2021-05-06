from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombres, apellidos, username, password=None):
        if not email:
            raise ValueError('Deben de ingresar un correo electronico')
        usuario = self.model(
            nombres = nombres,
            apellidos = apellidos,
            username=username,
            email=self.normalize_email(email)
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, nombres, apellidos, username, email, password):
        usuario = self.create_user(
            email,
            nombres = nombres,
            apellidos = apellidos,
            username=username,
            password=password
        )
        usuario.usuario_staff = True
        usuario.usuario_admin = True
        usuario.save(using=self._db)
        return usuario

    def create_staffuser(self, nombres, apellidos, username, email, password):
        usuario = self.create_user(
            email,
            nombres=nombres,
            apellidos=apellidos,
            username=username,
            password=password
        )
        usuario.usuario_staff = True
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser):#
    id = models.AutoField(primary_key = True)
    nombres= models.CharField(max_length= 50 )
    apellidos = models.CharField(max_length= 50)
    username = models.CharField(max_length= 50, unique = True)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    usuario_staff = models.BooleanField(default= False)
    usuario_admin = models.BooleanField(default= False)
    usuario_activo = models.BooleanField(default = True)


    Objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres', 'apellidos']

class Meta():
    verbose_name = 'usuario'
    verbose_name_plural = 'usuarios'

    def get_full_name(self):
        return self.nombres + '' +self.apellidos

    def get_short_name(self):
        return self.nombres

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.usuario_staff

    @property
    def is_admin(self):
        return self.usuario_admin

    @property
    def is_active(self):
        return self.usuario_activo

    def __str__(self):
        return self.nombres + ' ' + self.apellidos + ''+ self.email


