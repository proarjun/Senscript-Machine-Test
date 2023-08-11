# Senscript-Machine-Test

The project is an application that performs CRUD operations to store, update and delete details of students and their marks for three subjects. The application is built using Django REST Framework.

 To deploy the application,run migrations and runserver in the cmd terminal and go to http://127.0.0.1:8000. 
 
 In the Browsable API View of the DRF, the user will be able to add new student credentials and view the list of students along with their marklist. 
 
 A pagination of three student credentials per page is given to the list view.

(Note: Always enter the id as integer/numerical only. Student_id will be automatically get updated as 'STD_id')

 The List View has a filter button with a search box for searching student credentials based on student id number, phone, email.

 To view, update or delete the student credentials, go to http://127.0.0.1:8000/(id)

 To add marklist to a new student, go to http://127.0.0.1:8000/marks/r<student id number>. Select the admission number and add the marks for three subjects. 

 To update or delete the marklist of a student, go to http://127.0.0.1:8000/marks/f<student id number>/update

 To view, update or delete the student credentials, go to http://127.0.0.1:8000/(id)

 To add marklist to a new student, go to http://127.0.0.1:8000/marks/(id). Select the admission number and add the marks for three subjects. 

 To update or delete the marklist of a student, go to http://127.0.0.1:8000/marks/(id)/update
 
 Django Admin Login Credentials
 ---------------------------------
 Username : admin
 Password : admin123
>>>>>>> 63cdf5fef63b16b5b002668b6dfdc92546b4c323

 Dependencies
 -------------
 django, djangorestframework

 (Note: The dependencies have also been listed in the Pipfile in the main directory.)
