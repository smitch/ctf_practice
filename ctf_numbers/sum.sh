#!/bin/bash

mkfifo tmp2
nc localhost 10000 < tmp2 | python sum.py > tmp2
rm tmp2
