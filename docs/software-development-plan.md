# Anemoment TriSonica Data Logging and Web GUI

## Software Architecture
<p align=center>
![](software-architecture/Software Architecture.png)
</p>
The software architecture is built around open-source database and web frameworks.  Data retreived from the Anemoment Trisonica tool will be loaded into a database.  The web framework will read data from that database, then serve web pages that generate interactive graphs from that data.  This results in a highly portable and maintainable software project that can easily add new features in future versions.

## Development Environment
Borg

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
