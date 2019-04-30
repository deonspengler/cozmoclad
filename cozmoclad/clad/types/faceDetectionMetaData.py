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
Source: clad/types/faceDetectionMetaData.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ../coretech/vision/clad/src/ -o ../generated/cladPython// clad/types/faceDetectionMetaData.clad
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

class SmileAmount(object):
  "Generated message-passing structure."

  __slots__ = (
    '_wasChecked', # bool
    '_amount',     # float_32
    '_confidence', # float_32
  )

  @property
  def wasChecked(self):
    "bool wasChecked struct property."
    return self._wasChecked

  @wasChecked.setter
  def wasChecked(self, value):
    self._wasChecked = msgbuffers.validate_bool(
      'SmileAmount.wasChecked', value)

  @property
  def amount(self):
    "float_32 amount struct property."
    return self._amount

  @amount.setter
  def amount(self, value):
    self._amount = msgbuffers.validate_float(
      'SmileAmount.amount', value, 'f')

  @property
  def confidence(self):
    "float_32 confidence struct property."
    return self._confidence

  @confidence.setter
  def confidence(self, value):
    self._confidence = msgbuffers.validate_float(
      'SmileAmount.confidence', value, 'f')

  def __init__(self, wasChecked=False, amount=0.0, confidence=0.0):
    self.wasChecked = wasChecked
    self.amount = amount
    self.confidence = confidence

  @classmethod
  def unpack(cls, buffer):
    "Reads a new SmileAmount from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('SmileAmount.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new SmileAmount from the given BinaryReader."
    _wasChecked = bool(reader.read('b'))
    _amount = reader.read('f')
    _confidence = reader.read('f')
    return cls(_wasChecked, _amount, _confidence)

  def pack(self):
    "Writes the current SmileAmount, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current SmileAmount to the given BinaryWriter."
    writer.write(int(self._wasChecked), 'b')
    writer.write(self._amount, 'f')
    writer.write(self._confidence, 'f')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._wasChecked == other._wasChecked and
        self._amount == other._amount and
        self._confidence == other._confidence)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._wasChecked, 'b') +
      msgbuffers.size(self._amount, 'f') +
      msgbuffers.size(self._confidence, 'f'))

  def __str__(self):
    return '{type}(wasChecked={wasChecked}, amount={amount}, confidence={confidence})'.format(
      type=type(self).__name__,
      wasChecked=self._wasChecked,
      amount=self._amount,
      confidence=self._confidence)

  def __repr__(self):
    return '{type}(wasChecked={wasChecked}, amount={amount}, confidence={confidence})'.format(
      type=type(self).__name__,
      wasChecked=repr(self._wasChecked),
      amount=repr(self._amount),
      confidence=repr(self._confidence))

Anki.Vision.SmileAmount = SmileAmount
del SmileAmount


class Gaze(object):
  "Generated message-passing structure."

  __slots__ = (
    '_wasChecked',    # bool
    '_leftRight_deg', # float_32
    '_upDown_deg',    # float_32
  )

  @property
  def wasChecked(self):
    "bool wasChecked struct property."
    return self._wasChecked

  @wasChecked.setter
  def wasChecked(self, value):
    self._wasChecked = msgbuffers.validate_bool(
      'Gaze.wasChecked', value)

  @property
  def leftRight_deg(self):
    "float_32 leftRight_deg struct property."
    return self._leftRight_deg

  @leftRight_deg.setter
  def leftRight_deg(self, value):
    self._leftRight_deg = msgbuffers.validate_float(
      'Gaze.leftRight_deg', value, 'f')

  @property
  def upDown_deg(self):
    "float_32 upDown_deg struct property."
    return self._upDown_deg

  @upDown_deg.setter
  def upDown_deg(self, value):
    self._upDown_deg = msgbuffers.validate_float(
      'Gaze.upDown_deg', value, 'f')

  def __init__(self, wasChecked=False, leftRight_deg=0.0, upDown_deg=0.0):
    self.wasChecked = wasChecked
    self.leftRight_deg = leftRight_deg
    self.upDown_deg = upDown_deg

  @classmethod
  def unpack(cls, buffer):
    "Reads a new Gaze from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('Gaze.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new Gaze from the given BinaryReader."
    _wasChecked = bool(reader.read('b'))
    _leftRight_deg = reader.read('f')
    _upDown_deg = reader.read('f')
    return cls(_wasChecked, _leftRight_deg, _upDown_deg)

  def pack(self):
    "Writes the current Gaze, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current Gaze to the given BinaryWriter."
    writer.write(int(self._wasChecked), 'b')
    writer.write(self._leftRight_deg, 'f')
    writer.write(self._upDown_deg, 'f')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._wasChecked == other._wasChecked and
        self._leftRight_deg == other._leftRight_deg and
        self._upDown_deg == other._upDown_deg)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._wasChecked, 'b') +
      msgbuffers.size(self._leftRight_deg, 'f') +
      msgbuffers.size(self._upDown_deg, 'f'))

  def __str__(self):
    return '{type}(wasChecked={wasChecked}, leftRight_deg={leftRight_deg}, upDown_deg={upDown_deg})'.format(
      type=type(self).__name__,
      wasChecked=self._wasChecked,
      leftRight_deg=self._leftRight_deg,
      upDown_deg=self._upDown_deg)

  def __repr__(self):
    return '{type}(wasChecked={wasChecked}, leftRight_deg={leftRight_deg}, upDown_deg={upDown_deg})'.format(
      type=type(self).__name__,
      wasChecked=repr(self._wasChecked),
      leftRight_deg=repr(self._leftRight_deg),
      upDown_deg=repr(self._upDown_deg))

