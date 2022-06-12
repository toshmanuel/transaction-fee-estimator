<h1 align="center">Transaction Fee Estimator </h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
</p>

> A Python application that allows users to have an idea of how much to pay for their bitcoin transaction to avoid overpaying or underpaying. This
application provides users with APIs for use with any GUI or other backend applications.

### Setup Environment
1. Clone repository
```shell
git clone https://github.com/toshmanuel/transaction-fee-estimator.git
```
2. Go into environment
```shell
source env/bin/activate
```
3. Install requirements
```shell
pip install -r requirements.txt
```
5. Start server
```shell
uvicorn main:app --reload
```
### API Documentation
1. **Redoc** - *{{base_url}}/redoc*

