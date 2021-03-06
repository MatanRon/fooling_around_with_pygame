

class Event(object):
    """
    A superclass for any events that might be generated by an
    object and sent to the EventManager.
    """

    def __init__(self):
        self.name = "Generic event"

    def __str__(self):
        return self.name


class QuitEvent(Event):
    """
    Quit event.
    """

    def __init__(self):
        self.name = "Quit event"


class TickEvent(Event):
    """
    Tick event.
    """

    def __init__(self):
        self.name = "Tick event"


class InputEvent(Event):
    """
    Keyboard or mouse input event.
    """

    def __init__(self, unicodechar, clickpos):
        self.name = "Input event"
        self.char = unicodechar
        self.clickpos = clickpos

    def __str__(self):
        return '%s, char=%s, clickpos=%s' % (self.name, self.char, self.clickpos)


class InitializeEvent(Event):
    """
    Tells all listeners to initialize themselves.
    This includes loading libraries and resources.

    Avoid initializing such things within listener __init__ calls
    to minimize snafus (if some rely on others being yet created.)
    """

    def __init__(self):
        self.name = "Initialize event"

class onBoatLandingEvent(Event):
    """
    Tells all listeners that a parachutist land on the boat.
    """
    def __init__(self):
        self.name = "On boat landing event"

class onWaterLandingEvent(Event):
    """
    Tells all listeners that a parachutist land in the water.
    """
    def __init__(self):
        self.name = "On water landing event"

class ParachutistReachedSeaLevelEvent(Event):
    """
    Tells all listeners a parachutist reached sea level.
    """

    def __init__(self, ParachutistModel):
        self.name = "parachutist reached sea level event"
        self.parachutistModel = ParachutistModel
        psoition = ParachutistModel.getPosition()
        self.xPosition = psoition[0] # todo: fix where this field in use to call parachutistModel.getposition() insead
        # self.yPosition = position[1]
        # self.higt = ParachutistModel.getHight()
        # self.width = ParachutistModel.getwidth()


class EventManager(object):
    """
    We coordinate communication between the Model, View, and Controller.
    """

    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def RegisterListener(self, listener):
        """
        Adds a listener to our spam list.
        It will receive Post()ed events through it's notify(event) call.
        """

        self.listeners[listener] = 1

    def UnregisterListener(self, listener):
        """
        Remove a listener from our spam list.
        This is implemented but hardly used.
        Our weak ref spam list will auto remove any listeners who stop existing.
        """

        if listener in self.listeners.keys():
            del self.listeners[listener]

    def Post(self, event):
        """
        Post a new event to the message queue.
        It will be broadcast to all listeners.
        """

        if not isinstance(event, TickEvent):
            # print the event (unless it is TickEvent)
            print(str(event))

        for listener in list(self.listeners):
            listener.notify(event)