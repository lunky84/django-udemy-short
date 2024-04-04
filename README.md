# django-udemy-short

### VSCode Devcontainer

```
devcontainer open
```

### Using Docker Compose

```
docker compose up
```

### Using the Dockerfile

Generate image

```
docker build -t meetups_image .
```

Run the container

```
docker run -d -p 8042:8041 --name meetups_container meetups_image
```

To view the site go to [http://localhost:8042/meetups/](http://localhost:8042/meetups/)

Administer the site via [http://localhost:8042/admin/](http://localhost:8042/admin/)

Example API endpoint [http://localhost:8042/api/locations/](http://localhost:8042/api/locations/)

### API responses

Example curl command

```
curl -v http://localhost:8042/api/locations/
```

Example httpie command

```
http GET http://localhost:8042/api/locations/
```

### Venv commands

Start venv virtual environment

```
source myworld/bin/activate
```

Intall dependencies

```
pip install -r requirements.txt
```

Change to project directory

```
cd django_course_site
```

Run server

```
python manage.py runserver
```

Close virtual environment

```
deactivate
```

### Useful Commands

See which python packages are installed

```
pip list
```

Generate a requirements.txt file containing the currently installed python packages

```
pip freeze > requirements.txt
```
