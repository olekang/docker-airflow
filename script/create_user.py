#!/usr/bin/python
# -*- coding:utf-8 -*-

import getpass

import airflow
from airflow import models, settings
from airflow.contrib.auth.backends.password_auth import PasswordUser

IS_CORRECT = "Y"
HINT_THIS_SCRIPT = "\nhint!!\n==> YOU RUN THIS SCRIPT TO CREATE AIRFLOW USER NOW\n"
HINT_USER = "Please enter username you want to create: "
HINT_EMAIL_WITH_USER = "Please enter email for user `{username}`: "
HINT_PASSWORD_WITH_USER = "Please enter password for user `{username}`: "
HINT_CONFIRM_USER_PASSWORD = "\nhint!! > you want to add user `{username}` with email `{email}`\n" \
    "enter 'Y/y' to confirm the information\nor enter other key to reinput information\n>> "

user = PasswordUser(models.User())

while True:
    print(HINT_THIS_SCRIPT)
    user.username = input(HINT_USER)
    user.email = input(HINT_EMAIL_WITH_USER.format(username=user.username))
    user.password = getpass.getpass(HINT_PASSWORD_WITH_USER.format(username=user.username))
    correct = input(HINT_CONFIRM_USER_PASSWORD.format(username=user.username, email=user.email))

    if correct.strip().upper() == IS_CORRECT:
        break

session = settings.Session()
session.add(user)
session.commit()
session.close()
