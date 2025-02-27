import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.evpn.configure import unconfigure_evpn_default_gateway_advertise_global


class TestUnconfigureEvpnDefaultGatewayAdvertiseGlobal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          NyqC:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9300
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['NyqC']
        self.device.connect()

    def test_unconfigure_evpn_default_gateway_advertise_global(self):
        result = unconfigure_evpn_default_gateway_advertise_global(self.device)
        expected_output = None
        self.assertEqual(result, expected_output)
