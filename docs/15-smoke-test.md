# Smoke Test

In this lab you will complete a series of tasks to ensure your Kubernetes cluster is functioning correctly.

## Data Encryption

In this section you will verify the ability to [encrypt secret data at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/#verifying-that-data-is-encrypted).

Create a generic secret:

```
kubectl create secret generic kubernetes-the-hard-way \
  --from-literal="mykey=mydata"
```

Print a hexdump of the `kubernetes-the-hard-way` secret stored in etcd:

```
sudo ETCDCTL_API=3 etcdctl get \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/etcd/ca.crt \
  --cert=/etc/etcd/etcd-server.crt \
  --key=/etc/etcd/etcd-server.key\
  /registry/secrets/default/kubernetes-the-hard-way | hexdump -C
```

> output

```
00000000  2f 72 65 67 69 73 74 72  79 2f 73 65 63 72 65 74  |/registry/secret|
00000010  73 2f 64 65 66 61 75 6c  74 2f 6b 75 62 65 72 6e  |s/default/kubern|
00000020  65 74 65 73 2d 74 68 65  2d 68 61 72 64 2d 77 61  |etes-the-hard-wa|
00000030  79 0a 6b 38 73 3a 65 6e  63 3a 61 65 73 63 62 63  |y.k8s:enc:aescbc|
00000040  3a 76 31 3a 6b 65 79 31  3a f1 5f 15 06 fd c5 b8  |:v1:key1:._.....|
00000050  b0 87 56 b9 56 97 d2 b1  24 97 b8 71 1f fd f6 f3  |..V.V...$..q....|
00000060  3d 11 03 03 b8 40 a7 da  3d 97 f0 ca 40 97 12 9a  |=....@..=...@...|
00000070  61 57 ce 96 8b d3 ff f0  5b 96 40 14 be 64 73 49  |aW......[.@..dsI|
00000080  64 0f 12 0c 89 a2 a6 5e  46 c6 57 9c e2 00 ff 44  |d......^F.W....D|
00000090  d4 0f 36 c4 b6 03 f3 83  94 de 3a ae cc 8b 91 1d  |..6.......:.....|
000000a0  24 34 d9 40 d6 fa 2e 0e  11 01 0c b3 58 70 4e 59  |$4.@........XpNY|
000000b0  a9 81 c0 c0 43 8f 2c b9  76 bd a0 de 0f eb 27 21  |....C.,.v.....'!|
000000c0  76 21 a0 7c 15 78 79 05  1a e5 8d 13 28 f7 9a 23  |v!.|.xy.....(..#|
000000d0  95 c8 09 ad 30 2a 5d 26  2d 3b f6 cf 8c 89 6a 97  |....0*]&-;....j.|
000000e0  66 47 a2 3c e6 1f 5e 2f  58 e3 7a 54 69 ab a4 73  |fG.<..^/X.zTi..s|
000000f0  78 4b 4c 68 ee c6 17 4f  42 a7 be 9f b8 1a e7 4f  |xKLh...OB......O|
00000100  1b a5 d4 d5 95 68 16 4a  c5 bc f0 dd a2 1e c4 88  |.....h.J........|
00000110  c0 23 0a e8 d9 f6 4f 56  ea 5c 74 c3 b6 c7 db 33  |.#....OV.\t....3|
00000120  23 a3 d5 aa 2f 7d a0 b7  c5 94 29 96 5b bd 4c 95  |#.../}....).[.L.|
00000130  ab 66 6b d5 fe 1d e8 b5  7f eb 53 1e b6 90 32 ab  |.fk.......S...2.|
00000140  91 55 7d 23 a1 c8 cf fb  c1 a2 4b b4 6c ce 9c 7b  |.U}#......K.l..{|
00000150  87 6c 4f 1c c5 7b cf 89  a1 0a                    |.lO..{....|
0000015a
```

The etcd key should be prefixed with `k8s:enc:aescbc:v1:key1`, which indicates the `aescbc` provider was used to encrypt the data with the `key1` encryption key.

Cleanup:
`kubectl delete secret kubernetes-the-hard-way`

## Deployments

In this section you will verify the ability to create and manage [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

Create a deployment for the [nginx](https://nginx.org/en/) web server:

```
kubectl create deployment nginx --image=nginx
```

List the pod created by the `nginx` deployment:

```
kubectl get pods -l app=nginx
```

> output

```
NAME                    READY   STATUS    RESTARTS   AGE
nginx-dbddb74b8-6lxg2   1/1     Running   0          10s
```

### Services

In this section you will verify the ability to access applications remotely using [port forwarding](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/).

Create a service to expose deployment nginx on node ports.

```
kubectl expose deployment nginx --type=NodePort --port 80
```


```
PORT_NUMBER=$(kubectl get svc -l app=nginx -o jsonpath="{.items[0].spec.ports[0].nodePort}")
```

Test to view NGINX page

```
curl http://worker-1:$PORT_NUMBER
curl http://worker-2:$PORT_NUMBER
curl http://worker-3:$PORT_NUMBER
```

> output

```
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

### Logs

In this section you will verify the ability to [retrieve container logs](https://kubernetes.io/docs/concepts/cluster-administration/logging/).

Retrieve the full name of the `nginx` pod:

```
POD_NAME=$(kubectl get pods -l app=nginx -o jsonpath="{.items[0].metadata.name}")
```

Print the `nginx` pod logs:

```
kubectl logs $POD_NAME
```

> output

```
10.38.0.0 - - [28/Sep/2020:01:11:53 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.72.0" "-"
10.32.0.1 - - [28/Sep/2020:01:11:58 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.72.0" "-"
10.40.0.0 - - [28/Sep/2020:01:12:09 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.72.0" "-"
```

### Exec

In this section you will verify the ability to [execute commands in a container](https://kubernetes.io/docs/tasks/debug-application-cluster/get-shell-running-container/#running-individual-commands-in-a-container).

Print the nginx version by executing the `nginx -v` command in the `nginx` container:

```
kubectl exec -ti $POD_NAME -- nginx -v
```

> output

```
nginx version: nginx/1.19.2
```

Next: [End to End Tests](16-e2e-tests.md)
