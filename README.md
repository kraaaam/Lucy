# Lucy
A microservice project that will follow the SAGA pattern


### Lucy
Lucy is a microservice project that follows the SAGA pattern. The project is designed to handle complex transactions across multiple services in a distributed system. The SAGA pattern is used to ensure that transactions are completed or rolled back in case of failures.

#### Getting Started
To get started with Lucy, you will need to have the following installed on your system:

- Python 3.6 or higher
- Docker
- Docker Compose

Once you have the prerequisites installed, you can clone the Lucy repository and run the following command to start the project:

```
docker-compose up
```

This will start all the services required for Lucy to run.

#### Architecture
Lucy is built using a microservices architecture. Each service is designed to handle a specific task and communicate with other services using REST APIs. The services are loosely coupled and can be scaled independently.

The following services are included in Lucy:

- Order Service: Handles the creation and management of orders.
- Payment Service: Handles payment processing for orders.
- Shipping Service: Handles shipping of orders.
- Notification Service: Sends notifications to customers about their orders.

##### SAGA Pattern
Lucy uses the SAGA pattern to manage transactions across multiple services. The SAGA pattern is a way to ensure that transactions are completed or rolled back in case of failures. In Lucy, each service is responsible for a specific part of the transaction. If a service fails, the SAGA pattern is used to roll back the transaction and ensure that all services are in a consistent state.

##### Contributing
If you would like to contribute to Lucy, please read the contributing guidelines for more information.

