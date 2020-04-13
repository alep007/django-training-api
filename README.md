[![Build Status](https://travis-ci.com/alep007/django-training-api.svg?branch=master)](https://travis-ci.com/alep007/django-training-api)

# django-training-api
Course from udemy to start working with Django


# creating django project
docker-compose run app sh -c "django-admin.py startproject app ."

# creating core-project
docker-compose run app sh -c "python manage.py startapp core"

# rebuilding docker with new dependencies
docker-compose build

# running test 
docker-compose run --rm app sh -c "python manage.py test && flake8"

# running migrations
docker-compose run app sh -c "python manage.py makemigrations core"

# create superuser
docker-compose run app sh -c "python manage.py createsuperuser"


# create a new module
docker-compose run --rm app sh -c "python manage.py startapp ___module_name"

