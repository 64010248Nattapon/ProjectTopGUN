from fastapi import APIRouter
from fastapi_mqtt.fastmqtt import FastMQTT
from fastapi_mqtt.config import MQTTConfig
import time

mqtt_config = MQTTConfig(
    host="192.168.1.50",
    port=1883,
    keepalive=600,
    username="admin",
    password="server123"
)

# FastMQTT instance
fast_mqtt = FastMQTT(config=mqtt_config)

# API Router
router = APIRouter()

# Initialize FastMQTT with the router
fast_mqtt.init_app(router)

from server.database import (
    add_water,
)
from server.models.water import (
    ErrorResponseModel,
    ResponseModel,
    WaterSchema,
)

@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    fast_mqtt.client.subscribe("/TGR_22")

    #subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)

@fast_mqtt.on_message()
async def message(client, topic, payload, qos, properties):
    print("Received message: ",topic, payload.decode(), qos, properties)
    
@fast_mqtt.subscribe("/TGR_22/#")
async def message_to_topic(client, topic, payload, qos, properties):
    message = payload.decode()
    jsondata = {
        "station_id":"1",
        "Date":"56",
        "w_height":float(message),
        "w_discharge":0
        
    }
    await add_water(jsondata)
    print("Received message to specific topic: ", topic, payload.decode(), qos, properties)

@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

@fast_mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)


@router.get("/", response_description="test publish to mqtt")
async def publish_hello():
    fast_mqtt.publish("TGR_22/water", "get") #publishing mqtt topic

    return {"result": True,"message":"Published" }
