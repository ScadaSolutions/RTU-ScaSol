#!/bin/bash

cd RTU-ScaSol/RTU/

python3 exec.py  &
pid1=$!

sleep 2

cd

~/opendnp3-release/build/cpp/examples/outstation/outstation-demo &
pid2=$!
