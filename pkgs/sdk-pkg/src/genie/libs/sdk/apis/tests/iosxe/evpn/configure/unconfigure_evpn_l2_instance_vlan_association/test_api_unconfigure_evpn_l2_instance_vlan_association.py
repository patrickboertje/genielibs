import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.evpn.configure import unconfigure_evpn_l2_instance_vlan_association


class TestUnconfigureEvpnL2InstanceVlanAssociation(unittest.TestCase):

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

    def test_unconfigure_evpn_l2_instance_vlan_association(self):
        result = unconfigure_evpn_l2_instance_vlan_association(self.device, '10', '10', '60010')
        expected_output = None
        self.assertEqual(result, expected_output)
