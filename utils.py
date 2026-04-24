import os

EN_US = os.getenv("LANG") != "zh_CN.UTF-8"
API_TRANS = os.getenv("api_caiyun")
KEY_TRANS = os.getenv("apikey_caiyun")
if not (API_TRANS and KEY_TRANS):
    print("请检查环境变量")
    exit()
