
# Trading application with python

This is a trading applications based on Microservice on top of Flask, with some useful packages like:

- [Flask](http://flask.pocoo.org/)
- [Flask-Injector](https://pypi.python.org/pypi/Flask-Injector)
- [Connexion](https://github.com/zalando/connexion)
- [Flask-swagger](https://pypi.org/project/flask-swagger/)

# Source Code Architecture

|Location                           |Description|
|-----------------------------------|-----------|
|__<app-name>/config.py__           |contains the application configuration parameters.|
|__instance/config.py__             |to configure local environment. Avoid to pushing to CVS production deployment branch|
|__<app-name>/models/<app-name>.py__|contains the definition of the application’s models.|
|__<app-name>/static/__             |contains the application’s static files.|
|__<app-name>/templates/__          |contains the application’s templates.|
|__<app-name>/views/<name>.py__     |contains the definition of the application’s routes and views. Application logic|
|__run.py__                         |This is the file that is invoked to start up a development server. It gets a copy of the app from your package and runs it. This won’t be used in production, but it will see a lot of mileage in development.|

# Requirements

We are going to build a microservice to index stock trading information coming from another service (crawler).
[comment]: <> ( Future we can analyze indexing the information into Elasticsearch instead of Mysql)

<mark>Work in progress=WIP</mark>

The indexing will be a process of:

- Validate and sanitize the data <mark>WIP</mark> 
- Get some metadata from the information like geolocalization, news, qualitative data of the company, etc <mark>WIP</mark> 
- Storage information <mark>WIP</mark> 
- Send an event to [RabbitMQ](https://www.rabbitmq.com/) every time a new company has been indexed serializing the 
  payload with Avro. <mark>NOT Started</mark> 

**Endpoints**:

|Method|URI|Description| Status |
|------|---|-----------|--------|
| POST | /scrap/most_active/<to_sql> | | **Development** |
| PATCH | /scrap/<name>/{id} | this PATCH method will allow us to make changes on the indexed item | Not started |
| DELETE | /scrap/<name>/{id} | this method will remove the id from the index | Not started |
| GET | /scrap/<name>/{id} | this method will return the room data for a given room id | Not started |
| GET | /scrap/health-check | This endpoint returns the state of the service | Not started |

# Running the environment


