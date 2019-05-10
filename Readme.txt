# Notes Document: "Python with Docker.pages"


# This is a test driven app. There is no UI for this app. It can be tested using Postman
# We don't have the list of API endpoints handy.

# Use the below command to run the tests.
docker-compose run app sh -c "python manage.py test && flake8"

# Run the API server
docker-compose up

# Access admin via browser http://localhost:8000/admin. The username is an email.
# username: admin@abc.com
# password: Admin123
