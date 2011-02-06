#!/bin/bash
if [ -f login/settings-deploy.py ]
then
	mv login/settings.py login/settings-local.py
	mv login/settings-deploy.py login/settings.py
fi
./manage.py deploy
