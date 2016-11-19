RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']
SERVER_NAME = None
MONGO_HOST = 'mongo'
MONGO_PORT = 27017
DOMAIN = {
    'product': {
        'schema': {
            'name': {
                'type': 'string',
                'unique': True,
                'required': True,
            },
            'price': {
                'type': 'number',
                'required': True,
            },
            'stock': {
                'type': 'integer',
                'required': True,
            }
        }
    }
}
