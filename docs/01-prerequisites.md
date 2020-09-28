# Prerequisites

## VM Hardware Requirements

8 GB of RAM (Preferebly 16 GB)
50 GB Disk space

## Libvirt & QEMU

Install Virt-manager, Libvirt, and QEMU on Linux distributions, which should use
KVM as the primary driver. After the installation, start/enable the
`libvirtd.service` and make sure virsh and virt-manager can function properly
and be used to create virtual machines.

## Vagrant

Once Libvirt and QEMU is installed you may chose to deploy virtual machines
manually on it. Vagrant provides an easier way to deploy multiple virtual
machines with KVM more consistenlty.

Download and Install [Vagrant](https://www.vagrantup.com/) on your platform.

- Windows
- Debian
- Centos
- Linux
- macOS
- Arch Linux

## Vagrant-libvirt

This is a Vagrant plugin for libvirt provider. Install it as instructed
[here](https://github.com/vagrant-libvirt/vagrant-libvirt#installation) with
```
vagrant plugin install vagrant-libvirt
```
