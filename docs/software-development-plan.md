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

### MySQL
Borg already includes support for MySQL via [MariaDB](https://mariadb.org).  The setup scripts will port to the Raspberry Pi and accept Anemoment Trisonica data without issue.

### Django
[Django](https://www.djangoproject.com) is a

### Javascript
C3 and JSON

### Apache Webserver With mod_wsgi

### Web Browser

## Custom Software

### Anemoment Trisonica Data Parser

### Database Models

### Wind Data View

### Graph Webpage
