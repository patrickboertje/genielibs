import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.arp.configure import clear_arp_cache


class TestClearArpCache(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          sisf-c9500-21-8-26-2:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: ios
            type: ios
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['sisf-c9500-21-8-26-2']
        self.device.connect()

    def test_clear_arp_cache(self):
        result = clear_arp_cache(self.device)
        expected_output = None
        self.assertEqual(result, expected_output)
