import "./navbar.css"

export default function CustomNavbar() {
   return (
      <nav class="navbar is-danger" role="navigation" aria-label="main navigation">
         <div class="navbar-brand">
            <a class="navbar-item" href="/">
               <img
                  src="../../../media/meal_mate_white.png"
                  width={200}
               />
            </a>
         </div>

         <div id="navbarBasicExample" class="navbar-menu">
            <div class="navbar-start">
               <a class="navbar-item" href="/">
                  Home
               </a>
               <a class="navbar-item" href="/about">
                  About Us
               </a>
            </div>
            <div class="navbar-end">
               <div class="navbar-item">
                  <div class="buttons">
                     <a class="button is-danger" href="/signup">
                        <strong>Sign up</strong>
                     </a>
                     <a class="button is-light" href="/signin">
                        Log in
                     </a>
                  </div>
               </div>
            </div>
         </div>
      </nav>
   )
}