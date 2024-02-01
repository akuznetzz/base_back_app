# base_back_app

### Instalation requirements: 
Python version >= 3.12  
Package and dependency manager - PDM
Database - PostgreSQL

### Install steps
* Ensure that you have PDM installed
* Activate python 3.12. Recommended way - conda
* After cloning project come to `.src` dir and run `pdm install`
* Create DB and add credentials to `src/core/settings.py`

#### Migrate and run django project as usual

## To check after installation
* pre-commit 

### To tune later
* ruff linter
* ruff formater (using instead of black)