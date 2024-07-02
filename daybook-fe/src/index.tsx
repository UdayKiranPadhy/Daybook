import React, { useEffect } from "react";
import ReactDOM from "react-dom/client";
import App from "./App/App";
import "beercss";
import reportWebVitals from "./reportWebVitals";
import { Provider } from "react-redux";
import { store } from "./redux/store";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import PublicRoute from "./components/PublicRoute/PublicRoute";
import PrivateRoute from "./components/PrivateRoute/PrivateRoute";
import Logout from "./components/Logout/Logout";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);

const router = createBrowserRouter([
  {
    path: "/",
    element: (
      <PrivateRoute>
        <App />
      </PrivateRoute>
    ),
  },
  {
    path: "login",
    element: (
      <PublicRoute>
        <div>
          <h1>
            <a href="http://localhost:8000/oauth/google">Login with Google</a>
          </h1>
        </div>
      </PublicRoute>
    ),
  },
  {
    path: "logout",
    element: (
      <PrivateRoute>
        <Logout />
      </PrivateRoute>
    ),
  },
]);

root.render(
  <Provider store={store}>
    <React.StrictMode>
      <RouterProvider router={router} />
    </React.StrictMode>
  </Provider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
