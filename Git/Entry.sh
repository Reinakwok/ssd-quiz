#!/bin/sh

# Set Git user information
git config --global user.name "Kwok Sze Xuan Reina"
git config --global user.email "2203286@sit.singaporetech.edu.sg"

# Start the git-http-server on port 3000
exec git-http-server -p 3000 /home/git

