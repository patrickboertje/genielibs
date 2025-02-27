import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.multicast.configure import configure_ip_pim_vrf_ssm_default


class TestConfigureIpPimVrfSsmDefault(unittest.TestCase):

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

    def test_configure_ip_pim_vrf_ssm_default(self):
        result = configure_ip_pim_vrf_ssm_default(self.device, 'vrf3001')
        expected_output = None
        self.assertEqual(result, expected_output)
