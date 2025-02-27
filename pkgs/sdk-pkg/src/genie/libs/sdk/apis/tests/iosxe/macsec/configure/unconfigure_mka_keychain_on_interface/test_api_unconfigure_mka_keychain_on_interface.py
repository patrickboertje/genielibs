import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.macsec.configure import unconfigure_mka_keychain_on_interface


class TestUnconfigureMkaKeychainOnInterface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          LG-PK:
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
        self.device = self.testbed.devices['LG-PK']
        self.device.connect()

    def test_unconfigure_mka_keychain_on_interface(self):
        result = unconfigure_mka_keychain_on_interface(self.device, 'GigabitEthernet1/0/10', 'kc1')
        expected_output = None
        self.assertEqual(result, expected_output)
