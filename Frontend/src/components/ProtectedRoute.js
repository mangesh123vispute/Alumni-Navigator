import React from "react";
import { Navigate } from "react-router-dom";
import Notification from "../Notification/Notification.js";

const isAuthenticated = () => {
  const token = localStorage.getItem("authTokens");
  return token ? true : false;
};

const ProtectedRoute = ({ element: Component }) => {
  return isAuthenticated() ? Component : <Navigate to="/login" replace />;
};

export default ProtectedRoute;
