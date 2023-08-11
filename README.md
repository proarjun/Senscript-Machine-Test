# Senscript-Machine-Test

The project is an application that performs CRUD operations to store, update and delete details of students and their marks for three subjects. The application is built using Django REST Framework.

 To deploy the application,run migrations and runserver in the cmd terminal and go to http://127.0.0.1:8000. 
 
 In the Browsable API View of the DRF, the user will be able to add new student credentials and view the list of students along with their marklist. 
 
 A pagination of three student credentials per page is given to the list view.

(Note: Always enter the student id as integer/numerical only.)

 The List View has a filter button with a search box for searching student credentials based on student id number, phone, email.

 To view, update or delete the student credentials, go to http://127.0.0.1:8000/<student id number>

 To add marklist to a new student, go to http://127.0.0.1:8000/marks/<student id number>. Select the admission number and add the marks for three subjects. 

 To update or delete the marklist of a student, go to http://127.0.0.1:8000/marks/<student id number>/update


