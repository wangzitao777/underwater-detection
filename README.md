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

    git clone git@github.com:ultralytics/ultralytics.git
    
2. Create a new environment and install the liberaries:

    python -m venv underwater_detection
    
    pip install -r requirements.txt

## Usage

1. Prepare your dataset

3. [Include any relevant screenshots or gifs to demonstrate usage]
4. [Add any additional instructions or guidelines]

## Contributing

We welcome contributions from the community! If you'd like to contribute to the project, please follow these guidelines:

1. Fork the repository
2. Create a new branch
3. Make your changes and commit them
4. Push your changes to your forked repository
5. Submit a pull request with a clear description of your changes

## License

This project is licensed under the [name of the license]. Please see the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Acknowledge any contributors or resources that have been used]
- [Give credit to any external libraries, frameworks, or resources]

## Contact

If you have any questions, suggestions, or feedback, please feel free to reach out to us at [email address or other contact information]. We'd love to hear from you!

## Additional Information

[Include any additional information, such as project status, future plans, or relevant links]

[Optional: Add badges, such as build status or version number]

[Optional: Include a table of contents for easy navigation]

Thank you for using our project!
