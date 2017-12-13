from django.test import TestCase

user = 'vagrant'
pw_file = '/share/.mysql_user_pass'
with open(pw_file) as f:
    password = f.read().split()[0]
host = 'localhost'
port = 3306
db_name = 'anemomenttest'
