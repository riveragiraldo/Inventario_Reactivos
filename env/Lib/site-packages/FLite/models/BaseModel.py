import importlib
from torch import nn
from os import path
import logging

logger = logging.getLogger(__name__)


class BaseModel(nn.Module):
    def __init__(self):
        super(
            BaseModel, self
        ).__init__()  # super() is a built-in function that returns a proxy object (temporary object of the superclass) that allows you to refer parent class by 'super' instead of 'self'. The proxy object delegates method calls to the parent class or to a sibling class.


def initModel(model_name: str):

    dir_path = path.dirname(path.realpath(__file__))
    model_file = path.join(dir_path, "{}.py".format(model_name))
    if not path.exists(model_file):
        logger.error("Please specify a valid model.")

    model_path = "FLite.models.{}".format(model_name)
    model_lib = importlib.import_module(model_path)
    model = getattr(model_lib, "Model")
    return model
