from FLite.registry import etcd_client
from FLite.registry.vclient import VirtualClient
from kubernetes import client, config
from FLite.registry.vclient import VirtualClient

SOURCE_MANUAL = "manual"
SOURCE_ETCD = "etcd"
SOURCE_K8S = "kubernetes"
SOURCES = [SOURCE_MANUAL, SOURCE_ETCD, SOURCE_K8S]

CLIENT_DOCKER_IMAGE = "FLite-client"


def get_k8s_clients():
    """Get clients in kubernetes based on client field selector.

    Returns:
        list[:obj:`VirtualClient`]: A list of clients.
    """
    config.load_kube_config()

    v1 = client.CoreV1Api()

    ret = v1.list_namespaced_endpoints(
        "FLite", watch=False, field_selector="metadata.name=FLite-client-svc"
    )

    clients = []
    for record in ret.items:
        for subset in record.subsets:
            port = subset.ports[0].port
            for index, address in enumerate(subset.addresses):
                addr = "{}:{}".format(address.ip, port)
                c = VirtualClient(address.target_ref.name, addr, index)
                clients.append(c)
    return clients


def get_clients(source, etcd_addresses=None):
    """Get clients from registry.

    Args:
        source (str): Registry source, options: manual, etcd, kubernetes.
        etcd_addresses (str, optional): The addresses of etcd service.
    Returns:
        list[:obj:`VirtualClient`]: A list of clients with addresses.
    """

    if source == SOURCE_MANUAL:
        return [
            VirtualClient("1", "localhost:23400", 0),
            VirtualClient("2", "localhost:23401", 1),
        ]
    elif source == SOURCE_ETCD:
        etcd = etcd_client.EtcdClient("server", etcd_addresses, "backends")
        return etcd.get_clients(CLIENT_DOCKER_IMAGE)
    elif source == SOURCE_K8S:
        return get_k8s_clients()
    else:
        raise ValueError("Not supported source type")
