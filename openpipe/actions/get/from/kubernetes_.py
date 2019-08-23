"""
Get data fron a Kubernetes API Endpoint
"""
import sys
from openpipe.pipeline.engine import ActionRuntime
from kubernetes import client, config as kube_config

class Action(ActionRuntime):

    required_some_config = """
    """

    def on_start(self, config):
      kube_config.load_kube_config()
      self.api = client.CoreV1Api()

    def on_input(self, item):
      for key, value in self.config.items():
        func = getattr(self.api, key)
        reply = func(**value)
        self.put(reply.to_dict())
