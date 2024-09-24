import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import LoadingSpinner from "../Loading/Loading.js";

const Otp = () => {
  const navigate = useNavigate();
  const [message, setMessage] = useState("");
  const [Loading, setLoading] = useState(false);
  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true)
    const otp = event.target.otp.value;

    const response = await fetch("http://127.0.0.1:8000/otp/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        otp: Number(otp),
      }),
    });
    const data = await response.json();

    if (response.ok) {
      setLoading(false)
      // Handle successful registration (e.g., redirect to login)
      // console.log("Registration successful:", data);
      if (response.status === 200) {
        console.log("Registration successful:", data);
        setMessage("Registration successful!");
        navigate("/");
      }
    } else {
      // Handle message response
      setMessage(data.detail || "Something went wrong.");
      setLoading(false)
    }
  };
  return (
    <div className="hold-transition login-page">
      <LoadingSpinner isLoading={Loading} />
      <meta charSet="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>AlumniHub | Forgot Password</title>
      {/* Google Font: Source Sans Pro */}
      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback"
      />
      {/* Font Awesome */}
      <link
        rel="stylesheet"
        href="../../plugins/fontawesome-free/css/all.min.css"
      />
      {/* icheck bootstrap */}
      <link
        rel="stylesheet"
        href="../../plugins/icheck-bootstrap/icheck-bootstrap.min.css"
      />
      {/* Theme style */}
      <link rel="stylesheet" href="../../dist/css/adminlte.min.css" />
      <div className="login-box">
        <div className="login-logo">
          <a href="../../index2.html">
            <b>Alumni</b>Hub
          </a>
        </div>
        {/* /.login-logo */}
        <div className="card">
          <div className="card-body login-card-body">
            {message && <p style={{ color: "red" }}>{message}</p>}
            <p className="login-box-msg">
              Enter Your Otp, Its validity is 1 min
            </p>
            <form onSubmit={handleSubmit}>
              <div className="input-group mb-3">
                <input
                  type="number"
                  className="form-control"
                  placeholder="Enter Otp"
                  name="otp"
                />
                <div className="input-group-append">
                  <div className="input-group-text">
                    {/* <span className="fas fa-envelope" /> */}
                  </div>
                </div>
              </div>
              <div className="row">
                <div className="col-12">
                  <button type="submit" className="btn btn-primary btn-block">
                    Enter Otp
                  </button>
                </div>
                {/* /.col */}
              </div>
            </form>
            <p className="mt-3 mb-1">
              <a href="/login">Login</a>
            </p>
            <p className="mb-0">
              <a href="/register" className="text-center">
                Register a new membership
              </a>
            </p>
          </div>
          {/* /.login-card-body */}
        </div>
      </div>
      {/* /.login-box */}
      {/* jQuery */}
      {/* Bootstrap 4 */}
      {/* AdminLTE App */}
    </div>
  );
};

export default Otp;
