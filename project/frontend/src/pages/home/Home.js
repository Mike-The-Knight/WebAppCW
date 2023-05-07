import { Component } from "react"
import { Post } from "../../components/Post/Post"
import axios from "axios";


import "./home.css"

export default class Home extends Component {
   constructor(props) {
      super(props);
      this.state = {
         posts: []
      };
   }

   componentDidMount() {
      this.fetchPosts();
   }

   fetchPosts = () => {
      axios
         .get("/api/posts/")
         .then((response) => {
            this.setState({
               posts: response.data,
            });
         })
         .catch((error) => console.log(error));
   };

   render() {
      const { posts } = this.state;

      return (
         <div class="section">
            <section class="hero">
               <div class="hero-body">
                  <p class="title is-1 has-text-centered">Welcome to Meal Mate!</p>
               </div>
            </section>

            <p class="has-text-centered is-size-4 mb-1">What our users are posting</p>
            <div class="columns is-centered">
               <div class="column is-4">
                  {posts.map((post) => (
                     <Post key={post.id} post={post} />
                  ))}
               </div>
            </div>
         </div>
      );
   }

}