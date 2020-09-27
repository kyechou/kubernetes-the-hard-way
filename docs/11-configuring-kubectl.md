# Configuring kubectl for Remote Access

In this lab you will generate a kubeconfig file for the `kubectl` command line utility based on the `admin` user credentials.

## The Admin Kubernetes Configuration File

Each kubeconfig requires a Kubernetes API Server to connect to. To support high availability the IP address assigned to the external load balancer fronting the Kubernetes API Servers will be used.

Generate a kubeconfig file suitable for authenticating as the `admin` user:

```
KUBERNETES_LB_ADDRESS=192.168.5.100

kubectl config set-cluster k8s-cluster \
    --certificate-authority=./certs/ca.crt \
    --embed-certs=true \
    --server=https://${KUBERNETES_LB_ADDRESS}:6443

kubectl config set-credentials admin \
    --client-certificate=./certs/admin.crt \
    --client-key=./certs/admin.key

kubectl config set-context k8s-the-hard-way \
    --cluster=k8s-cluster \
    --user=admin

kubectl config use-context k8s-the-hard-way
```

Reference doc for kubectl config [here](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)

## Verification

Check the health of the remote Kubernetes cluster:

```
kubectl get componentstatuses
```

Output:

```
NAME                 STATUS    MESSAGE             ERROR
controller-manager   Healthy   ok
scheduler            Healthy   ok
etcd-1               Healthy   {"health":"true"}
etcd-0               Healthy   {"health":"true"}
```

List the nodes in the remote Kubernetes cluster:

```
kubectl get nodes
```

Output:

```
NAME       STATUS   ROLES    AGE    VERSION
worker-1   NotReady    <none>   118s   v1.13.0
worker-2   NotReady    <none>   118s   v1.13.0
```

Note: It is OK for the worker node to be in a `NotReady` state. Worker nodes will come into `Ready` state once networking is configured.

Next: [Deploy Pod Networking](12-configure-pod-networking.md)
