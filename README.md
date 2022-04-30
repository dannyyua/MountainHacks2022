<p align="center">
  <img src="./readme_image.png" alt="Mystery Mountain" height="300" />
</p>

---
Built using Python, kivy, kivyMD and WebSocket
Mystery Mountain is a guessing game for the mountainous adept who wish to hone their mountain skills. 

Gameplay consists of being given 5 rounds. In each round you are given a Mountain Peak and its corresponding image. You must then guess three very important pieces of information:

- **A**ltitude of a given Mountain
- **P**rominence of a Mountain
- **I**solation between next closest Mountain

You are then given a score out of 10 for the correctness of your guess in each round.
At the end of the round you will recieve a final score, which will be updated to a local server
and a leaderboard of top players will be displayed!


## Tech Stack and Deployment

Our backend/frontend is coded using Python, We utilise libraries from KivyMD for UI and WebSocket for Server-Client communication
We used OOP to create the logic of the project and designed special algorithms for score calculations

### Running Mystery Mountain
To install Mystery Mountain, please follow below.


Installing and running backend.  **Note**: python > 3.5 is required. 
```bash 
pip install -r requirements.txt
```
