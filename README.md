### Hexlet tests and linter status:
[![hexlet-check](https://github.com/volkov-timofey/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/volkov-timofey/python-project-52/actions/workflows/hexlet-check.yml)
[![Python CI](https://github.com/volkov-timofey/python-project-52/actions/workflows/pyci.yml/badge.svg)](https://github.com/volkov-timofey/python-project-52/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/15f3d73677bdedf49fd1/maintainability)](https://codeclimate.com/github/volkov-timofey/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/15f3d73677bdedf49fd1/test_coverage)](https://codeclimate.com/github/volkov-timofey/python-project-52/test_coverage)

### Information
Application "Task Manager" is a task management system similar to [redmine.org](http://www.redmine.org/). It allows you to set tasks, assign performers and change their statuses. To work with the system, registration and authentication are required.

### Demo application
[https://task-manager-xnt6.onrender.com/](https://task-manager-xnt6.onrender.com)

### Install

#### Prepare the database.

##### Before installing the application, prepare your environment variables:
* DATABASE_URL
    > For example: DATABASE_URL=postgresql://user:password@localhost:5432/mydb
* SECRET_KEY

#### Clone the repository and run application:
```bash
$ git clone https://github.com/volkov-timofey/Task_Manager.git
$ cd Task_Manager
$ make build
$ make start
```
