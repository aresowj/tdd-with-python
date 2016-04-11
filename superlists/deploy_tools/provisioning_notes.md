Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virutalenv

## Nginx Virutal Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
|--sites
|--|--SITENAME
|----|--database
|----|--tdd-with-python
|------|--superlists
|----|--static
|----|--venv

