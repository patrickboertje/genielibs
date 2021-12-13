import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.evpn.configure import unconfigure_l2vpn_evpn_router_id


class TestUnconfigureL2vpnEvpnRouterId(unittest.TestCase):

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

    def test_unconfigure_l2vpn_evpn_router_id(self):
        result = unconfigure_l2vpn_evpn_router_id(self.device, 'loopback0')
        expected_output = None
        self.assertEqual(result, expected_output)
