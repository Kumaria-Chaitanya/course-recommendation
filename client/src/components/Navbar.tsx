import { FC } from "react";

interface INavbar {
  setTab: (tab: number) => void;
}

const Navbar: FC<INavbar> = ({ setTab }) => {
  return (
    <nav className="border-b border-black py-4 bg-gray-200 shadow flex items-center justify-between">
      <div className="mx-4 font-bold text-lg">Course Recommendation</div>
      <div>
        <div>
          <button
            type="button"
            className="border border-black rounded py-1 px-4 hover:bg-gray-400 mx-2"
            onClick={() => setTab(1)}
          >
            Admin
          </button>
          <button
            type="button"
            className="border border-black rounded py-1 px-4 hover:bg-gray-400 mx-2"
            onClick={() => setTab(2)}
          >
            Student
          </button>
          <button
            type="button"
            className="border border-black rounded py-1 px-4 hover:bg-gray-400 mx-2"
            onClick={() => setTab(3)}
          >
            Instructor
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
