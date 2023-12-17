import { useState } from "react";
import Admin from "./components/Admin";
import Instructor from "./components/Instructor";
import Navbar from "./components/Navbar";
import Student from "./components/Student";

const App = () => {
  const [tab, setTab] = useState<number>(1);

  const renderComponent = () => {
    switch (tab) {
      case 1:
        return <Admin />;
      case 2:
        return <Student />;
      case 3:
        return <Instructor />;
      default:
        return null;
    }
  };

  return (
    <main>
      <Navbar setTab={setTab} />
      {renderComponent()}
    </main>
  );
};

export default App;
