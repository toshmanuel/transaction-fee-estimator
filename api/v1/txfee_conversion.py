from requests import *
from decouple import config


def txfee_to_usd(fee):
    fee=int(fee)
    accesskey=config('ACCESS_KEY')
    tnx_pub_req = Session().post(
            url=f"http://api.coinlayer.com/api/live?access_key={accesskey}")
    one_btc_to_dollar=tnx_pub_req.json()['rates']['BTC']
    fee_to_usd= (fee/100000000)*int(one_btc_to_dollar)
    return (f'${fee_to_usd}')
