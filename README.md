# MentorshipPlatformAPI
This is a simple REST API built with Django and the Django REST framework for a mentorship platform. The API includes models for Mentor, Project, and Mentorship and allows creating, retrieving, and updating operations. The project also uses Docker to simplify deployment and development.

## Prerequisites
Before you begin, make sure you have the following installed:

- Docker
- Docker Compose

## Getting Started
To set up the project, follow these steps:

Clone the repository:
```bash
git clone https://github.com/alfonsomiralles/MentorshipPlatformAPI.git
```
Build the Docker images:
```bash
docker-compose build
```
Run the Docker containers:
```bash
docker-compose up -d
```
Perform the database migrations:
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```
## Now the API should be up and running at http://localhost:8000.

docker-compose exec web python manage.py createsuperuser

## API Endpoints
To acces admin panel
Create superuser
```bash
docker-compose exec web python manage.py createsuperuser
```
http://localhost:8000/admin

Access to some endpoints on your browser with Django REST framework
![image](https://user-images.githubusercontent.com/62959463/231559168-3459100f-513a-4916-a13c-4c0094af60d0.png)

![image](https://user-images.githubusercontent.com/62959463/231559335-542ed9bd-c74e-416c-a3fc-6cfb9fb7d4a7.png)

![image](https://user-images.githubusercontent.com/62959463/231559478-09eaf8fe-d4ec-4835-b688-604c57009867.png)

## The following endpoints are available:

GET /mentorship/mentors/: List all mentors

POST /mentorship/mentors/: Create a new mentor

GET /mentorship/mentors/:id/: Retrieve a specific mentor

PUT /mentorship/mentors/:id/: Update a specific mentor

PATCH /mentorship/mentors/:id/: Partially update a specific mentor

GET /mentorship/projects/: List all projects

POST /mentorship/projects/: Create a new project

GET /mentorship/projects/:id/: Retrieve a specific project

PUT /mentorship/projects/:id/: Update a specific project

PATCH /mentorship/projects/:id/: Partially update a specific project

GET /mentorship/mentorships/: List all mentorships

POST /mentorship/mentorships/: Create a new mentorship

GET /mentorship/mentorships/:id/: Retrieve a specific mentorship

PUT /mentorship/mentorships/:id/: Update a specific mentorship

PATCH /mentorship/mentorships/:id/: Partially update a specific mentorship
