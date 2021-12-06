from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# create a new user
# create a superuser
class MyAccountManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Usuários devem ter endereço de email.")
        # if not username:
        #     raise ValueError("Usuários devem ter username.")

        user = self.model(
            email=self.normalize_email(email), 
            # username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            # username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'


def get_default_profile_image():
    return "media/logo_1080_1080.png"


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True, blank=True)
    first_name = models.CharField(verbose_name="Nome", max_length=30, unique=False)
    last_name = models.CharField(verbose_name="Sobrenome", max_length=30, unique=False)
    created_at = models.DateTimeField(verbose_name="Criado", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado", auto_now=True)
    is_active = models.BooleanField(verbose_name="Ativo", default=True)
    is_staff = models.BooleanField(verbose_name="Básico", default=False)
    is_admin = models.BooleanField(verbose_name="Administrador", default=False)
    is_superuser = models.BooleanField(verbose_name="Root", default=False)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin 

    def has_module_perms(self, app_label):
        return True
    
