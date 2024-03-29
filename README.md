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

To run the container, and be able to save changes made to the Jupyter notebook:

`docker run -it -p 9000:9000 -v <local_project_path>/smoke-detection/src:/userdata/kerasData <desired_container_name>`

The `-v` option treats the `/src` folder as a Docker volume for persistent data storage. Changes made in this folder 
persist past the life of the Docker container.

Once the container is running, you should see output similar to the following. Open the link 
your browser to use the interactive Jupyter notebook.

![output of running Docker container](/docs/images/jupyter_output.png "output of running Docker container")

## Code maintenance
### Parent repositories

This repository is forked from [i3perez/keras-smoke-detection](https://gitlab.nautilus.optiputer.net/i3perez/keras-smoke-detection/-/tree/master), 
which is forked from [ar-noc/smoke-detection](https://gitlab.nautilus.optiputer.net/ar-noc/keras-smoke-detection/-/tree/670a1c6c2feb4e9f08acf42a6bbd35e2b9190b35) 

Both may be set as upstream remotes for this repository. For example, once established, you can view your 
remotes via `git remote -v`

![output of git remote -v](/docs/images/remote_list.png "output of git remote -v")

### Working with Docker

If you've accumulated a bunch of dangling images (denoted by the `<none>` name and tag) then you can clear them with:

`docker system prune`

### Working with AWS
#### Set everything up
1. Set up EC2 G or P instance with at least 75GB of EBS storage.
2. Create an IAM Role that allows for all S3 policies. Assign the role to the EC2 instance from Step 1.
3. Create an S3 bucket. 
4. `ssh` into EC2 instance. Pull down appropriate images from HPWREN. 

`ssh -i <path to private key you generated> ec2-user@<DNS iPV4 name of instance>`

5. Untar the file.
6. Copy over images to S3 bucket.

`aws s3 cp my_image_folder s3://my_bucket/dest_folder_name --recursive`

#### Once the S3 bucket has been populated
1. If the EC2 bucket doesn't already have the files from the S3 bucket, `cp` them over.
2. Build the Docker container
3. Run the container (see command above)



### Current TODOs
NOTE: This repo is a WIP.
Upcoming improvements include:
- full information about the fork history of the repo
- instructions on how to fetch updates from various upstream remote repos
- how to run this on Chameleon
- how to set up and use the Docker containers given recent improvements
- any alteration made to the Waggle setup process
- code restructuring and changes pulled in from ar-noc, which are in local branches but have yet to be pushed
- better documentation and cleaning up deprecated files
