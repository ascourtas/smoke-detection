# Smoke Detection Using Deep Learning
Successful wildfire intervention is dependent on the early detection of wildfire smoke; 
mere minutes can drastically alter the extent of societal and ecological damage from 
wildfires. 

When using deep learning for detecting wildfire smoke, past research has largely focused on CNNs. 
Here, we explore using a combined CNN-LSTM to capture both spatial and temporal information
about the smoke.

## Getting started
All packages and dependencies are included in the Dockerfile at the root of this repo. 

To build the Docker container, run the following from the root of this repository:

`docker build -t <desired_name_of_image> . `

To run the container:

`docker run -it -p 9000:9000 <desired_name_of_image>`

The choice of ports (in this case, 9000) is arbitrary, replace it with whatever ports you have 
open.

Once the container is running, you should see output similar to the following. Open the link 
your browser to use the interactive Jupyter notebook.

![alt text](/docs/images/jupyter_output.png "output of running Docker container")

## Code maintenance
### Parent repositories

This repository is forked from 

### Current TODOs
NOTE: This repo is a WIP.
Upcoming improvements include:
- full information about the fork history of the repo
- instructions on how to fetch updates from various upstream remote repos
- how to run this on Chameleon
- how to set up and use the Docker containers given recent improvements
- any alteration made to the Waggle setup process