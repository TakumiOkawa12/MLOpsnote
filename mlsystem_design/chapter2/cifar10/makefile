ABSOLUTE_PATH := $(shell pwd)
BASE_IMAGE_NAME := takumiokawa/ml-system-in-actions
TRAINING_PATTERN := training_pattern
TRAINING_PROJECT := cifar10
IMAGE_VERSION := 0.0.1

DOCKERFILE := Dockerfile

.PHONY: dev
dev:
	pip install -r requirements.txt

.PHONY: d_build
d_build:
	docker build \
		-t $(BASE_IMAGE_NAME):$(TRAINING_PATTERN)_$(TRAINING_PROJECT)_$(IMAGE_VERSION) \
		-f $(DOCKERFILE) .

.PHONY: train
train:
	mlflow run . --env-manager=local

.PHONY: ui
ui:
	mlflow ui