# Prometheus

## Install

Clone this repo, set up and activate a virtualenv and install the required python dependencies
```console
git clone https://github.com/vibhu-evs/prometheus.git
cd prometheus
python3 -m venv ev
source ev/bin/activate
pip install -r requirements/base.txt
```

## Create Database and Tables
```console
python create_db.py
```

## Run the server 
```console
make server
```

## Tests 
```console
make test 
```


## Check test coverage
```console
coverage run --source src manage.py test
coverage report -m
```