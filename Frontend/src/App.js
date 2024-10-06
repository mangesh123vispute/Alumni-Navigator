import Home from "./components/Dashboard/Home.js";
import { AuthProvider } from "./context/AuthContext";
import Login from "./components/authentication/Login.js";
import Register from "./components/authentication/Register.js";
import Profile from "./components/Pages/Profile.js";
import AboutUs from "./components/Pages/Aboutus.js";
import Home2 from "./components/Pages/Home2.js";
import Error from "./components/Pages/Error.js";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import LandingPage from "./components/LandingPage.js";
import Reset_password from "./components/authentication/Reset_password.js";
import ProtectedRoute from "./components/ProtectedRoute.js";
 import Addpost from "./components/Pages/Addpost.js";
import ImageUpload from "./components/Dashboard/Imageupload.js";


function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          {/* <Route path="/" element={<Layout />}> */}
          <Route path="/" element={<LandingPage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/home" element={<ProtectedRoute element={<Home />} />} />
          <Route path="/home2" element={<ProtectedRoute element={<Home2 />} />} />
          <Route
            path="/profile"
            element={<ProtectedRoute element={<Profile />} />}
          />
          <Route 
          path="/add-post"
          element={<ProtectedRoute element={<Addpost/>} />}
          
           />
            <Route 
          path="/add"
          element={<ProtectedRoute element={<ImageUpload/>} />}        
           />
          <Route path="/register" element={<Register />} />
          <Route path="/about" element={<AboutUs />} />
          <Route path="*" element={<Error />} />
          {/* <Route path="/forgot_password" element={<ProtectedRoute element={<Reset_password />} />} /> */}
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
