import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.multicast.configure import config_ip_pim


class TestConfigIpPim(unittest.TestCase):

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

    def test_config_ip_pim(self):
        result = config_ip_pim(self.device, 'loopback3001', 'sparse-mode')
        expected_output = None
        self.assertEqual(result, expected_output)
