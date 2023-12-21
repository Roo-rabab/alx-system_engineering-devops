#!/usr/bin/env bash

# Use pkill to send SIGHUP signal to Gunicorn processes
pkill -HUP gunicorn

# Wait for a few seconds to allow Gunicorn to gracefully restart
sleep 5

# Check if Gunicorn processes have been restarted
pgrep gunicorn

# Additional logic can be added here to verify the restart status
