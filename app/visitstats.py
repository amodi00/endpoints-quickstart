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
  """An interface for reading data about airports."""

  def __init__(self):
# Connect to my sql database here
  def get_max_sitvisits_dept(visitDate):
# Get department with max site visits on a specific visit date
    return 'Building Materials'
  def get_max_orders_dept(orderDate) 
# Get department with highest orders on a specific date
    return 'Hardlines'
  def get_max_conv_dept(orderDate) 
# Get department with highest conversion on a specific date
    return 'Decor'