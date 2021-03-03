# Tips Calculator

## General Information:
Basic Django website, using Bootstrap as a front-end, built to host a Python script.
Takes the Excel export of scheduled/worked hours of a popular Dutch staff scheduling platform as a file input.
Outputs the amount of tips and hours worked per employee per department.

## Demo:
![Demo](/media//DEMO.gif)

## Project Summary:
Built as a favour for a friend who runs a restaurant.
Automates the task of calculating the distribution of tips among employees on a weekly basis, based on the amount of hours they have worked and their respective department. The results are displayed using Django-Tables, and are stored in a database (PostgreSQL). Additionally, the results can be exported to an Excel file in order to be downloaded. The website has basic user authentication (login, registration, password reset, etc) using the built-in features of Django. Furthermore, the website contains basic user profile functionality, and automatic testing using the standard unittest module.

## Technologies:
Project created with Python 3.8. Packages used:
* Django
* Django-tables
* Isoweek
* Openpyxl
* Pandas
* Xlrd

Note: In order to parse Excel files, the Pandas module uses Xlrd. However, Xlrd has an issue parsing some older Excel formats (.xls). Hence, a forked version of Xlrd is used to circumvent the issue. 