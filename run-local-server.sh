#!/bin/bash
if [ -f login/settings-local.py ]
then
	mv login/settings.py login/settings-deploy.py
	mv login/settings-local.py login/settings.py
fi
python manage.py runserver 150.161.9.157:8000 #runserver 0.0.0.0:80
