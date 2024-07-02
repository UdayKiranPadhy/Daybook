import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import isAuthenticated from "../../utils/login";

const PrivateRoute = ({ children }: { children: React.ReactNode }) => {
  const navigate = useNavigate();

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
    }
  }, [navigate]);
  return <>{children}</>;
};

export default PrivateRoute;
