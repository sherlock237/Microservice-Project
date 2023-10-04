## Designing Microservices Architecture with Django Framework


Content Service

title: CharField (max_length=255)
story: TextField
date_published: DateTimeField (auto_now_add=True)
User_id: IntegerField

User Interaction Service

user_id: IntegerField
content_id: IntegerField
interaction_type: CharField (max_length=4, choices=INTERACTION_TYPES, null=True)
created_at: DateTimeField (auto_now_add=True)

User Service
first_name: CharField (max_length=255)
last_name: CharField (max_length=255)
email_id: EmailField (unique=True)
phone_number: CharField (max_length=15)


### Architecture
*Mock Architecture*


https://drive.google.com/file/d/1-7fB8Qn4rMYq0V_xoYOdbdX-5cgb4R0Y/view?usp=sharing

### Tools

- Docker
- nginx
- MongoDB
- Django REST Framework

### Getting Started

- Clone this repository
- change directory where `docker-compose.yaml` within folder
- Build with `docker-compose build`
- After build completed, run `docker-compose up -d` or without detached flag `docker-compose up`
- Navigate to localhost, something like `0.0.0.0:8001` for `content service` API and so on
