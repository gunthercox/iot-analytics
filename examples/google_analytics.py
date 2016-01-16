from iot_analytics.interfaces import GoogleAnalyticsInterface
from iot_analytics.models import Event


'''
This is an example for how to use the python iot_analytics
package to record data to a self hosted database.
'''

# Create a new interface
interface = GoogleAnalyticsInterface()

# Create an event object
event = Event("ROBOT1-ID", {
    'category': 'button',
    'action': 'pressed',
    'label': 'momentary',
    'value': 10
})

# Add the event via the interface
interface.add(event)
