#!/bin/bash

make MV88X3310=YES
make install
modprobe tn40xx
