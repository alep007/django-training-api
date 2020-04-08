# django-training-api
Course from udemy to start working with Django


# creating django project
docker-compose run app sh -c "django-admin.py startproject app ."

# rebuilding docker with new dependencies
docker-compose build

# running test 
docker-compose run app sh -c "python manage.py test && flake8"