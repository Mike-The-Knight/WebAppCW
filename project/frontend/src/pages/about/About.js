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
            <div class="container">
               <div class="columns is-centered">
                  <div class="column is-three-fifths">
                     <figure>
                        <img
                           src="../../../media/about_us.jpeg"
                           width={1000}
                        />
                     </figure>
                     <div class="container has-text-weight-medium	is-size-5 is-max-desktop mt-6">
                        <br></br>
                        <p>By making a platform that is only about food, we can give food lovers from all over the world a place to share their knowledge, meet other people who like the same things they do, and learn about new and exciting ways to eat</p>
                        <br></br>
                        <p>We adhere to the UK's Data Protection Act 2018, the General Data Protection Regulation (GDPR), and all other applicable data protection laws. We only collect and process data necessary for providing our services, and users are always informed of their rights, including the right to access, rectify, or delete their data.</p>
                     </div>
                  </div>
               </div>
            </div>



         </div>
      )
   }

}