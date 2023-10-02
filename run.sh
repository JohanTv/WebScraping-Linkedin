#!/bin/bash
IMAGE="scrapy_project"
TAG="v0.1"
CONTAINER_NAME="scrapy"

SOURCE=$PWD
TARGET="/home/app/"
WORK_DIR=$TARGET

docker run -it --rm -v $SOURCE:$TARGET -w $WORK_DIR $IMAGE:$TAG $1 $2 $3 $4
# docker create -it --name $CONTAINER_NAME -v $SOURCE:$TARGET -w $WORK_DIR $IMAGE:$TAG /bin/bash
# docker start -i $CONTAINER_NAME 