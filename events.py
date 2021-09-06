subscribers = dict()

def subscribe(event_type: str, fn):
    """
    update subscribers if not found in subscribers dict
    """
    if not event_type in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)


def post_event(event_type: str, sheet, data):
    """
    run function based on event_type if found in subscribers
    """
    if not event_type in subscribers:
        return
    for fn in subscribers[event_type]:
        fn(sheet, data)


def return_data_event(event_type: str, data):
    """
    run data return function based on event_type if found in subscribers
    return data from said function
    """
    if not event_type in subscribers:
        return
    for fn in subscribers[event_type]:
        data_returned = fn(data)
        return data_returned
