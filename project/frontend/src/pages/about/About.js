import { Component } from "react"
import "./about.css"

export default class About extends Component {
   constructor(props) {
      super(props);
      this.state = {
      };
   }

   render() {
      return (

         <div className="about-container">
            <section class="section is-medium">
               <p class="title is-1 has-text-centered has-text-white">About Us</p>
            </section>

            <div class="container is-max-desktop">
               <br></br>
               <p>TEST- By making a platform that is only about food, we can give food lovers from all over the world a place to share their knowledge, meet other people who like the same things they do, and learn about new and exciting ways to eat</p>
               <br></br>
               <p>We adhere to the UK's Data Protection Act 2018, the General Data Protection Regulation (GDPR), and all other applicable data protection laws. We only collect and process data necessary for providing our services, and users are always informed of their rights, including the right to access, rectify, or delete their data.</p>
            </div>
         </div>
      )
   }

}