# Election-Campaign-Application

## EC Phase 2 Trigger(Citizens' Voice)
+ This repository is a slightly different version of the Sentiment Prediction Workflow repo. The scheduling process in this repository was implemented using the schedule python library, instead of GitHub Action as in the Sentiment Prediciton Workflow repo. This repository wasn't hosted, and is simply for the purpose of showing how schedule python library can be used in this scenario to schedule a script locally.  

### Purpose of this Project 
+ To call the endpoint of the API built, containerized (using Docker), and deployed (using Kubernetes in Digital Ocean) in the implementation of second Phase of the Election Campaign Application everyday, in order to trigger the daily sentiment prediction and topic extraction of tweet extracted from the Nigerian online Twitter space.
+ To forward the response gotten from the daily API call to a personal email, using in-built python email and smtp libraries.

### Reference GitHub Repositories
+ https://github.com/dub-em/Election-Campaign-Application
+ https://github.com/dub-em/Election-Campaign-Application-Phase2
+ https://github.com/dub-em/Election-Campaign-Application-Phase2-Implementation
+ https://github.com/dub-em/Sentiment-Prediction-Worflow

### Duckerhub Repository
+ https://hub.docker.com/r/dub3m/citizens-voice

### Article
+ https://www.linkedin.com/pulse/citizens-sentiment-michael-igbomezie

### Contribution
This Project is open to contribution and collaboration. Feel free to connect to join the project collaborators.

### Author(s)
+ Michael Dubem Igbomezie