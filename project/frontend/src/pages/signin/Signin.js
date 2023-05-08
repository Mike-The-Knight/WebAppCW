import React, { useState } from 'react';
import { toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';


export default function Signin() {
   const navigate = useNavigate();

   const [username, setUsername] = useState('');
   const [password, setPassword] = useState('');

   const handleSubmit = async (event) => {
      event.preventDefault();

      const response = await fetch('/members/api/login/', {
         method: 'POST',
         headers: { 'Content-Type': 'application/json' },
         body: JSON.stringify({ username, password }),
      });

      const data = await response.json();
      if (response.ok) {
         localStorage.setItem('token', data.access);
         toast.success("Successfully signed in!")
         navigate('/home');
      } else {
         toast.error("Invalid credentials")
      }
   };

   return (
      <section class="section is-medium">
         <section class="section" style={{ marginTop: 3 }}>
            <p class="title is-2 has-text-centered">Sign into your Meal Mate account</p>
         </section>

         <form onSubmit={handleSubmit}>
            <div class="container is-max-desktop">
               <div class="columns is-centered">
                  <div class="column">
                     <div class="field ">
                        <label for="" class="label">Username</label>
                        <div class="control">
                           <input type="username" placeholder="e.g. bobsmith123" class="input" name="username" value={username} onChange={(event) => setUsername(event.target.value)}
                              required></input>
                        </div>
                     </div>
                  </div>
               </div>
               <div class="columns is-centered">
                  <div class="column">
                     <div class="field ">
                        <label for="" class="label">Password</label>
                        <div class="control">
                           <input type="password" placeholder="*******" class="input" name="password" value={password} onChange={(event) => setPassword(event.target.value)} required></input>
                        </div>
                     </div>
                  </div>
               </div>
               <div class="columns is-centered">
                  <div class="column is-2">
                     <div class="actions has-text-centered">
                        <button type="submit" class="button is-danger is-fullwidth">
                           Sign in
                        </button>
                     </div>
                  </div>
               </div>
            </div>
         </form>
      </section>
   )
}