[![Build Status](https://travis-ci.org/FaithOroone/Fast-food-fast.svg?branch=develop)](https://travis-ci.org/FaithOroone/Fast-food-fast) [![Maintainability](https://api.codeclimate.com/v1/badges/cebadc11188adbfb2708/maintainability)](https://codeclimate.com/github/FaithOroone/Fast-food-fast/maintainability) [![Coverage Status](https://coveralls.io/repos/github/FaithOroone/Fast-food-fast/badge.svg?branch=develop-api)](https://coveralls.io/github/FaithOroone/Fast-food-fast?branch=develop-api)
# Fast-food-fast
Fast-Food-Fast is a food delivery service app for a restaurant.

## Description
Fast-Food-Fast is a food delivery service app for a restaurant which enables users
to create user accounts by signup up and then login to the account, place an order for food, get list of orders, get a specific order,update the status of an order, get the menu, add food option to the menu and view the order history  for a particular user.
21/09/2018

### Required Features(Endpoints)
Endpoint Functionality.

* POST /auth/signup Register a user
* POST /auth/login  Login a user
* POST /api/v2/users/orders Place an order for food.
* GET /api/v2/users/orders Get the order history for a particular user.
* GET /api/v2/orders Get a list of orders.
* GET /api/v2/orders/<int:orderId> Fetch a specific order .
* PUT /api/v2/orders/<int:orderId> update the order status.
* GET /api/v2/menu  Get available menu.
* POST /api/v2/menu Add a meal option to the menu.

## Technologies Used
* postgresql database.
* python

### Prerequisites
Python/Flask framework

### License
Copyright (c) 2018 Orone Faith Eunice

