from lib.vpn_server.datatypes import VpnConfig


def get_mock_vpn_config():
    return VpnConfig(
        private_key='COYf3iCiGUxEBkh18bG665b3xmG3XEMPu50smR3llmU=',
        address='10.66.66.2/32,fd42:42:42::2/128',
        dns='8.8.8.8,94.140.15.15',
        public_key='yP5aL+ZKJP1RltS9jiBEq6nNovmOdunqHd6KMBeTEDE=',
        preshared_key='bw75mMF7fosJUEZhM3i4gAsxXaqTeEKR86o0fXVgh6M=',
        endpoint='194.87.140.181:56030',
        allowed_ips='0.0.0.0/0,::/0',
        config_name='395040322_0'
    )