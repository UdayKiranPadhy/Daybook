import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { removeCookie } from "../../utils/cookie";

const Logout = () => {
  const navigate = useNavigate();

  useEffect(() => {
    removeCookie("session");

    // Redirect to the login page after logout
    navigate("/login");
  }, [navigate]);

  // Optionally, display a message or a loader while processing the logout
  return <div>Logging out...</div>;
};

export default Logout;
