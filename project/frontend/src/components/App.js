import { Component } from "react";
import HomePage from "../pages/home/Home"
import SigninPage from "../pages/signin/Signin"
import SignupPage from "../pages/signup/Signup"
import AboutPage from "../pages/about/About"
import PostView from "../pages/PostView/PostView"
import 'react-toastify/dist/ReactToastify.css';
import CustomNavbar from "./Navbar/Navbar"
import { ToastContainer } from 'react-toastify';
import "../../node_modules/bulma/css/bulma.css";
import { render } from "react-dom";
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from "react-router-dom"


export default class App extends Component {
  render() {
    return (
      [<CustomNavbar />,
      <ToastContainer />,
      <Router>
        <Routes>
          <Route path='/' element={<HomePage />} />
          <Route path='/home' element={<HomePage />} />
          <Route path='/about' element={<AboutPage />} />
          <Route path='/signin' element={<SigninPage />} />
          <Route path='/signup' element={<SignupPage />} />
          <Route path="/post/:id" element={<PostView />} />
        </Routes>
      </Router>
      ]
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
