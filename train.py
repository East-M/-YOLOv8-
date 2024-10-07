from ultralytics import YOLO

# 加载模型
model = YOLO("yolov8n.yaml")  # "yolov8-CBAM.yaml"是加了注意力机制的模型，
                                  # "yolov8n.yaml"是未加注意力机制的模型

# 训练模型
model.train(data='datasets/CamouflagedTarget.yaml',epochs=2000,device='cpu')

# 验证模型
model.val()
