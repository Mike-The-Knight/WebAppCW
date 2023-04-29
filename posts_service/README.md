# Posts service
End points:
Posts:
Posts have an author (int), a date_posted (date), a type ("MEAL" or "RECIPE"), a title (string), a description (string), ingredients (string) and instructions (string).
It is intended that only RECIPE type posts have ingredients and istructions however this validation is not coded into the model.
- GET /posts Get all posts
- GET /posts/:id Get post with specific id
- POST /posts Create new post
- PUT /posts/:id Update post with specific id

Likes
Likes have a user (int) and a post (int)
- GET /likes Get all likes
- GET /likes/:id Get like with specific id
- POST /likes Create new like
- PUT /likes/:id Update like with specific id

Comments
Comments have an author (int), a post (int), a date_posted (date) and text (string)
- GET /comments Get all comments
- GET /comments/:id Get comment with specific id
- POST /comments Create new comment
- PUT /comments/:id Update comment with specific id

Reviews
Reviews have an author (int), post (int), date_posted (date), title (string), text (string) and a rating (int 1 - 5)
- GET /reviews Get all reviews
- GET /reviews/:id Get review with specific id
- POST /reviews Create new review
- PUT /reviews/:id Update review with specific id
