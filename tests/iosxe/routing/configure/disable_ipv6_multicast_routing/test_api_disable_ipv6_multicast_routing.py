import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.routing.configure import disable_ipv6_multicast_routing


class TestDisableIpv6MulticastRouting(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          Intrepid-DUT-1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: C9600
            type: C9600
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['Intrepid-DUT-1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_disable_ipv6_multicast_routing(self):
        result = disable_ipv6_multicast_routing(device=self.device)
        expected_output = None
        self.assertEqual(result, expected_output)
