import { useState } from "react";

const AppTest = () => {
  const [studentID, setStudentID] = useState("");
  const [studentName, setStudentName] = useState("");
  const [studentAge, setStudentAge] = useState("");
  const [studentEmail, setStudentEmail] = useState("");
  const [courseID, setCourseID] = useState("");
  const [courseName, setCourseName] = useState("");
  const [instructorID, setInstructorID] = useState("");
  const [instructorName, setInstructorName] = useState("");
  const [progress, setProgress] = useState("");

  const onRegister = async () => {
    const url = `${process.env.REACT_APP_BACKEND_URL}/students/register`;

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          student_id: studentID,
          student_name: studentName,
          student_age: studentAge,
          student_email: studentEmail,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Student registered successfully:", data);
    } catch (error: any) {
      console.error("Error during registration:", error.message);
    }
  };

  const getStudentInfo = async () => {
    const url = `${process.env.REACT_APP_BACKEND_URL}/students/info/${studentID}`;

    try {
      const response = await fetch(url, {
        method: "GET",
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Student data", data);
    } catch (error: any) {
      console.error("Error during registration:", error.message);
    }
  };

  const updateStudentInfo = async () => {
    const url = `${process.env.REACT_APP_BACKEND_URL}/students/update/${studentID}`;

    try {
      const response = await fetch(url, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          student_name: studentName,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Student registered successfully:", data);
    } catch (error: any) {
      console.error("Error during registration:", error.message);
    }
  };

  const addCourse = async () => {
    const url = `${process.env.REACT_APP_BACKEND_URL}/admin/courses`;

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          course_id: courseID,
          course_name: courseName,
          instructor_id: instructorID,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Course added:", data);
    } catch (error: any) {
      console.error("Error during registration:", error.message);
    }
  };

  const enrollInCourse = async () => {
    const url = `${process.env.REACT_APP_BACKEND_URL}/students/enroll/${studentID}/${courseID}`;

    try {
      const response = await fetch(url, {
        method: "GET",
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Enrolled ", data);
    } catch (error: any) {
      console.error("Error during registration:", error.message);
    }
  };

  const getStudentEnrolledCourses = async () => {
    const url = `${process.env.REACT_APP_BACKEND_URL}/students/courses/${studentID}`;

    try {
      const response = await fetch(url, {
        method: "GET",
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Enrolled ", data);
    } catch (error: any) {
      console.error("Error during registration:", error.message);
    }
  };

  const onInstructorRegister = async () => {
    const url = `${process.env.REACT_APP_BACKEND_URL}/instructors/register`;

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          instructor_id: instructorID,
          instructor_name: instructorName,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Instructor registered successfully:", data);
    } catch (error: any) {
      console.error("Error during registration:", error.message);
    }
  };

  const addStudentProgress = async () => {
    const url = `${process.env.REACT_APP_BACKEND_URL}/admin/courses/${studentID}/${courseID}`;

    try {
      const response = await fetch(url, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ progress }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Progress added successfully:", data);
    } catch (error: any) {
      console.error("Error during adding progress:", error.message);
    }
  };

  return (
    <main>
      <section>
        <input
          className="border border-black"
          placeholder="id"
          value={studentID}
          onChange={(e) => setStudentID(e.target.value)}
        />
        <input
          className="border border-black"
          placeholder="name"
          value={studentName}
          onChange={(e) => setStudentName(e.target.value)}
        />
        <input
          className="border border-black"
          placeholder="age"
          value={studentAge}
          onChange={(e) => setStudentAge(e.target.value)}
        />
        <input
          className="border border-black"
          placeholder="email"
          value={studentEmail}
          onChange={(e) => setStudentEmail(e.target.value)}
        />
        <button onClick={onRegister}>Register</button>
      </section>
      <section>
        <input
          className="border border-black"
          placeholder="id"
          value={studentID}
          onChange={(e) => setStudentID(e.target.value)}
        />
        <button onClick={getStudentInfo}>Get Info</button>
      </section>
      <section>
        <input
          className="border border-black"
          placeholder="id"
          value={studentID}
          onChange={(e) => setStudentID(e.target.value)}
        />
        <input
          className="border border-black"
          placeholder="name"
          value={studentName}
          onChange={(e) => setStudentName(e.target.value)}
        />
        <input
          className="border border-black"
          placeholder="age"
          value={studentAge}
          onChange={(e) => setStudentAge(e.target.value)}
        />
        <input
          className="border border-black"
          placeholder="email"
          value={studentEmail}
          onChange={(e) => setStudentEmail(e.target.value)}
        />
        <button onClick={updateStudentInfo}>Update Info</button>
      </section>
      <section>
        <input
          className="border border-black"
          placeholder="course-id"
          value={courseID}
          onChange={(e) => setCourseID(e.target.value)}
        />
        <input
          className="border border-black"
          placeholder="course-name"
          value={courseName}
          onChange={(e) => setCourseName(e.target.value)}
        />
        <input
          className="border border-black"
          placeholder="instructor-id"
          value={instructorID}
          onChange={(e) => setInstructorID(e.target.value)}
        />
        <button onClick={addCourse}>Add Course</button>
      </section>
      <section>
        <input
          className="border border-black"
          placeholder="id"
          value={studentID}
          onChange={(e) => setStudentID(e.target.value)}
        />
        <input
          className="border border-black"
          placeholder="course-id"
          value={courseID}
          onChange={(e) => setCourseID(e.target.value)}
        />
        <button onClick={enrollInCourse}>Enroll</button>
      </section>
      <section>
        <input
          className="border border-black"
          placeholder="id"
          value={studentID}
          onChange={(e) => setStudentID(e.target.value)}
        />
        <button onClick={getStudentEnrolledCourses}>Get Student Courses</button>
      </section>
      <section>
        <input
          className="border border-black"
          placeholder="instructor-id"
          value={instructorID}
          onChange={(e) => setInstructorID(e.target.value)}
        />
        <input
          className="border border-black"
          placeholder="instructor-name"
          value={instructorName}
          onChange={(e) => setInstructorName(e.target.value)}
        />
        <button onClick={onInstructorRegister}>Register</button>
      </section>
      <section>
        <input
          className="border border-black"
          placeholder="id"
          value={studentID}
          onChange={(e) => setStudentID(e.target.value)}
        />
        <input
          className="border border-black"
          placeholder="course-id"
          value={courseID}
          onChange={(e) => setCourseID(e.target.value)}
        />
        <input
          className="border border-black"
          placeholder="progress"
          value={progress}
          onChange={(e) => setProgress(e.target.value)}
        />
        <button onClick={addStudentProgress}>Add Progress</button>
      </section>
    </main>
  );
};

export default AppTest;
