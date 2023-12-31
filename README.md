## Designing Microservices Architecture with Django Framework


*User Service*
This service is responsible for managing user data. It provides APIs for creating, listing, and updating user data.

*Content Service*
This service manages the content data. It provides APIs for creating, listing, updating, and deleting content. It also provides APIs for sorting content by date and ingesting CSV data.

*User Interaction Service*
This service manages user interactions with the content. It provides APIs for creating and updating user interactions. It also provides APIs for getting top content based on ‘READ’ and ‘LIKE’ interactions.


### Architecture
*Mock Architecture*
https://drive.google.com/file/d/1J-qqEABcFvhZz3LkiWhT83dec-uGQwiL/view?usp=sharing


![image](https://drive.google.com/file/d/1J-qqEABcFvhZz3LkiWhT83dec-uGQwiL/view?usp=sharing)

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

### Documentation
https://docs.google.com/document/d/1xPzc4tSEKCYew1s1Rof5pzo33zqxpBWaRA0To5pjEsw/edit?usp=sharing
