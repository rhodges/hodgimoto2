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
python3 -m venv env
source env/bin/activate
python -m pip install --upgrade pip
pip install ./requirements.txt
```

### Install PostgreSQL and PostGIS


### Configure Django
cd /usr/local/apps/hodgimoto2/hodgimoto
cp template_local_settings.py local_settings.py
