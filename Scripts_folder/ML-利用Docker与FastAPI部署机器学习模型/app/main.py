from fastapi import FastAPI
from pydantic import BaseModel
import pickle 
import os

# 定义输入样式.     # df.columns = ['Cement', 'Blast_Furnace_Slag', 'Fly_Ash', 'Water', 'Superplasticizer', 'Coarse_Aggregate', 'Fine_Aggregate', 'Age', 'Strength']
class InputData(BaseModel):
    Cement: float                  # 水泥含量，类型为浮点数
    Blast_Furnace_Slag: float      # 高炉渣含量，类型为浮点数
    Fly_Ash: float                 # 粉煤灰含量，类型为浮点数
    Water: float                   # 水含量，类型为浮点数
    Superplasticizer: float        # 超级塑化剂含量，类型为浮点数
    Coarse_Aggregate: float        # 粗骨料含量，类型为浮点数
    Fine_Aggregate: float          # 细骨料含量，类型为浮点数
    Age: int                       # 混凝土龄期，类型为整数

# 数据输入示例.
"""
input_data = InputData(
    Cement=300.0,
    Blast_Furnace_Slag=100.0,
    Fly_Ash=50.0,
    Water=200.0,
    Superplasticizer=5.0,
    Coarse_Aggregate=1000.0,
    Fine_Aggregate=500.0,
    Age=28
)
"""

# 初始化一个FastAPI app.
app = FastAPI(title='Concrete Compress Strength Prediction API')

# 加载训练好的机器学习模型文件.
model_path = os.path.join("../model/", "RF_model.pkl")
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(data:InputData):
    # 用于预测的输入数据.
    input_features = [[data.Cement, data.Blast_Furnace_Slag, data.Fly_Ash, data.Water, data.Superplasticizer, data.Coarse_Aggregate, data.Fine_Aggregate, data.Age]]

    # 模型预测.
    prediction = model.predict(input_features)

    # 预测结果返回.
    return {"Predicted_Compress_Strength":prediction[0]}