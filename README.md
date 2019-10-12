# Brower Go API

## Resources

### Login


### Users

###### User Endpoints
@auth_required  
`/users/<str:user_name>` GET  
`/users/<str:user_name>` POST  
`/users/<str:user_name>` PUT   
Alias:  
`/users/<int:user_id>`

### Games
`/games/` no endpoint; game lists are retrieved by room  

##### Moves & Branches
`/games/<int:game_id>` GET  
@auth_required  
`/games/<int:game_id>` POST  <- post move to game


##### Messages
@auth_required
`/games/<int:game_id>/moves/<int:move_id>` POST  <- post message/branch
`/games/<int:game_id>/moves/<int:move_id>` POST  <- edit move

### Rooms

##### Archive Room

The archive room is used to search and access games once they have been completed.
path: `/rooms/archive`