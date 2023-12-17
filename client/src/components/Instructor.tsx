import { useEffect, useState } from "react";

const Instructor = () => {
  const [courses, setCourses] = useState<any[]>([]);
  const [myCourses, setMyCourses] = useState<any[]>([]);

  useEffect(() => {
    (async () => {
      const url = `${process.env.REACT_APP_BACKEND_URL}/admin/courses`;

      try {
        const response = await fetch(url, {
          method: "GET",
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        setCourses(data);
      } catch (error: any) {
        console.error("Error during registration:", error.message);
      }
    })();

    (async () => {
      const url = `${process.env.REACT_APP_BACKEND_URL}/instructors/courses/2`;

      try {
        const response = await fetch(url, {
          method: "GET",
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        setMyCourses(data);
      } catch (error: any) {
        console.error("Error during registration:", error.message);
      }
    })();
  }, []);

  return (
    <section className="flex justify-center items-center my-10">
      <div className="bg-gray-200 rounded py-8 px-12 shadow">
        <div className="flex items-center justify-between mb-4">
          <div className="text-xl font-bold">Instructor</div>
        </div>

        <section className="flex gap-4">
          <section>
            <div className="font-bold text-lg mb-2">My Courses</div>
            {myCourses.map((course, i) => (
              <div
                key={i}
                className="flex justify-between gap-2 text-left mb-4 border border-black rounded px-8 py-4 hover:bg-gray-400"
              >
                <div>
                  <div>
                    <span className="font-bold">ID: </span>
                    {course.courseId}
                  </div>
                  <div>
                    <span className="font-bold">Name: </span>
                    {course.courseName}
                  </div>
                </div>
              </div>
            ))}
          </section>

          <section>
            <div className="font-bold text-lg mb-2">All Courses</div>
            {courses.map((course, i) => (
              <div
                key={i}
                className="flex justify-between gap-2 text-left mb-4 border border-black rounded px-8 py-4 hover:bg-gray-400"
              >
                <div>
                  <div>
                    <span className="font-bold">ID: </span>
                    {course.courseId}
                  </div>
                  <div>
                    <span className="font-bold">Name: </span>
                    {course.courseName}
                  </div>
                </div>
              </div>
            ))}
          </section>
        </section>
      </div>
    </section>
  );
};

export default Instructor;
