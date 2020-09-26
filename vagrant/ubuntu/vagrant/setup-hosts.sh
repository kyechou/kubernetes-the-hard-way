#!/bin/bash
set -e

# remove ubuntu1804 entry
sed -e '/^.*ubuntu1804.*/d' -i /etc/hosts

# Update /etc/hosts about other hosts
cat >> /etc/hosts <<EOF
192.168.5.11    master-1
192.168.5.12    master-2
192.168.5.21    worker-1
192.168.5.22    worker-2
192.168.5.23    worker-3
192.168.5.100   loadbalancer
EOF
