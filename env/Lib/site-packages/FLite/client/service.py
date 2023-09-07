import importlib
import logging
import threading

from FLite.protobuf import (
    client_service_pb2_grpc as client_grpc,
    client_service_pb2 as client_pb,
    common_pb2 as common_pb,
)
from FLite.protocol import codec
from FLite.utils.obvious_notice_logger import noticelogger

logger = logging.getLogger(__name__)


class ClientService(client_grpc.ClientServiceServicer):
    """ "Remote gRPC client service.

    Args:
        client (:obj:`BaseClient`): Federated learning client instance.
    """

    def __init__(self, client):
        self._base = client

    def Operate(self, request, context):
        """Perform training/testing operations."""
        data = request.model

        try:
            if self._base.encryption_key != "":
                encryption_type = self._base.encryption_type
                encryptor_path = "FLite.encryptor.{}".format(encryption_type)
                encryptor_lib = importlib.import_module(encryptor_path)
                encryptor = getattr(encryptor_lib, "Encryptor")(self._base.encryption_key)
                data = encryptor.decrypt(request.model)
                noticelogger.get_instance().blue("During model publishing: Decryption ({}) OK!".format(self._base.encryption_type))
        except Exception as e:
            logger.error("\033[1;31mDuring model publishing: Decryption ({}) failed maybe! \033[0m".format(self._base.encryption_type,e))

        model = codec.unmarshal(data)
        is_train = request.type == client_pb.OP_TYPE_TRAIN
        # Threading is necessary to respond to server quickly
        t = threading.Thread(
            target=self._base.operate,
            args=[model, request.config, request.data_index, is_train],
        )
        t.start()
        response = client_pb.OperateResponse(
            status=common_pb.Status(code=common_pb.SC_OK),
        )
        return response