Anki.Vision.Gaze = Gaze
del Gaze


class BlinkAmount(object):
  "Generated message-passing structure."

  __slots__ = (
    '_wasChecked',       # bool
    '_blinkAmountLeft',  # float_32
    '_blinkAmountRight', # float_32
  )

  @property
  def wasChecked(self):
    "bool wasChecked struct property."
    return self._wasChecked

  @wasChecked.setter
  def wasChecked(self, value):
    self._wasChecked = msgbuffers.validate_bool(
      'BlinkAmount.wasChecked', value)

  @property
  def blinkAmountLeft(self):
    "float_32 blinkAmountLeft struct property."
    return self._blinkAmountLeft

  @blinkAmountLeft.setter
  def blinkAmountLeft(self, value):
    self._blinkAmountLeft = msgbuffers.validate_float(
      'BlinkAmount.blinkAmountLeft', value, 'f')

  @property
  def blinkAmountRight(self):
    "float_32 blinkAmountRight struct property."
    return self._blinkAmountRight

  @blinkAmountRight.setter
  def blinkAmountRight(self, value):
    self._blinkAmountRight = msgbuffers.validate_float(
      'BlinkAmount.blinkAmountRight', value, 'f')

  def __init__(self, wasChecked=False, blinkAmountLeft=0.0, blinkAmountRight=0.0):
    self.wasChecked = wasChecked
    self.blinkAmountLeft = blinkAmountLeft
    self.blinkAmountRight = blinkAmountRight

  @classmethod
  def unpack(cls, buffer):
    "Reads a new BlinkAmount from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('BlinkAmount.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new BlinkAmount from the given BinaryReader."
    _wasChecked = bool(reader.read('b'))
    _blinkAmountLeft = reader.read('f')
    _blinkAmountRight = reader.read('f')
    return cls(_wasChecked, _blinkAmountLeft, _blinkAmountRight)

  def pack(self):
    "Writes the current BlinkAmount, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current BlinkAmount to the given BinaryWriter."
    writer.write(int(self._wasChecked), 'b')
    writer.write(self._blinkAmountLeft, 'f')
    writer.write(self._blinkAmountRight, 'f')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._wasChecked == other._wasChecked and
        self._blinkAmountLeft == other._blinkAmountLeft and
        self._blinkAmountRight == other._blinkAmountRight)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._wasChecked, 'b') +
      msgbuffers.size(self._blinkAmountLeft, 'f') +
      msgbuffers.size(self._blinkAmountRight, 'f'))

  def __str__(self):
    return '{type}(wasChecked={wasChecked}, blinkAmountLeft={blinkAmountLeft}, blinkAmountRight={blinkAmountRight})'.format(
      type=type(self).__name__,
      wasChecked=self._wasChecked,
      blinkAmountLeft=self._blinkAmountLeft,
      blinkAmountRight=self._blinkAmountRight)

  def __repr__(self):
    return '{type}(wasChecked={wasChecked}, blinkAmountLeft={blinkAmountLeft}, blinkAmountRight={blinkAmountRight})'.format(
      type=type(self).__name__,
      wasChecked=repr(self._wasChecked),
      blinkAmountLeft=repr(self._blinkAmountLeft),
      blinkAmountRight=repr(self._blinkAmountRight))

Anki.Vision.BlinkAmount = BlinkAmount
del BlinkAmount


