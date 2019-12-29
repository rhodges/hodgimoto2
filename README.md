# hodgimoto2
New Hodgimoto site: django3

## Installation

### Recommended Stack
* Ubuntu 18.04 LTS
* Python 3.x

### Create Workspace
```
cd /usr/local/
sudo mkdir apps
sudo chown {USERNAME} ./apps
cd apps
git clone https://github.com/rhodges/hodgimoto2.git
cd hodgimoto2
```

### Set Up Venv & Install Django/Requirements
```
sudo apt install python3-venv
cd /usr/local/apps/hodgimoto2/
python3 -m venv env
source env/bin/activate
python -m pip install --upgrade pip
pip install -r ./requirements.txt
```

### Install PostgreSQL and PostGIS
Below you will create a username and password for a database user, seen in the commands below as {DBUSER}.
For development installs you can skip this user-creation step and leave the `-O {DBUSER}` out of the createdb command.
```
sudo apt install postgresql-10 postgresql-10-postgis-2.4 postgresql-server-dev-10 python-psycopg2 -y
sudo -u postgres createuser -s -P {DBUSER}
sudo -u postgres createdb -O {DBUSER} hodgimoto
sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" hodgimoto
sudo vim /etc/postgresql/10/main/pg_hba.conf
```
**IF PRODUCTION INSTALL**:
If you created a {DBUSER} and assigned them as the DB owner (as above) then update pg_hba.conf 'Authentication' section as follows:
```
host    hodgimoto           {DBUSER}                                md5
```
Also update `/usr/local/apps/hodgimoto2/hodgimoto/local_settings.py` in the `DATABASES` section:
```
  'USER': '{DBUSER}',
  'PASSWORD': '{DBPASSWORD}',
```
**IF DEVELOPMENT INSTALL**:
If, however, you're on a develpment instance, you only need to update pg_hba.conf by changing postgres's settings from 'peer' to 'trust':
```
local   all             postgres                                trust
```

**EITHER WAY**: 
Restart postgreSQL.
```
sudo service postgresql restart
```

### Configure Django and perform initial DB Migration
```
cd /usr/local/apps/hodgimoto2/hodgimoto
cp template_local_settings.py local_settings.py
python /usr/local/apps/hodgimoto2/manage.py migrate
```
 
