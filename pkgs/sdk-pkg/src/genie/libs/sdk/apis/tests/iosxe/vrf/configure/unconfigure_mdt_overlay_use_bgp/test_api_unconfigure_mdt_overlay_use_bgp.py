import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.vrf.configure import unconfigure_mdt_overlay_use_bgp


class TestUnconfigureMdtOverlayUseBgp(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          P1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9500
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['P1']
        self.device.connect()

    def test_unconfigure_mdt_overlay_use_bgp(self):
        result = unconfigure_mdt_overlay_use_bgp(self.device, 'vrf3001', 'ipv4')
        expected_output = None
        self.assertEqual(result, expected_output)
