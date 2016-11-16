RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']
MONGO_PORT = 8888
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
