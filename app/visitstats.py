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

class Visitstats(object):
  """An interface for reading data about dashboard numbers."""

  def __init__(self):
    self.test = 1
    
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