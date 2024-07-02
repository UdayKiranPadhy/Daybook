import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import isAuthenticated from "../../utils/login";

function PublicRoute({ children }: { children: React.ReactNode }) {
  const navigate = useNavigate();

  useEffect(() => {
    if (isAuthenticated()) {
      navigate("/");
    }
  }, [navigate]);

  return <>{children}</>;
}

export default PublicRoute;
