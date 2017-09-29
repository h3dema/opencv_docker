#!/bin/bash

###
# create de container
###
docker build -t opencv .

# set variables
XSOCK=/tmp/.X11-unix
XAUTH=/tmp/.docker.xauth
xauth nlist $DISPLAY | sed -e 's/^..../ffff/' | xauth -f $XAUTH nmerge -

# TODO: redirect USB port to connect to the camera

###
# run the container
###
docker run -ti -v $XSOCK:$XSOCK -v $XAUTH:$XAUTH -e DISPLAY=$DISPLAY -e XAUTHORITY=$XAUTH opencv
