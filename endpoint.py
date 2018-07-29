from flask import Flask, request, make_response, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def endpoint():
    """ An example endpoint to use with ChainSentinel.
        Receives POST requests and handles the required authentication
        Sends received data to the _handle_data function
        Returns 200 - OK in case of success and 500 - ERROR otherwise
    """
    if request.method == 'GET':
        return 'Simple Endpoint for <a href="https://chainsentinel.co">Chain Sentinel</a>'

    try:
        data = request.get_json()
        if 'permission' in data:
            auth_reply = {
                'permission': 'given',
                'nonce': data['nonce']
            }
            response = make_response(jsonify(auth_reply), 200)
            return response
        else:
            _handle_data(data)
            return make_response("OK", 200)

    except Exception as e:
        raise e
        return make_response("ERROR", 500)


def _handle_data(data):
    """This function exemplifies how received data can be handled
    Received data is structured in the following way:
    {
          "event_type": "{value}",
          "contract_hash": "{value}",
          "tx_hash": "{value}",
          "block_number": 123,
          "event_payload":  {
            "type": "Array",
            "value": [
              {
                "type": "ByteArray",
                "value": "7472616e73666572"
              },
              {
                "type": "Integer",
                "value": 1
              },
              {
                "type": "String",
                "value": "a given string"
              },
              {
                "type": "Boolean",
                "value": "true"
              }
            ]
          },
          "execution_success": True,
          "test_mode": "{value}",
          "extra": {'network': "{value}"}
        }
    DOCS: https://chainsentinel.co/dashboard/docs/webhooks
    """
    contract_hash = data['contract_hash']
    event_type = data['event_type']
    event_payload = data['event_payload']
    if event_payload['type'] == 'Array':
        for item in event_payload['value']:
            if item['type'] == 'ByteArray':
                try:
                    item['value'] = _decode(str(item['value']))
                except Exception:
                    pass

    elif event_payload['type'] == 'ByteArray':
        if event_payload['type'] == 'ByteArray':
            try:
                event_payload['value'] = _decode(str(event_payload['value']))
            except Exception:
                pass
    print(data)

def _decode(hex):
    """Decodes an hex encoded string"""
    return bytearray.fromhex(hex).decode()
