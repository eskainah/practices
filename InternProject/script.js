// Arrays to store data
let students = [];
let teachers = [];
let courses = [];

// Function to add a student
function addStudent() {
  const studentName = document.getElementById("studentName").value;
  if (studentName) {
    students.push(studentName);
    document.getElementById("studentName").value = "";
    displayStudents();
  }
}

// Function to add a teacher
function addTeacher() {
  const teacherName = document.getElementById("teacherName").value;
  if (teacherName) {
    teachers.push(teacherName);
    document.getElementById("teacherName").value = "";
    displayTeachers();
  }
}

// Function to add a course
function addCourse() {
  const courseName = document.getElementById("courseName").value;
  if (courseName) {
    courses.push(courseName);
    document.getElementById("courseName").value = "";
    displayCourses();
  }
}

// Function to display students
function displayStudents() {
  const studentList = document.getElementById("studentList");
  studentList.innerHTML = students.map((student, index) => `
    <li>${student} <button onclick="removeStudent(${index})">Remove</button></li>
  `).join("");
}

// Function to display teachers
function displayTeachers() {
  const teacherList = document.getElementById("teacherList");
  teacherList.innerHTML = teachers.map((teacher, index) => `
    <li>${teacher} <button onclick="removeTeacher(${index})">Remove</button></li>
  `).join("");
}

// Function to display courses
function displayCourses() {
  const courseList = document.getElementById("courseList");
  courseList.innerHTML = courses.map((course, index) => `
    <li>${course} <button onclick="removeCourse(${index})">Remove</button></li>
  `).join("");
}

// Function to remove a student
function removeStudent(index) {
  students.splice(index, 1);
  displayStudents();
}

// Function to remove a teacher
function removeTeacher(index) {
  teachers.splice(index, 1);
  displayTeachers();
}

// Function to remove a course
function removeCourse(index) {
  courses.splice(index, 1);
  displayCourses();
}
