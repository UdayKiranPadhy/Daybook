import NavBar from "../components/NavBar/NavBar";
import NavigationDrawer from "../components/NavigationDrawer/NavigationDrawer";
import { useState } from "react";
import "./App.css";
import Planner from "../components/CalendarOverview/Planner";

function App() {
  const [drawerOpen, setDrawerOpen] = useState(false);

  return (
    <>
      <NavBar setDrawerOpen={setDrawerOpen} drawerOpen={drawerOpen} />
      <div className="container">
        <aside>
          <NavigationDrawer drawerOpen={drawerOpen}></NavigationDrawer>
        </aside>
        <main className="max border round small-padding">
          <Planner />
        </main>
      </div>
    </>
  );
}

export default App;
