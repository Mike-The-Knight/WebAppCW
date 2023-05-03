import HomePage from "./pages/home/Home"
import SigninPage from "./pages/signin/Signin"
import SignupPage from "./pages/signup/Signup"
import 'bulma/css/bulma.min.css';
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from "react-router-dom"


function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<HomePage />} />
        <Route path='/signin' element={<SigninPage />} />
        <Route path='/signup' element={<SignupPage />} />
      </Routes>
    </Router>
  );
}

export default App;
