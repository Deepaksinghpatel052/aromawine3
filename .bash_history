sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
sudo -u postgres psql
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
mkdir wine
cd wine
virtualenv wineenv
ls
source wineenv/bin/activate
pip install django gunicorn psycopg2-binary
django-admin.py startproject wineproject ~/wine
ls
cd wineproject/
ls
sudo nano settings.py 
cd ..
python manage.py makemigrations
python manage.py migrate
sudo ufw allow 8000
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow enable
sudo ufw enable
sudo ufw status
python manage.py runserver 0.0.0.0:8000
gunicorn --bind 0.0.0.0:8000 wineproject.wsgi
deactivate
sudo nano /etc/systemd/system/gunicorn.socket
sudo nano /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket
file /run/gunicorn.sock
curl --unix-socket /run/gunicorn.sock localhost
sudo systemctl status gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
sudo nano /etc/nginx/sites-available/wine
sudo ln -s /etc/nginx/sites-available/wine /etc/nginx/sites-enabled
sudo nginx -t
sudo nano /etc/nginx/sites-available/wine
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
cd ..
ls
sudo chmod -R 777 wine
ls
cd wine
ls
cd wine/
source wineenv/bin/activate
python manage.py migrate
pip install django-import-export
python manage.py migrate
pip install django-summernote
python manage.py migrate
pip install django-filter
python manage.py migrate
pip install Pillow
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
cd wine/
source wineenv/bin/activate
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
sudo systemctl restart gunicorn
sudo systemctl restart gunicorn
cd wine/
source wineenv/bin/activate
python manage.py makemigrations
python manage.pmigrate
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
sudo systemctl restart gunicorn
cd wine/
source wineenv/bin/activate
python manage.py makemigrations
python manage.py migrate
sudo systemctl restart gunicorn
cd wine/
source wineenv/bin/activate
python manage.py collectstatic
sudo systemctl restart gunicorn
python manage.py collectstatic
ls
cd ..
ls
cd wine/
python manage.py collectstatic
sudo systemctl restart gunicorn
python manage.py collectstatic
sudo systemctl restart gunicorn
cd wine/
source wineenv/bin/activate
python manage.py makemigrations
python manage.py migrate
sudo systemctl restart gunicorn
python manage.py runserver 0.0.0.0:8000
cd wine/
source wineenv/bin/activate
python manage.pu makemigrationa
python manage.py makemigrations
sudo systemctl restart gunicorn
python manage.py makemigrations
cd wine/
source wineenv/bin/activate
python manage.py makemigrations
2
python manage.py makemigrations
python manage.py migrate
sudo systemctl restart gunicorn
cd wine/
source wineenv/bin/activate
python manage.py runserver 0.0.0.0:8000
sudo fuser -k 8000/tcp
python manage.py runserver 0.0.0.0:8000
sudo systemctl restart gunicorn
cd wine/
source wineenv/bin/activate
python manage.py runserver 0.0.0.0:8000
sudo systemctl restart gunicorn
sudo systemctl restart gunicorn
cd wine/
source wineenv/bin/activate
python manage.py makemigrations
python manage.pymigrate
python manage.py migrate
sudo systemctl restart gunicorn
python manage.py makemigrations
python manage.py migrate
sudo systemctl restart gunicorn
cd wine
source wineenv/bin/activate
python manage.py makemigrations
python manage.py migrate
sudo systemctl restart gunicorn
python manage.py makemigrations
python manage.py migrate
sudo systemctl restart gunicorn
cd wine
source wineenv/bin/activate
python manage.py makemigrations
python manage.pymigrate
python manage.py migrqate
python manage.py migrate
sudo systemctl restart gunicorn
python manage.py makemigrations
python manage.py migrate
sudo systemctl restart gunicorn
cd wine
source wineenv/bin/activate
python manage.py makemigrations
python manage.py migrate
sudo systemctl restart gunicorn
cd wine
source wineenv/bin/activate
python manage.py makemigrations
python manage.py migrate
sudo systemctl restart gunicorn
sudo systemctl restart gunicorn
cd wine
sudo systemctl restart gunicorn
sudo systemctl restart gunicorn
cd wine/
source wineenv/bin/activate
python manage.py startapp account
sudo systemctl restart gunicorn
cd wne
cd wine/
source wineenv/bin/activate
python manage.py startapp dashboard_user
sudo systemctl restart gunicorn
cd wine/
source wineenv/bin/activate
python manage.py collectstatic
sudo systemctl restart gunicorn
cd wine/
source wineenv/bin/activate

sudo systemctl restart gunicorn
pip install djangorestframework
sudo systemctl restart gunicorn
cd wine/
git init
git add -A
