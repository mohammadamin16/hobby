from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """
    Creates and saves a User with the given email, date of
    birth and password.
    """

    def create_user(self, username, name, password=""):
        username = username
        password = password
        name = name
        user = self.model(
            username=username,
            password=password,
            name=name
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', default='No-Image')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'name']

    objects = UserManager()

    # Hobby Fields:
    watched_films = models.ManyToManyField('films.Film', blank=True, related_name='watched')
    fav_list      = models.ManyToManyField('films.Film', blank=True, related_name='fav')

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.writer.username + " : " + self.text[:20]

