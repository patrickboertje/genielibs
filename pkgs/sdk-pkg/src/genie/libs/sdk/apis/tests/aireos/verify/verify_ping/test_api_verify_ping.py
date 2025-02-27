import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.aireos.verify import verify_ping


class TestVerifyPing(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          vWLC:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os aireos --mock_data_dir mock_data --state connect
                protocol: unknown
            os: aireos
            platform: single_rp
            type: ap
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['vWLC']
        self.device.connect()

    def test_verify_ping(self):
        result = verify_ping(self.device, '172.25.195.1')
        expected_output = True
        self.assertEqual(result, expected_output)
