[![Build Status](https://travis-ci.org/FaithOroone/Fast-food-fast.svg?branch=develop)](https://travis-ci.org/FaithOroone/Fast-food-fast) [![Coverage Status](https://coveralls.io/repos/github/FaithOroone/Fast-food-fast/badge.svg?branch=add_an_order)](https://coveralls.io/github/FaithOroone/Fast-food-fast?branch=add_an_order) [![Maintainability](https://api.codeclimate.com/v1/badges/cebadc11188adbfb2708/maintainability)](https://codeclimate.com/github/FaithOroone/Fast-food-fast/maintainability)

# Fast-food-fast-API

## Description
Fast-Food-Fast is a food delivery service app for a restaurant which enables users to place an order for food, get a list of orders, fetch a specific order and update the order status.
21/09/2018

### Required Features(Endpoints)
Endpoint Functionality
* POST /api/v1/orders Place an order for food.
* GET /api/v1/orders Get a list of orders.
* GET /api/v1/orders/<int:orderId> Fetch a specific order .
* PUT /api/v1/orders/<int:orderId> update the order status.

### Prerequisites
Python/Flask framework

### Setup/Installation Requirements
* Install Python
* Install pip
* Setup a virtual environment
* pip install Flask
* pip install pytest
* Run App Run python app.py on command prompt
* View the api on http://127.0.0.1:5000/api/v1/api/order
* Test it's usage with postman

### License
Copyright (c) 2018