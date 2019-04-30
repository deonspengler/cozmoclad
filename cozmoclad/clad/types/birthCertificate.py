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
Source: clad/types/birthCertificate.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ../robot/clad/src/ -o ../generated/cladPython// clad/types/birthCertificate.clad
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
Anki.Cozmo = msgbuffers.Namespace()

class BirthCertificate(object):
  "Generated message-passing structure."

  __slots__ = (
    '_atFactory',    # uint_8
    '_whichFactory', # uint_8
    '_whichLine',    # uint_8
    '_model',        # uint_8
    '_year',         # uint_8
    '_month',        # uint_8
    '_day',          # uint_8
    '_hour',         # uint_8
    '_minute',       # uint_8
    '_second',       # uint_8
  )

  @property
  def atFactory(self):
    "uint_8 atFactory struct property."
    return self._atFactory

  @atFactory.setter
  def atFactory(self, value):
    self._atFactory = msgbuffers.validate_integer(
      'BirthCertificate.atFactory', value, 0, 255)

  @property
  def whichFactory(self):
    "uint_8 whichFactory struct property."
    return self._whichFactory

  @whichFactory.setter
  def whichFactory(self, value):
    self._whichFactory = msgbuffers.validate_integer(
      'BirthCertificate.whichFactory', value, 0, 255)

  @property
  def whichLine(self):
    "uint_8 whichLine struct property."
    return self._whichLine

  @whichLine.setter
  def whichLine(self, value):
    self._whichLine = msgbuffers.validate_integer(
      'BirthCertificate.whichLine', value, 0, 255)

  @property
  def model(self):
    "uint_8 model struct property."
    return self._model

  @model.setter
  def model(self, value):
    self._model = msgbuffers.validate_integer(
      'BirthCertificate.model', value, 0, 255)

  @property
  def year(self):
    "uint_8 year struct property."
    return self._year

  @year.setter
  def year(self, value):
    self._year = msgbuffers.validate_integer(
      'BirthCertificate.year', value, 0, 255)

  @property
  def month(self):
    "uint_8 month struct property."
    return self._month

  @month.setter
  def month(self, value):
    self._month = msgbuffers.validate_integer(
      'BirthCertificate.month', value, 0, 255)

  @property
  def day(self):
    "uint_8 day struct property."
    return self._day

  @day.setter
  def day(self, value):
    self._day = msgbuffers.validate_integer(
      'BirthCertificate.day', value, 0, 255)

  @property
  def hour(self):
    "uint_8 hour struct property."
    return self._hour

  @hour.setter
  def hour(self, value):
    self._hour = msgbuffers.validate_integer(
      'BirthCertificate.hour', value, 0, 255)

  @property
  def minute(self):
    "uint_8 minute struct property."
    return self._minute

  @minute.setter
  def minute(self, value):
    self._minute = msgbuffers.validate_integer(
      'BirthCertificate.minute', value, 0, 255)

  @property
  def second(self):
    "uint_8 second struct property."
    return self._second

  @second.setter
  def second(self, value):
    self._second = msgbuffers.validate_integer(
      'BirthCertificate.second', value, 0, 255)

  def __init__(self, atFactory=0, whichFactory=1, whichLine=1, model=1, year=0, month=0, day=0, hour=0, minute=0, second=0):
    self.atFactory = atFactory
    self.whichFactory = whichFactory
    self.whichLine = whichLine
    self.model = model
    self.year = year
    self.month = month
    self.day = day
    self.hour = hour
    self.minute = minute
    self.second = second

  @classmethod
  def unpack(cls, buffer):
    "Reads a new BirthCertificate from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('BirthCertificate.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new BirthCertificate from the given BinaryReader."
    _atFactory = reader.read('B')
    _whichFactory = reader.read('B')
    _whichLine = reader.read('B')
    _model = reader.read('B')
    _year = reader.read('B')
    _month = reader.read('B')
    _day = reader.read('B')
    _hour = reader.read('B')
    _minute = reader.read('B')
    _second = reader.read('B')
    return cls(_atFactory, _whichFactory, _whichLine, _model, _year, _month, _day, _hour, _minute, _second)

  def pack(self):
    "Writes the current BirthCertificate, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current BirthCertificate to the given BinaryWriter."
    writer.write(self._atFactory, 'B')
    writer.write(self._whichFactory, 'B')
    writer.write(self._whichLine, 'B')
    writer.write(self._model, 'B')
    writer.write(self._year, 'B')
    writer.write(self._month, 'B')
    writer.write(self._day, 'B')
    writer.write(self._hour, 'B')
    writer.write(self._minute, 'B')
    writer.write(self._second, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._atFactory == other._atFactory and
        self._whichFactory == other._whichFactory and
        self._whichLine == other._whichLine and
        self._model == other._model and
        self._year == other._year and
        self._month == other._month and
        self._day == other._day and
        self._hour == other._hour and
        self._minute == other._minute and
        self._second == other._second)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._atFactory, 'B') +
      msgbuffers.size(self._whichFactory, 'B') +
      msgbuffers.size(self._whichLine, 'B') +
      msgbuffers.size(self._model, 'B') +
      msgbuffers.size(self._year, 'B') +
      msgbuffers.size(self._month, 'B') +
      msgbuffers.size(self._day, 'B') +
      msgbuffers.size(self._hour, 'B') +
      msgbuffers.size(self._minute, 'B') +
      msgbuffers.size(self._second, 'B'))

  def __str__(self):
    return '{type}(atFactory={atFactory}, whichFactory={whichFactory}, whichLine={whichLine}, model={model}, year={year}, month={month}, day={day}, hour={hour}, minute={minute}, second={second})'.format(
      type=type(self).__name__,
      atFactory=self._atFactory,
      whichFactory=self._whichFactory,
      whichLine=self._whichLine,
      model=self._model,
      year=self._year,
      month=self._month,
      day=self._day,
      hour=self._hour,
      minute=self._minute,
      second=self._second)

  def __repr__(self):
    return '{type}(atFactory={atFactory}, whichFactory={whichFactory}, whichLine={whichLine}, model={model}, year={year}, month={month}, day={day}, hour={hour}, minute={minute}, second={second})'.format(
      type=type(self).__name__,
      atFactory=repr(self._atFactory),
      whichFactory=repr(self._whichFactory),
      whichLine=repr(self._whichLine),
      model=repr(self._model),
      year=repr(self._year),
      month=repr(self._month),
      day=repr(self._day),
      hour=repr(self._hour),
      minute=repr(self._minute),
      second=repr(self._second))

Anki.Cozmo.BirthCertificate = BirthCertificate
del BirthCertificate


