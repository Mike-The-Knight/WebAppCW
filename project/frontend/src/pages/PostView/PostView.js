import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import axios from "axios";


export default function PostView() {
   const [post, setPost] = useState(null);
   const { id } = useParams();

   useEffect(() => {
      axios.get(`/api/main/posts/${id}/`).then((res) => {
         setPost(res.data);
      });
   }, [id]);

   if (!post) {
      return <div>Loading...</div>;
   }

   return (
      <div>
         <h1>{post.title}</h1>
         <p>{post.description}</p>
         <p>{post.type}</p>
      </div>
   );

}