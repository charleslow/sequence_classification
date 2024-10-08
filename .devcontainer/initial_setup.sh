#!/bin/bash

# ideally the brew install would be done in the Dockerfile, but somehow that doesn't work
brew tap databricks/tap
brew install databricks

# install poetry environments
poetry install

# setup git
echo setting up git:
read -p "git user name: " git_username
read -p "git user email: " git_user_email
git config --global user.name "$git_username"
git config --global user.email "$git_user_email"
git config --global pull.rebase false


# setup spark
cat <<EOF >> ~/.bashrc
export JAVA_HOME=/usr/lib/jvm/default-java
EOF