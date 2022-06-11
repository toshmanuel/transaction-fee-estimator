from requests import *

def get_feerate_per_vbytes(num_of_inputs,num_of_outputs,tx_type):
    tx_type=str(tx_type).lower()
    if tx_type=='legacy':
        fee_rate=int(num_of_inputs) * 146 + int(num_of_outputs) * 33 +10
        
    elif tx_type=='segwit':
        fee_rate= int(num_of_inputs) * 68.5 + int(num_of_outputs) * 31 +10
    return int(fee_rate)

