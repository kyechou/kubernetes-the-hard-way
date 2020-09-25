# Provisioning Compute Resources

Note: You must have Libvirt, QEMU, and Vagrant configured at this point

Download this github repository and cd into the vagrant folder

`git clone https://github.com/mmumshad/kubernetes-the-hard-way.git`

CD into vagrant directory

`cd kubernetes-the-hard-way/vagrant`

Run Vagrant up

`vagrant up --provider=libvirt`


This does the below:

- Deploys 6 VMs - 2 Master, 3 Worker and 1 Loadbalancer with the name 'k8s-* '
    > This is the default settings. This can be changed at the top of the Vagrant file

- Set's IP addresses in the range 192.168.5

    | VM            |  VM Name         | Purpose       | IP            | Forwarded Port   |
    | ------------  | ---------------- |:-------------:| -------------:| ----------------:|
    | master-1      | k8s-master-1     | Master        | 192.168.5.11  |     2711         |
    | master-2      | k8s-master-2     | Master        | 192.168.5.12  |     2712         |
    | worker-1      | k8s-worker-1     | Worker        | 192.168.5.21  |     2721         |
    | worker-2      | k8s-worker-2     | Worker        | 192.168.5.22  |     2722         |
    | worker-3      | k8s-worker-3     | Worker        | 192.168.5.23  |     2723         |
    | loadbalancer  | k8s-loadbalancer | LoadBalancer  | 192.168.5.100 |     2800         |

    > These are the default settings. These can be changed in the Vagrant file

- Add's a DNS entry to each of the nodes to access internet
    > DNS: 8.8.8.8

- Install's Docker on Worker nodes
- Runs the below command on all nodes to allow for network forwarding in IP Tables.
  This is required for kubernetes networking to function correctly.
    > sysctl net.bridge.bridge-nf-call-iptables=1


## SSH to the nodes

There are two ways to SSH into the nodes:

### 1. SSH using Vagrant

  From the directory you ran the `vagrant up` command, run `vagrant ssh <vm>`
  for example: `vagrant ssh master-1`.
  > Note: Use VM field from the above table and not the vm name itself.

### 2. SSH Using SSH Client Tools

Use your favourite SSH Terminal tool (putty).

Use the above IP addresses. Username and password based SSH is disabled by
default. Vagrant generates a private key for each of these VMs. It is placed
under the .vagrant folder (in the directory you ran the `vagrant up` command
from) at the below path for each VM:

**Private Key Path:** `.vagrant/machines/<machine name>/libvirt/private_key`

**Username:** `vagrant`


## Verify Environment

- Ensure all VMs are up
- Ensure VMs are assigned the above IP addresses
- Ensure you can SSH into these VMs using the IP and private keys
- Ensure the VMs can ping each other
- Ensure the worker nodes have Docker installed on them. Version: 18.06
  > command `sudo docker version`

## Troubleshooting Tips

If any of the VMs failed to provision, or is not configured correct, delete the
vm using the command:

`vagrant destroy <vm>`

Then reprovision. Only the missing VMs will be re-provisioned

`vagrant up --provider=libvirt`

