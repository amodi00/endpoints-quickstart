# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from flask import Flask
from flask import request
from visitstats import Visitstats

app = Flask(__name__)
  
@app.route('/getDeptWithMaxSiteVisits', methods=['GET'])
def getDeptWithMaxSiteVisits():
  visitstats_util = Visitstats()
  visit_date = request.args.get('visitDate')
  if visit_date is None:
    return 'Provide a valid visit date',400
  dept_name = visitstats_util.get_dept_with_max_sitvisits(visit_date)
  return dept_name, 200

@app.route('/getDeptWithMaxOrders', methods=['GET'])
def getDeptWithMaxOrders():
  visitstats_util = Visitstats()
  visit_date = request.args.get('visitDate')
  if visit_date is None:
    return 'Provide a valid visit date',400
  dept_name = visitstats_util.get_dept_with_max_orders(visit_date)
  return dept_name, 200

@app.route('/getDeptWithMaxConversion', methods=['GET'])
def getDeptWithMaxConversion():
  visitstats_util = Visitstats()
  visit_date = request.args.get('visitDate')
  if visit_date is None:
    return 'Provide a valid visit date',400
  dept_name = visitstats_util.get_dept_with_max_conv(visit_date)
  return dept_name, 200

@app.route('/getDeptWithMaxGD', methods=['GET'])
def getDeptWithMaxGD():
  visitstats_util = Visitstats()
  visit_date = request.args.get('visitDate')
  if visit_date is None:
    return 'Provide a valid visit date',400
  dept_name = visitstats_util.get_dept_with_max_GD(visit_date)
  return dept_name, 200

@app.route('/getMCWithMaxVisits', methods=['GET'])
def getMCWithMaxVisits():
  visitstats_util = Visitstats()
  visit_date = request.args.get('visitDate')
  if visit_date is None:
    return 'Provide a valid visit date',400
  dept_name = visitstats_util.get_MC_with_max_visits(visit_date)
  return dept_name, 200

# Edit here
@app.route('/getTop10ProductsWithMaxGD', methods=['GET'])
def getTop10ProductsWithMaxGD():
  visitstats_util = Visitstats()
  visit_date = request.args.get('visitDate')
  if visit_date is None:
    return 'Provide a valid visit date',400
  dept_name = visitstats_util.get_top10_with_max_GD(visit_date)
  return dept_name, 200

@app.route('/getMCWithMaxGD', methods=['GET'])
def getMCWithMaxGD():
  visitstats_util = Visitstats()
  visit_date = request.args.get('visitDate')
  if visit_date is None:
    return 'Provide a valid visit date',400
  dept_name = visitstats_util.get_MC_with_max_GD(visit_date)
  return dept_name, 200

@app.route('/getSpecialBuy', methods=['GET'])
def getSpecialBuy():
  visitstats_util = Visitstats()
  dept_name = visitstats_util.get_spcial_buy()
  return dept_name, 200

@app.route('/getNoOfSKUsSpecialBuy', methods=['GET'])
def getNoOfSKUsSpecialBuy():
  visitstats_util = Visitstats()
  dept_name = visitstats_util.get_noOfSKUs_special_buy()
  return dept_name, 200

@app.route('/getTodaysConv', methods=['GET'])
def getTodaysConv():
  visitstats_util = Visitstats()
  visit_date = request.args.get('visitDate')
  if visit_date is None:
    return 'Provide a valid visit date',400
  dept_name = visitstats_util.get_todays_conv(visit_date)
  return dept_name, 200

@app.route('/getMCWithMaxConv', methods=['GET'])
def getMCWithMaxConv():
  visitstats_util = Visitstats()
  visit_date = request.args.get('visitDate')
  if visit_date is None:
    return 'Provide a valid visit date',400
  dept_name = visitstats_util.get_MC_with_max_conv(visit_date)
  return dept_name, 200


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
