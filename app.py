from flask import Flask
from flask_restful import Api, Resource
from flasgger import Swagger
import paho.mqtt.client as mqtt

# Flask app and Swagger configuration
app = Flask(__name__)
api = Api(app)
swagger = Swagger(app, template_file='swagger.yaml')

# MQTT client configuration
broker = "broker.hivemq.com"
port = 1883
topic = "lesly/topic"

client = mqtt.Client(protocol=mqtt.MQTTv311)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Received message from {msg.topic}: {msg.payload.decode()}")

client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port, 60)

# Flask REST API resource
class HelloWorld(Resource):
    def get(self):
        """
        A simple GET endpoint
        ---
        tags:
          - HelloWorld
        responses:
          200:
            description: Returns a hello world message
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: Hello, MQTT World!
        """
        # Publish a message to the MQTT topic
        client.publish(topic, "Hello, MQTT World!")
        return {'message': 'Hello, MQTT World!'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    client.loop_start()
    print("Swagger UI available at http://0.0.0.0:5000/apidocs/")
    app.run(host='0.0.0.0', port=5000)