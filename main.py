from fastapi import FastAPI
from api.utils.api_version import api_version


app = FastAPI(
    title="BTC_TRANSACTION_FEE_ESTIMATOR",
    version="1.0.0",
)

@app.get('/ping')
def ping():
    return {'status': 'ok'}

@app.post(api_version("/fee_rate"))
def fee_rate(inputs:int,outputs:int,tx_type:str):
    from api.v1.feerate_per_vbytes import get_feerate_per_vbytes
    fee_rate=get_feerate_per_vbytes(inputs,outputs,tx_type)
    return {'Transaction fee':int(fee_rate)}

@app.get(api_version("/fee_in_usd"))
def fee_conversion(fee):
    from api.v1.txfee_conversion import txfee_to_usd
    usd_conversion=txfee_to_usd(fee)
    return {"fee_to_usd":usd_conversion}
