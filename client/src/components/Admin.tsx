import { useEffect, useState } from "react";

const Admin = () => {
  const [students, setStudents] = useState<any[]>([]);
  const [courses, setCourses] = useState<any[]>([]);
  const [showModal, setShowModal] = useState<boolean>(false);

  useEffect(() => {
    (async () => {
      const url = `${process.env.REACT_APP_BACKEND_URL}/admin/students`;

      try {
        const response = await fetch(url, {
          method: "GET",
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        setStudents(data);
      } catch (error: any) {
        console.error("Error during registration:", error.message);
      }
    })();

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
  }, []);

  return (
    <section className="flex justify-center items-center my-10">
      <div className="bg-gray-200 rounded py-8 px-12 shadow">
        <div className="flex items-center justify-between mb-4">
          <div className="text-xl font-bold">Admin</div>

          <div>
            <button
              type="button"
              className="border border-black rounded py-1 px-4 hover:bg-gray-400 mx-2"
              onClick={() => setShowModal(true)}
            >
              Add Student
            </button>

            <button
              type="button"
              className="border border-black rounded py-1 px-4 hover:bg-gray-400"
              onClick={() => setShowModal(true)}
            >
              Add Courses
            </button>
          </div>

          {/* Main modal */}
          {showModal && (
            <div className="fixed flex justify-center items-center z-50 w-full p-4 md:inset-0 h-screen backdrop-filter backdrop-blur backdrop-brightness-50">
              {/* Overlay */}
              <div
                className="fixed inset-0 bg-white opacity-50 w-full h-full"
                onClick={() => setShowModal(false)}
              />
              <div className="relative w-full max-w-lg max-h-full">
                {/* Modal content */}
                <div className="relative bg-gray-800 rounded-lg shadow">
                  <button
                    type="button"
                    className="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                    onClick={() => setShowModal(false)}
                  >
                    <svg
                      className="w-3 h-3"
                      aria-hidden="true"
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 14 14"
                    >
                      <path
                        stroke="currentColor"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth="2"
                        d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
                      />
                    </svg>
                    <span className="sr-only">Close modal</span>
                  </button>
                  <div className="px-6 py-6 lg:px-8">
                    <h3 className="mb-4 text-xl font-medium text-gray-900 dark:text-white">
                      Add Student
                    </h3>
                    <section className="space-y-6">
                      <div>
                        <label
                          htmlFor="id"
                          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                        >
                          Student ID
                        </label>
                        <input
                          name="id"
                          id="od"
                          className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                          placeholder="id"
                          required
                        />
                      </div>
                      <div>
                        <label
                          htmlFor="name"
                          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                        >
                          Student Name
                        </label>
                        <input
                          name="name"
                          id="name"
                          className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                          placeholder="name"
                          required
                        />
                      </div>
                      <div>
                        <label
                          htmlFor="age"
                          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                        >
                          Student Age
                        </label>
                        <input
                          name="age"
                          id="age"
                          className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                          placeholder="age"
                          required
                        />
                      </div>
                      <div>
                        <label
                          htmlFor="email"
                          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                        >
                          Student Email
                        </label>
                        <input
                          name="email"
                          id="email"
                          className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                          placeholder="email"
                          required
                        />
                      </div>
                      <button
                        className="w-full focus:outline-none font-semibold rounded-lg text-md px-5 py-2.5 text-center bg-gray-200 hover:bg-gray-400"
                        // onClick={handleUpload}
                      >
                        Add Student
                      </button>
                    </section>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>

        <section className="flex gap-4">
          <section>
            <div className="font-bold text-lg mb-2">Students</div>
            {students.map((student, i) => (
              <div
                key={i}
                className="flex-row gap-2 text-left mb-4 border border-black rounded px-8 py-4 hover:bg-gray-400 cursor-pointer"
              >
                <div>
                  <span className="font-bold">ID: </span>
                  {student.studentId}
                </div>
                <div>
                  <span className="font-bold">Name: </span>
                  {student.studentName}
                </div>
                <div>
                  <span className="font-bold">Age: </span>
                  {student.studentAge}
                </div>
                <div>
                  <span className="font-bold">Email: </span>
                  {student.studentEmail}
                </div>
              </div>
            ))}
          </section>

          <section>
            <div className="font-bold text-lg mb-2">Courses</div>
            {courses.map((course, i) => (
              <div
                key={i}
                className="flex-row gap-2 text-left mb-4 border border-black rounded px-8 py-4 hover:bg-gray-400 cursor-pointer"
              >
                <div>
                  <span className="font-bold">ID: </span>
                  {course.courseId}
                </div>
                <div>
                  <span className="font-bold">Name: </span>
                  {course.courseName}
                </div>
              </div>
            ))}
          </section>
        </section>
      </div>
    </section>
  );
};

export default Admin;
