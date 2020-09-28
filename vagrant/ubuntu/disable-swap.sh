#!/bin/bash

set -e
set -o nounset

sed -i -e 's/^\(.*\<swap\>.*\)$/#\1/' /etc/fstab
swapoff -a
