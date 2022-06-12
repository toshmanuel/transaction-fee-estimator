from requests import Session

from api.v1.fee import get_fee

def calculate_fee_base_on_block_confirmation_target(num_of_inputs, num_of_outputs, tx_type, target_block):
    if target_block < 1 or target_block > 1008:
        raise ValueError("Target block must be between 1 and 1008")
    result = Session().get('https://blockstream.info/testnet/api/fee-estimates')

    if 25 <= target_block < 144:
        fee_rate = result.json()[str(25)]
    elif 144 <= target_block < 504:
        fee_rate = result.json()[str(144)]
    elif 504 <= target_block < 1008:
        fee_rate = result.json()[str(504)]
    else:
        fee_rate = result.json()[str(target_block)]

    fee = get_fee(num_of_inputs, num_of_outputs, tx_type, )

    return fee_rate * fee
    