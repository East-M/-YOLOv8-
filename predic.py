from ultralytics import YOLO

# 导入模型
model = YOLO('weights/best8.pt')

# 预测
model.predict("datasets/CamouflagedTarget/test",save=True)