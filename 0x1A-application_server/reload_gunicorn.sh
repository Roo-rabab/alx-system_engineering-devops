#!/usr/bin/env bash

# Reload Gunicorn using systemctl
echo "Reloading Gunicorn without downtime..."
sudo systemctl reload gunicorn
echo "Gunicorn reloaded successfully."
