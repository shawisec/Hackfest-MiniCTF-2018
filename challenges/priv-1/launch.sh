#!/bin/bash

socat TCP4-LISTEN:5010,fork,tcpwrap=script EXEC:/root/docker.sh,pty,stderr
