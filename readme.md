# Installation de Hello Dynalogic

## Installations préalables:
Ce site requiert python 3.6:

* S'assurer que cette version de python soit installée en local :

``` 
python -V
```
* Sinon l'installer

```
sudo apt-get update
sudo apt-get install python3.6
```

Pour les versions antérieures à Ubuntu 16.10 ajouter le dépôt ([Doc](http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/))

```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
```


Nous aurons besoin d'avoir dans notre environnement de travail : pip et pipenv déjà installés:

* Pour s'assurer que pip est installé, dans un shell,  taper 

```
 pip3 --version
```

* Installer pip3 pour la version python3.6

```
curl https://bootstrap.pypa.io/get-pip.py | sudo -H python3.6
```

* Verifier

```
python3.6 -m pip -V
pip 19.0.3 from /usr/local/lib/python3.6/dist-packages/pip (python 3.6)
```

* Installer pipenv

``` 
pip3 install --user pipenv
```

* Se positionner dans le dossier choisi

```
cd /tmp
git clone https://github.com/horlas/hello_Dynalogic.git
cd hello_Dynalogic

```

* Installer et activer l'environnement virtuel , lancer l'application en local

```
pipenv install
pipenv shell
python manage.py runserver
```

