# Exercises

Detecting Change
You have a table containing data on the weather. Each date has a boolean indicating if
it rained (TRUE) or did not rain (FALSE). Query the table to determine the dates in
which the weather became bad (i.e. when the weather changed from FALSE to TRUE)
Dataset:

weather
Date was_rainy
1/1/20 FALSE
1/2/20 TRUE
1/3/20 TRUE
1/4/20 FALSE
1/5/20 FALSE
1/6/20 TRUE
1/7/20 FALSE
1/8/20 TRUE
1/9/20 TRUE
1/10/20 TRUE

Expected Result:
date was_rainy
1/2/20 TRUE
1/6/20 TRUE
1/8/20 TRUE


Seasons Problem
You have a table containing a large numper of orders over several ears - a sample is
shown below. Each order has a date attribute that you will need to use to determine the
season in which this order was placed. For reference see the table containing the dates
in whicn earn season talls

Spring: March 19th - June 19th
Summer: June 20th - September 21st
Fall: September 22nd - December 20th
Winter: December 20th - March 18th

spring = 19/03/-- | 19/06/--
summer = 20/06/-- | 21/09/--
fall = 22/09/--   | 20/12/--
winter = 21/12/-- | 18/03/--

Customer Order Status
You have a data source containing order-line data (each order can have multiple order
lines based on the number of products ordered under that specific order). An order line
item can be in one of the following three statuses: Pending, Shipped, Cancelled. You
want to determine the status of the overall order based on the statuses of each
individual order line item for that order. For example, if you have three items in order
number 1234, and two of them are marked "Shipped" but one is marked "Pending" then
the overall order status is Pending. If all are marked "Shipped" then the Status is
Shipped*
Dataset:
containing order-line data
three statuses: Pending, Shipped, Cancelled
status of the overall order 





# Instructions
Into the termirnal/powershell run the following commands

# Create enviroment
python3 -m venv exercises

# Accesing
$ virtualenv exercises

# Activate the virtualenv - MacOs & Linux
$ source exercises/bin/activate

# Activate the virtualenv - Windows
$ exercises\Scripts\activate

# Installing packages
pip3 install Flask Werkzeug Jinja2

# Run the Flask development server
python3 -m flask run

After running all those commands you should have a line like this
' * Running on http://127.0.0.1:5000'

Click on the address 
A new window  of your default web browser should be opened
You should be able to play around with the app
All this problems are solved within app
There is also some CSV test files to play around with the app located in the 'examples' folder

Have fun!

# Stoping the app 
Ctrl+C

# Stop the virtualenv
$ deactivate




# Index of Test

Detecting Change
test_detecting_change - Given a data, it's expeted to get a dictionary	

Seasons Problem
test_spring - Test data for getting 'Spring ' given a date
test_summer - Test data for getting 'Spring ' given a date
test_fall - Test data for getting 'fall' given a date
test_winter - Test data for getting 'winter ' given a date""" 	 

Customer Order Status
test_PENDING_output
Test data for getting 'PENDING' with data ['SHIPPED', 'SHIPPED', 'PENDING']

test_SHIPPED_output
Test data for getting 'SHIPPED' with data ['SHIPPED', 'CANCELLED', 'CANCELLED']	

test_CANCELLED_output
Test data for getting 'CANCELLED	 with data ['CANCELLED', 'CANCELLED']