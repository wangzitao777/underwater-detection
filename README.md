# Underwater Detection

## Description

This project is designed to provide a YOLOv8 based object dectection method for Forward-Looking Sonar (FLS) images. It aims to integrate YOLOv8 with attention mechanism and make detection more robust with a preprocessing module.

## Features

- A threshold-adaptive judgment criterion is proposed to limit the influences of artifacts. And contrast limited adaptive histogram equalization (CLAHE) is used to improve the contrast of FLS images and make them easier to interpret. In addition, a wiener filter is applied further to reduce the effects of noise and improve the overall image quality.
- To further suppress irrelevant noise and extract useful features from FLS images, convolutional block attention module (CBAM) is added to the network head while not increasing computational complexity.
- Sufficient experiments are conducted to ensure the reliability of the results. And the real-time performance of the model has been verified on hardware.

## Installation

Our experiments were performed on a Ubuntu 20.04 personal computer with GTX1660 and 12th Intel i5-core. It's recommended that install our project via pip.
1. Clone the YOLOv8 project:
```bash
git clone git@github.com:ultralytics/ultralytics.git
```
2. Create a new environment and install the liberaries:
```bash
python -m venv underwater_detection    
pip install -r requirements.txt
```
## Preparation & Usage

1. Prepare your dataset. Several public FLS image datasets are given in additional information.

2. Directly use Command Line Interface (CLI) with a yolo command:
```bash
yolo predict model=demo/demo.pt source='[Your Picture]'
```
Or train your own model:
```bash
yolo task=detect mode=train model=yolov8n.yaml batch=16 epoch=300 workers=16 device=0 optimizer='Adam' lr0=1e-3 lrf=1e-5
```
More information on YOLO can be found in [YOLOv8](https://github.com/ultralytics/ultralytics)

3. A demo result is shown:
![image](https://github.com/wangzitao777/underwater-detection/blob/main/demo/demo.jpg)

## Contributing

We welcome contributions from the community! If you'd like to contribute to the project, please follow these guidelines:

1. Fork the repository
2. Create a new branch
3. Make your changes and commit them
4. Push your changes to your forked repository
5. Submit a pull request with a clear description of your changes

## Contact

If you have any questions, suggestions, or feedback, please feel free to reach out to us at wangzitao@sjtu.edu.cn. We'd love to hear from you!

## Additional Information

Several dataset:



Thank you for using our project!
