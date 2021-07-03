from django.contrib.auth import get_user_model

User = get_user_model()
username = 'admin'
password = 'admin'

try:
    User.objects.get(username='admin')
    print ("User 'admin' already exist")
except User.DoesNotExist:
    User.objects.create_superuser(username, password)
    print ("User 'admin' created with default password")
