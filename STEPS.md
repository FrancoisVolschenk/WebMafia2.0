# How the game should flow
## Top Level
User lands on home page and has option to host game or join game

### Host Game
   - After selecting Host Game, the user is asked to enter their name. New game gets created with the name of the host and is set into "lobby" state.
   - The host is then presented with a screen where they can set up the game that is about to happen by selecting how many mafia there should be, and which optional roles should be included. (a list of optional roles can be requested from the server)
   - On the setup screen, the host should also see a list of users who have joined their game and is waiting in the lobby. They should be able to remove players from the lobby.
   - Once they are ready, they should be able to start the game, at which point the roles will be assigned.
   - While the game is active they should still be able to see a list of the players in the game and their assigned roles.
   - When the game is done, they can choose to end the game. (Unlike the mafia 1.0 game, ending the game should send it back to lobby state, so users don't get kicked out and have to rejoin)
---
Some potential nice to haves
- If we keep the web socket connection open, maybe the host can tap on user names and buzz their phone to notify them that they have been killed or silenced
- The host can also use the list of players to mark off who has been killed and who was voted out

### Join Game
   - Join Game: User should be presented with a list of games in "lobby" state (these games will now be named after the host, so no more need to ask about game codes). User should enter their name before joining a game
   - After joining, they are taken to the lobby, where they can see a list of other players who have joined.
   - While in the lobby, the player should be able to change their name, or leave the game
   - When the host starts the game, their assigned role should show up on the screen with the role description
   - When the host ends the game, the player should be taken back to the lobby
---
Some potential nice to haves
- In the lobby, maybe players can see (but not change) the game settings that the host sets up
