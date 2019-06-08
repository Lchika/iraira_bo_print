#!/bin/bash

flask_pid=""
kivy_pid=""

echo initialize comm.txt
cp /dev/null ./comm.txt

# run flask app
python3 -u ./flask/main.py > ./flask/debug.log 2>&1 &
flask_pid=$!
echo flask PID: ${flask_pid}

# run kivy app
python -u ./kivy/main.py > ./kivy/debug.log 2>&1 &
kivy_pid=$!
echo kivy PID: ${kivy_pid}

read -p "Exit to hit any key..."

echo killing flask app
kill ${flask_pid}
echo killing kivy app
kill ${kivy_pid}
echo done!
