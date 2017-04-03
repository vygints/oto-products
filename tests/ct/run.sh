#! /bin/sh -x
# Component test for the products service. 
# Very dumb - create an product and verify there's an product for this product id.
# Assumes a fresh environment

curl -s -X POST -H "Content-Type:application/json" -d '{"name": "raspberryPi", "price": 35, "stock": 3 }' http://${APP_URL}:5000/product
curl -s http://${APP_URL}:5000/product | grep raspberryPi
