import React, { useState } from 'react';
import { toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';


export default function Signup() {
   const navigate = useNavigate();

   const [formData, setFormData] = useState({
      username: '',
      email: '',
      password: '',
   });

   const handleSubmit = (event) => {
      event.preventDefault();
      console.log(formData);

      fetch('members/api/register/', {
         method: 'POST',
         headers: {
            'Content-Type': 'application/json',
         },
         body: JSON.stringify(formData),
      })
         .then((response) => {
            if (response.ok) {
               toast.success("User successfully created!")
               navigate('/signin');
            } else {
               toast.error("Error creating user")
               console.error('Error creating user.');
            }
         })
         .catch((error) => {
            toast.error("Error creating user")
            console.error('Error creating user.', error);
         });
   };

   const handleChange = (event) => {
      setFormData(values => ({ ...values, [event.target.name]: event.target.value }));
   };

   return (
      <section class="section is-medium">
         <section class="section" style={{ marginTop: 3 }}>
            <p class="title is-2 has-text-centered">Create a MealMate Account</p>
            <h1 class="subtitle is-5 has-text-centered">It's quick and easy.</h1>
         </section>

         <form onSubmit={handleSubmit}>
            <div class="container is-max-desktop">
               <div class="columns is-centered">
                  <div class="column">
                     <div class="field ">
                        <label for="" class="label">Username</label>
                        <div class="control">
                           <input type="username" placeholder="e.g. bobsmith123" class="input" name="username" value={formData.username} onChange={handleChange} required></input>
                        </div>
                     </div>
                  </div>
               </div>
               <div class="columns is-centered">
                  <div class="column">
                     <div class="field ">
                        <label for="" class="label">Email</label>
                        <div class="control">
                           <input type="email" placeholder="e.g. bobsmith123@gmail.com" class="input" name="email" value={formData.email} onChange={handleChange} required></input>
                        </div>
                     </div>
                  </div>
               </div>
               <div class="columns is-centered">
                  <div class="column">
                     <div class="field ">
                        <label for="" class="label">Password</label>
                        <div class="control">
                           <input type="password" placeholder="*******" class="input" name="password" value={formData.password} onChange={handleChange} required></input>
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
                        <button type="submit" class="button is-danger is-fullwidth">
                           Sign up
                        </button>
                     </div>
                  </div>
               </div>
            </div>
         </form>
      </section>
   )
}