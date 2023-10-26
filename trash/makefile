.PHONY: all
.DEFAULT_GOAL := container

image:
	sudo docker build --build-arg USER_ID=$(shell id -u) --build-arg GROUP_ID=$(shell id -g) -t asr .

container: image
	sudo docker run -it --rm --gpus all -v .:/outer --ipc=host asr
