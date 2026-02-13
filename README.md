# Math app
Tietokannat ja web-ohjelmointi course

### Teaching app
My topic is an educational application from the example topics. The application provides online courses that teach mathematics. The courses include text material and exercises. Each user is a teacher or a student.

#### Features of the app:
- The user can log in and out and register as a user.
- The student can see a list of courses and can join courses.
- The student can read the text material of the course and solve the course exercises.
- The student can see the statistics of which course assignments he has solved.
- The teacher can create a new course, change existing courses and delete a course.
- The teacher can add text material and exercises to the course. The task can be at least multiple choice or a text field where you have to write the correct answer.
- The teacher can see the statistics of his course, which students are in the course and which course exercises each has solved.

### Status of the app
Structure of the app, the database, and register & login functions have been created. I haven't paid attention to the appearance yet.

### How to test
Clone this repository to your computer and go into its root directory.  

Create virtual environment:  
```python3 -m venv venv```  
Activate the virtual environment:    
```source venv/bin/activate```  
Install the app's dependencies with the commands:  
```pip install flask```  

Now you can run the app with the command ```flask run```


