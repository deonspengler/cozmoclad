# Copyright (c) 2016-2017 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Autogenerated python message buffer code.
Source: clad/types/facialExpressions.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ../coretech/vision/clad/src/ -o ../generated/cladPython// clad/types/facialExpressions.clad
"""

from __future__ import absolute_import
from __future__ import print_function

def _modify_path():
  import inspect, os, sys
  search_paths = [
    '../..',
    '../../../../tools/message-buffers/support/python',
  ]
  currentpath = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())))
  for search_path in search_paths:
    search_path = os.path.normpath(os.path.abspath(os.path.realpath(os.path.join(currentpath, search_path))))
    if search_path not in sys.path:
      sys.path.insert(0, search_path)
_modify_path()

import msgbuffers

Anki = msgbuffers.Namespace()
Anki.Vision = msgbuffers.Namespace()

class FacialExpression(object):
  "Automatically-generated int_8 enumeration."
  Unknown   = -1
  Neutral   = 0
  Happiness = 1
  Surprise  = 2
  Anger     = 3
  Sadness   = 4
  Count     = 5

Anki.Vision.FacialExpression = FacialExpression
del FacialExpression


