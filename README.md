# BLIP Image Captioning API

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-0.68.0-blue.svg)](https://fastapi.tiangolo.com/)
[![Hugging Face Transformers](https://img.shields.io/badge/transformers-4.19.0-blue.svg)](https://huggingface.co/docs/transformers/index)

BLIP Image Captioning API is a powerful and easy-to-use API that generates descriptive captions for images using the BLIP (Bootstrapping Language-Image Pre-training) model from Hugging Face Transformers. With just a few lines of code, you can integrate image captioning functionality into your applications.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [API Endpoint](#api-endpoint)
  - [Request](#request)
  - [Response](#response)
- [Configuration](#configuration)
- [Logging](#logging)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- 🖼️ Generate captions for images automatically
- 📝 Support for conditional image captioning with optional text input
- 🚀 Easy integration with FastAPI and Hugging Face Transformers
- 🐳 Containerization with Docker for easy deployment and scalability
- 📖 Comprehensive documentation and code examples

### Key features of the "blip-image-captioning-api" project:

1. FastAPI Integration: The API is built using FastAPI, a modern and fast web framework for building APIs in Python. FastAPI provides automatic API documentation, request validation, and high performance out of the box.
2. BLIP Model: The project utilizes the pre-trained BLIP model from Hugging Face Transformers, which has been trained on a large dataset of image-caption pairs. BLIP achieves impressive results in generating accurate and coherent captions for a wide range of images.
3. Easy Image Upload: The API allows users to upload images via a simple HTTP POST request, making it convenient to integrate image captioning functionality into various applications.
4. Conditional Image Captioning: In addition to generating captions based solely on the image content, the API supports conditional image captioning. Users can provide an optional text input along with the image to guide the caption generation process.
5. Containerization with Docker: The project is containerized using Docker, ensuring a consistent and reproducible environment for running the API. Docker simplifies the deployment process and makes it easy to scale the application.
6. Comprehensive Documentation: The repository includes detailed documentation on how to set up, run, and interact with the image captioning API. It provides step-by-step instructions, code examples, and explanations of the project's architecture and components.
7. Extensibility and Customization: The codebase is modular and well-structured, allowing developers to easily extend and customize the API according to their specific requirements. The project serves as a solid foundation for building more advanced image captioning applications.

Whether you are a developer interested in exploring image captioning techniques, a researcher studying deep learning for computer vision, or someone looking to integrate image captioning functionality into your application, the "blip-image-captioning-api" repository provides a valuable resource and starting point. It demonstrates the power of combining FastAPI and the BLIP model to create a robust and efficient image captioning API.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/askaresh/blip-image-captioning-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd blip-image-captioning-api
   ```

3. Build the Docker image:

   ```bash
   docker build -t blip-image-captioning-api .
   ```

4. Run the Docker container:

   ```bash
   docker run -p 8000:8000 blip-image-captioning-api
   ```

   The API will be accessible at `http://localhost:8000`.

## Usage

### API Endpoint

The API provides a single endpoint for generating image captions:

- `POST /caption`: Generate a caption for an image.

### Request

To generate a caption for an image, send a `POST` request to the `/caption` endpoint with the following parameters:

- `image` (required): The image file to generate a caption for. The image should be sent as a multipart form data.
- `text` (optional): An optional text input to guide the caption generation process. This can be used for conditional image captioning.

Example using cURL:

```bash
curl -X POST -F "image=@path/to/image.jpg" -F "text=optional text input" http://localhost:8000/caption
```

### Response

The API will respond with a JSON object containing the generated caption:

```json
{
  "caption": "a person riding a bike on a city street"
}
```

## Configuration

The configuration settings for the API can be found in the `config.py` file. You can modify the following settings:

- `blip_model_name`: The name of the BLIP model to use for image captioning. Default is `"Salesforce/blip-image-captioning-large"`.

## Logging

The API uses the Python logging module for logging. The logging configuration can be found in the `logging.conf` file. You can customize the log levels, handlers, and formatters according to your needs.

## Architecture

The architecture of the BLIP Image Captioning API can be represented using the following ASCII art diagram:

```
+-----------------+
|     Client      |
+-----------------+
        |
        | HTTP POST
        | (Image + Optional Text)
        ▼
+-----------------+
|     FastAPI     |
+-----------------+
        |
        | Request
        ▼
+-----------------+
|   API Endpoint  |
+-----------------+
        |
        | Image Processing
        ▼
+-----------------+
|     Utility     |
|    Functions    |
+-----------------+
        |
        | Preprocessed Image
        ▼
+-----------------+
|  Model Loading  |
+-----------------+
        |
        | BLIP Model
        ▼
+-----------------+
|     Caption     |
|   Generation    |
+-----------------+
        |
        | Generated Caption
        ▼
+-----------------+
|    Response     |
|   Formatting    |
+-----------------+
        |
        | JSON Response
        ▼
+-----------------+
|     Client      |
+-----------------+
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [BLIP Model](https://huggingface.co/Salesforce/blip-image-captioning-large)