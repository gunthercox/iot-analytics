import zorg
import time

def work (my):

    # Toggle the led
    my.touch_sensor.send(
        category='button',
        action='pressed',
        label='momentary',
        value='30'
    )
    print("ran")

    # Wait 1 second before doing it again
    time.sleep(1)

robot = zorg.robot({
    "connections": {
        "analytics": {
            "adaptor": "iot_analytics.GoogleAnalytics",
            "property_id": "UA-12573345-11",
        },
    },
    "devices": {
        "touch_sensor": {
            "connection": "analytics",
            "driver": "iot_analytics.Event",
        }
    },
    "name": "example", # Give your robot a unique name
    "work": work, # The method (on the main level) where the work will be done
})

robot.start()
