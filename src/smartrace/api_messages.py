

def api_version_request() -> str:
    return '{"type":"api_version"}'

def pit_enter(car_id:int) -> str:
    return '{"type":"analog_pit_enter","data":{"controller_id":'+str(car_id)+ '}}'

def pit_leave(car_id:int) -> str:
    return '{"type":"analog_pit_leave","data":{"controller_id":'+str(car_id)+ '}}'

def race_start() -> str:
    return '{"type":"race_control","data":{"value":"start"}}'

def race_stop() -> str:
    return '{"type":"race_control","data":{"value":"stop"}}'

def lap(car_id:int, timestamp:int) -> str:
    return '{"type":"analog_lap","data":{"timestamp":'+str(timestamp)+',"controller_id":'+str(car_id)+ '}}'

