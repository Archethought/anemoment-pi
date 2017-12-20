# Anemoment TriSonica Data Logging and Web GUI

## Software Architecture
<p align=center>
![](software-architecture/Software Architecture.png)
</p>
The software architecture is built around open-source database and web frameworks.  Data retreived from the Anemoment Trisonica tool will be loaded into a database.  The web framework will read data from that database, then serve web pages that generate interactive graphs from the data.  This results in a highly portable and maintainable software project that can easily add new features in future versions.

## Development Environment
The software will be developed using the [borg](https://github.com/Syncroness-Inc/borg) project.  Borg is a set of libraries that allow provisioning of virtual machines via simple YAML-formatted configuration files.  This results in a development environment that is agnostic to the host OS, and the ability to deploy an RPi system image that is similarly provisioned from the configuration file.

The software will be written mostly in Python, with limited HTML and Javascript being required to generate web pages. Although the software project doesn't require a specific IDE for development, [PyCharm](https://www.jetbrains.com/pycharm/) is highly recommended.

## Required COTS

### UART Driver

The UART drivers are already built in to the Raspberry Pi.  No additional work is needed to retrieve raw data from the Anemoment Trisonica.

*Estimated Time to Implement: 0 Hours*

### MySQL
Borg already includes support for MySQL via [MariaDB](https://mariadb.org).  The setup scripts will port to the Raspberry Pi without issue.

*Estimated Time to Implement: 0 Hours*

### Django
[Django](https://www.djangoproject.com) is a web development framework built in Python.  While borg already includes support for Django, additional configuration is needed for deploying to a production web server.

*Estimated Time to Implement: 2 Hours*

### Javascript
JSON data will be delivered to a [C3](http://c3js.org)-based graph and rendered on a web browser.  Since modern web browsers support Javascript, no additional work is needed to bring up Javascript.

*Estimated Time to Implement: 0 Hours*

### Apache Webserver With mod_wsgi

### Web Browser

## Custom Software

### Anemoment Trisonica Data Parser

### Database Models

### Wind Data View

### Graph Webpage

## System Integration and Deployment
