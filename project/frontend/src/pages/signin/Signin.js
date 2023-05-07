import React, { useState } from 'react';
import { toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';


export default function Signin() {
   const navigate = useNavigate();

   const [formData, setFormData] = useState({
      username: '',
      password: ''
   });

   const handleSubmit = (event) => {
      event.preventDefault();
      console.log(formData);


   };

   const handleChange = (event) => {
      setFormData(values => ({ ...values, [event.target.name]: event.target.value }));
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
                           <input type="username" placeholder="e.g. bobsmith123" class="input" name="username" value={formData.username} onChange={handleChange} required></input>
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