from requests import *

def get_fee(num_of_inputs,num_of_outputs,tx_type,fee_rate=1.02):
    tx_type=str(tx_type).lower()
    if tx_type=='legacy':
        vsize=int(num_of_inputs) * 146 + int(num_of_outputs) * 33 +10
        
    elif tx_type=='segwit':
        vsize= int(num_of_inputs) * 68.5 + int(num_of_outputs) * 31 +10
    return fee_rate * vsize

