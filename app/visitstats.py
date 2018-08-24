# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Airport data provided by David Megginson (http://ourairports.com/data/).

import csv
import io
import os
import MySQLdb

# These environment variables are configured in app.yaml.
# CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
# CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
# CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')
CLOUDSQL_CONNECTION_NAME = 'business-dashboard-212916:us-east1:dashboard'
CLOUDSQL_USER = 'root'
CLOUDSQL_PASSWORD = 'root'

class Visitstats(object):
  """An interface for reading data about dashboard numbers."""

  def __init__(self):
    self.test = 1
    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    # will be set to 'Google App Engine/version'.
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        # Connect using the unix socket located at
        # /cloudsql/cloudsql-connection-name.
        cloudsql_unix_socket = os.path.join(
            '/cloudsql', CLOUDSQL_CONNECTION_NAME)

        db = MySQLdb.connect(
            unix_socket=cloudsql_unix_socket,
            user=CLOUDSQL_USER,
            passwd=CLOUDSQL_PASSWORD)

    # If the unix socket is unavailable, then try to connect using TCP. This
    # will work if you're running a local MySQL server or using the Cloud SQL
    # proxy, for example:
    #
    #   $ cloud_sql_proxy -instances=your-connection-name=tcp:3306
    #
    else:
        db = MySQLdb.connect(
            host='127.0.0.1', user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD)
    """Simple request handler that shows all of the MySQL variables."""
    # self.response.headers['Content-Type'] = 'text/plain'

    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute('SHOW VARIABLES')

    # for r in cursor.fetchall():
    #     self.response.write('{}\n'.format(r))

# Connect to my sql database here
  def get_dept_with_max_sitvisits(self, visitDate):
# Get department with max site visits on a specific visit date
    return ('Building Materials')
  def get_dept_with_max_orders(self, orderDate):
# Get department with highest orders on a specific date
    return ('Hardlines')
  def get_dept_with_max_conv(self, orderDate):
# Get department with highest conversion on a specific date
    return ('Decor')
def get_dept_with_max_GD(self, orderDate):
# Get department with highest conversion on a specific date
    return ('Decor')
def get_MC_with_max_visits(self, orderDate):
# Get department with highest conversion on a specific date
    return ('Decor')        
def get_top10_with_max_GD(self, orderDate):
# Get department with highest conversion on a specific date - getTop10ProductsWithMaxGD
    return ('Top 10 products are')       
def get_MC_with_max_GD(self, orderDate):
# Get department with highest conversion on a specific date - getMCWithMaxGD
    return ('Decor')       
def get_spcial_buy(self):
# Get department with highest conversion on a specific date - getSpecialBuy
    return ('Decor')                   
def get_noOfSKUs_special_buy(self):
# Get department with highest conversion on a specific date - getNoOfSKUsSpecialBuy
    return ('Decor')                   
def get_todays_conv(self, orderDate):
# Get department with highest conversion on a specific date - getTodaysConv
    return ('Decor')  
def get_MC_with_max_conv(self, orderDate):
# Get department with highest conversion on a specific date - getMCWithMaxConv
    return ('Decor')                       