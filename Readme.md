# MQTTHelloWorld - Python

This is a **"Hello World"** project using **MQTT** in **Python**. The application connects to an MQTT broker, subscribes to a topic, and receives messages published to that topic. It also exposes a RESTful API using Flask, with automatically generated interactive documentation using **Swagger UI**.

## Features

- Implementation of an **MQTT** client that connects to a public broker (HiveMQ).
- Subscription to the `lesly/topic` topic and reception of messages.
- Exposure of a RESTful API using Flask.
- **Swagger UI** to visualize and test the API.
- Messages received on the MQTT topic are displayed in the console.

## Requirements

- Python 3.6 or higher
- Flask
- Flask-RESTful
- Flasgger for Swagger documentation
- Paho-MQTT for MQTT interaction

## Installation

1. Clone the repository:
```bash
git clone https://github.com/lessalcu/MQTT-HolaMundo.git
cd mqttholamundo
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate # On Linux/Mac
venv\Scripts\activate # On Windows
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. The application will run on `http://localhost:5000`. You can access Swagger UI at `http://localhost:5000/apidocs/`.

## Usage

- **Path for HTML file**:
When accessing `http://localhost:5000/`, the `index.html` file will be served if it exists in the `wwwroot` folder.

- **RESTful endpoint**:
The API has an endpoint available at `/` that responds to **GET** requests and returns a `Hello, World!` message:

**Example response**:
```json
{
"message": "Hello, World!"
}
```

- **MQTT**:
The application connects to HiveMQ's public MQTT broker at `broker.hivemq.com`, subscribes to the `test/topic` topic, and displays received messages in the console. Messages will be printed as:

```bash
Received message from test/topic: Hello, MQTT World!
```
### Download the image from Docker Hub

1. To download the image from Docker Hub:
```bash
docker pull lssalas/hello-world-mqtt:latest
```

## Notes

This project serves as a basic example to understand how to use **MQTT** in Python, and how to integrate this protocol with a RESTful API using **Flask**. Integration with **Swagger UI** allows you to easily explore and test the API. It also connects to a public HiveMQ broker to demonstrate how to handle messages in real time.
