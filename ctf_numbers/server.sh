#!/bin/bash

mkfifo tmp
nc localhost -l 10000 < tmp | python server.py > tmp
rm tmp

