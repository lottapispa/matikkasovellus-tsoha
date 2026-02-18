# Math app
Tietokannat ja web-ohjelmointi course

### Teaching app
My topic is an educational application from the old example topics. The application provides online courses that teach mathematics. The courses include text material, exercises and statistics. Each user is a teacher or a student.  

#### Goal features of the app:
- The user can log in and out and register as a user.
- The student can see a list of courses and can join courses.
- The student can read the text material of the course and solve the course exercises.
- The student can see the statistics of which course assignments he has solved.
- The teacher can create a new course, change existing courses and delete a course.
- The teacher can add text material and exercises to the course. The task can be at least multiple choice or a text field where you have to write the correct answer.
- The teacher can see the statistics of his course, which students are in the course and which course exercises each has solved.

### Status of the app
The base structure of the app and the database have been created. Register & login features have been implemented at working level. A CSS file has been made to add some styling to the web application.  Styling works on Chrome, not sure about other browsers yet.  

### How to use
Clone this repository to your computer and go into its root directory.  

Create a virtual environment:  
```python3 -m venv venv```  
Activate the virtual environment:    
```source venv/bin/activate```  
Install the app's dependencies:  
```pip install flask```  
Run the app:  
```flask run```  
Exit the virtual environment:  
```deactivate```  

