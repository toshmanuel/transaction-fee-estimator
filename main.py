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
def fee(inputs:int,outputs:int,tx_type:str):
    from api.v1.fee import get_fee
    fee=get_fee(inputs,outputs,tx_type)
    return {'Transaction fee':int(fee)}

@app.get(api_version("/fee_in_usd"))
def fee_conversion(fee):
    from api.v1.txfee_conversion import txfee_to_usd
    usd_conversion=txfee_to_usd(fee)
    return {"fee_to_usd":usd_conversion}


@app.post(api_version("/fee-target-block"))
def fee_rate(inputs:int,outputs:int,tx_type:str, target_block:int):
    from api.v1.fee_rate_per_confirmation import calculate_fee_base_on_block_confirmation_target
    fee = calculate_fee_base_on_block_confirmation_target(inputs,outputs,tx_type, target_block)

    return {'Transaction fee':fee}