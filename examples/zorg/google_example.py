import zorg
import time

def work (robot):

    # Send a button pressed event
    robot.touch_sensor.send(
        category='button',
        action='pressed',
        label='momentary',
        value='30'
    )
    print("button press detected")

    # Wait 1 second before doing it again
    time.sleep(1)

robot = zorg.robot({
    "connections": {
        "analytics": {
            "adaptor": "iot_analytics.apps.zorg.GoogleAnalytics",
            "property_id": "UA-12573345-12",
            "client_id": "d944d45c-9c92-46a2-97be-9ba07d922227",
        },
    },
    "devices": {
        "touch_sensor": {
            "connection": "analytics",
            "driver": "iot_analytics.apps.zorg.drivers.Event",
        }
    },
    "name": "example", # Give your robot a unique name
    "work": work, # The method (on the main level) where the work will be done
})

robot.start()
