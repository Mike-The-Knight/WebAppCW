import React, { Component } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faThumbsUp, faComment } from '@fortawesome/free-solid-svg-icons';
import { useNavigate } from 'react-router-dom';


export const Post = ({ post }) => {
   const navigate = useNavigate();

   const handleClick = () => {
      navigate(`/post/${post.id}`);
   };

   return (
      <div class="card mb-6 shadow-md is-cursor-pointer transform is-duration-300 hover-shadow-xl hover-translate-y" onClick={handleClick}>
         <div class="card-content">
            <div class="media">
               <div class="media-left">
                  <figure class="image is-64x64">
                     <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image"></img>
                  </figure>
               </div>
               <div class="media-content">
                  <p class="title is-3">{post.title}</p>
                  <p class="subtitle is-6">@{post.author.username}</p>
               </div>
            </div>

            <div class="content">
               <div class="mb-5">
                  {post.description}
               </div>
               {post.ingredients && (
                  <div>
                     <div class="has-text-grey-dark	 has-text-weight-bold mb-2">
                        Ingredients
                     </div>
                     <p class="mb-4">{post.ingredients}</p>
                  </div>
               )}
               {post.instructions && (
                  <div>
                     <div class="has-text-grey-dark	 has-text-weight-bold mb-2">
                        Method
                     </div>
                     <p>{post.instructions}</p>
                  </div>
               )}
            </div>

            <p class="mb-2">
               <span style={{ marginRight: '10px' }}>
                  <time datetime="2016-1-1">{post.date_posted} •</time>
               </span>
               <span style={{ marginRight: '15px' }}>
                  <FontAwesomeIcon icon={faThumbsUp} />
                  {' '}
                  {post.likes.length}
               </span>
               <span >
                  <FontAwesomeIcon icon={faComment} />
                  {' '}
                  {post.comments.length}
               </span>
            </p>
         </div>
      </div>
   )

}

export default Post;