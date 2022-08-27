# from curses.ascii import isdigit
# from django.core.management import BaseCommand
# from django.db import connections
# from django.db.utils import OperationalError
# import time
# from faker import Faker
from django.contrib.auth.models import User

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
# import random
# from sqlalchemy import create_engine, insert
# from sqlalchemy.orm import Session
# from django.utils import timezone
# from sqlalchemy.sql import text
# from multiprocessing.dummy import Pool as ThreadPool

# from sqlalchemy.orm import scoped_session
# from sqlalchemy.orm import sessionmaker


class Command(BaseCommand):
    # def f1(self, user):
    #     # now all calls to Session() will create a thread-local session.
    #     # If we call upon the Session registry a second time, we get back the same Session.
    #     session = self.Session()
    #     time = timezone.now()
    #     statement = "INSERT INTO users_user (username,first_name,last_name,password,email,phone_number,two_factor_authentication," \
    #                 "is_staff,is_active,is_superuser,date_joined,otp,phone_verified,created_by_merchant) VALUES ('{username}'," \
    #                 "'{first_name}','{last_name}','{password}','{email}','{phone_number}'," \
    #                 "false,true,true,false," + "'{}'".format(time) + ", '1111',false,false)"
    #     username = user.username
    #     if str(username).isdigit():
    #         phone_number = username
    #     else:
    #         phone_number = random.randint(10**(11-1), (10**11)-1)
    #     first_name = user.first_name
    #     last_name = user.last_name
    #     password = user.password
    #     if not password:
    #         user.set_password('1234')
    #         password = user.password

    #     email = user.email

    #     phone_number = phone_number

    #     try:
    #             if session.execute('select username from users_user where username="{}"'.format(username)).first():
                    
    #                 return
    #             session.execute(statement.format(
    #                 username=username.replace("'","\\'"), first_name=first_name.replace("'","\\'"), last_name=last_name.replace("'","\\'"), 
    #                 password=password.replace("'","\\'"), email=email.replace("'","\\'"), phone_number=phone_number.replace("'","\\'")))
    #             # trans.commit()
    #             session.commit()
                
                
    #     except Exception as e:
            
    #         return

    # def thread_worker(self, number):
    #     self.f1(number)
    # def work_parallel(self, numbers, thread_number=4):
    #     pool = ThreadPool(thread_number)
    #     results = pool.map(self.thread_worker, numbers)
    #     # If you don't care about the results, just comment the following 3 lines.
    #     # pool.close()
    #     # pool.join()
    #     # return results

    # def handle(self, *args, **options):
    #     print("start migrations script ...")
        
    #     engine = create_engine('mysql+pymysql://admin:-3U{faG#5fdeqr,M@sso-staging.cuwnpjk3aapl.ca-central-1.rds.amazonaws.com:3306/paymob_idms', pool_pre_ping=True)
    #     # conn = engine.connect()
    #     session_factory = sessionmaker(bind=engine)
    #     self.Session = scoped_session(session_factory)
    #     self.work_parallel( User.objects.all()[894000:], 8)
    #     print("enginee created ....")
    def handle(self, *args, **operations):
        self.stdout.write('query user db ')
        try:
            user = User.objects.all()
            print("user", user)
        except Exception as e:
            raise e
        

        self.stdout.write(self.style.SUCCESS(user))
        