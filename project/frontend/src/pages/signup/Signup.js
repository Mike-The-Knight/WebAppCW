export default function Signup() {
   return (
      <section class="section is-medium">
         <section class="section" style={{ marginTop: 3 }}>
            <p class="title is-2 has-text-centered">Create a MealMate Account</p>
            <h1 class="subtitle is-5 has-text-centered">It's quick and easy.</h1>
         </section>

         <div class="container is-max-desktop">
            <div class="columns is-centered">
               <div class="column">
                  <div class="field ">
                     <label for="" class="label">Username</label>
                     <div class="control">
                        <input type="username" placeholder="e.g. bobsmith123" class="input" required></input>
                     </div>
                  </div>
               </div>
            </div>
            <div class="columns is-centered">
               <div class="column">
                  <div class="field ">
                     <label for="" class="label">Email</label>
                     <div class="control">
                        <input type="email" placeholder="e.g. bobsmith123@gmail.com" class="input" required></input>
                     </div>
                  </div>
               </div>
            </div>
            <div class="columns is-centered">
               <div class="column">
                  <div class="field ">
                     <label for="" class="label">Password</label>
                     <div class="control">
                        <input type="password" placeholder="*******" class="input" required></input>
                     </div>
                  </div>
               </div>
            </div>
            <div class="columns is-centered">
               <div class="column">
                  <div class="field ">
                     <label for="" class="label">Password Confirmation</label>
                     <div class="control">
                        <input type="password" placeholder="*******" class="input" required></input>
                     </div>
                  </div>
               </div>
            </div>
            <div class="columns is-centered">
               <div class="column is-2">
                  <div class="actions has-text-centered">
                     <div class="button is-danger is-fullwidth">
                        Sign up
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </section>
   )
}