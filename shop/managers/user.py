from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        tenant = kwargs.get('tenant')

        user = self.model(**{
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'tenant': tenant
        })
        user.set_password(password)
        user.save()
        return user
