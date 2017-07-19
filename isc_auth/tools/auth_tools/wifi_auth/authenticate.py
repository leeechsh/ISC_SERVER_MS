import numpy as np
from preprocessing import WiFiFeatureExtractor
from sklearn.externals import joblib

MODEL_PATH = "new_model.pkl"
extractor = WiFiFeatureExtractor()
model = joblib.load(MODEL_PATH)
def authenticate(pc_wifi,mobile_wifi):
    '''
    PC_WIFI 字典格式，由原先定义的JSON直接转换
    MOBILE_WIFI 上同
    '''
    raw_record = {"pc":pc_wifi,"mobile":mobile_wifi}
    X = extractor.extract_feature_from_raw_record(raw_record)
    result = model.predict(np.array([X]))
    return result
