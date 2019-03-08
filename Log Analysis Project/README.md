# Log-Analysis
By Aminder Singh Sandhu.
### Project Overview
In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

### How to Run?

#### PreRequisites:
  * [Python](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download the data from Udasity.
  3. Unzip this file after downloading it. The file inside is called newsdata.sql.
  4. Copy the newsdata.sql file.

#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:

    $ vagrant up

  2. Then Log into this using command:

    $ vagrant ssh

  3. Change directory to /vagrant and look around with ls.

#### Setting up the database:

  1. Load the data in local database using the command:

    psql -d news -f newsdata.sql

  2. Use `psql -d news` to connect to database.

#### Running the queries:
  1. From the vagrant directory inside the virtual machine, run log_ana.py using:

    $ python log_ana.py
