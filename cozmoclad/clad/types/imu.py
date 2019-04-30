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
Source: clad/types/imu.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ../robot/clad/src/ -o ../generated/cladPython// clad/types/imu.clad
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
Anki.Cozmo.RobotInterface = msgbuffers.Namespace()

class IMUConstants(object):
  "Automatically-generated uint_8 enumeration."
  IMU_CHUNK_SIZE = 8

Anki.Cozmo.IMUConstants = IMUConstants
del IMUConstants


class IMURequest(object):
  "Generated message-passing message."

  __slots__ = (
    '_length_ms', # uint_32
  )

  @property
  def length_ms(self):
    "uint_32 length_ms struct property."
    return self._length_ms

  @length_ms.setter
  def length_ms(self, value):
    self._length_ms = msgbuffers.validate_integer(
      'IMURequest.length_ms', value, 0, 4294967295)

  def __init__(self, length_ms=0):
    self.length_ms = length_ms

  @classmethod
  def unpack(cls, buffer):
    "Reads a new IMURequest from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('IMURequest.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new IMURequest from the given BinaryReader."
    _length_ms = reader.read('I')
    return cls(_length_ms)

  def pack(self):
    "Writes the current IMURequest, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current IMURequest to the given BinaryWriter."
    writer.write(self._length_ms, 'I')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._length_ms == other._length_ms
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._length_ms, 'I'))

  def __str__(self):
    return '{type}(length_ms={length_ms})'.format(
      type=type(self).__name__,
      length_ms=self._length_ms)

  def __repr__(self):
    return '{type}(length_ms={length_ms})'.format(
      type=type(self).__name__,
      length_ms=repr(self._length_ms))

Anki.Cozmo.IMURequest = IMURequest
del IMURequest


class AccelData(object):
  "Generated message-passing structure."

  __slots__ = (
    '_x', # float_32
    '_y', # float_32
    '_z', # float_32
  )

  @property
  def x(self):
    "float_32 x struct property."
    return self._x

  @x.setter
  def x(self, value):
    self._x = msgbuffers.validate_float(
      'AccelData.x', value, 'f')

  @property
  def y(self):
    "float_32 y struct property."
    return self._y

  @y.setter
  def y(self, value):
    self._y = msgbuffers.validate_float(
      'AccelData.y', value, 'f')

  @property
  def z(self):
    "float_32 z struct property."
    return self._z

  @z.setter
  def z(self, value):
    self._z = msgbuffers.validate_float(
      'AccelData.z', value, 'f')

  def __init__(self, x=0.0, y=0.0, z=0.0):
    self.x = x
    self.y = y
    self.z = z

  @classmethod
  def unpack(cls, buffer):
    "Reads a new AccelData from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('AccelData.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new AccelData from the given BinaryReader."
    _x = reader.read('f')
    _y = reader.read('f')
    _z = reader.read('f')
    return cls(_x, _y, _z)

  def pack(self):
    "Writes the current AccelData, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current AccelData to the given BinaryWriter."
    writer.write(self._x, 'f')
    writer.write(self._y, 'f')
    writer.write(self._z, 'f')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._x == other._x and
        self._y == other._y and
        self._z == other._z)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._x, 'f') +
      msgbuffers.size(self._y, 'f') +
      msgbuffers.size(self._z, 'f'))

  def __str__(self):
    return '{type}(x={x}, y={y}, z={z})'.format(
      type=type(self).__name__,
      x=self._x,
      y=self._y,
      z=self._z)

  def __repr__(self):
    return '{type}(x={x}, y={y}, z={z})'.format(
      type=type(self).__name__,
      x=repr(self._x),
      y=repr(self._y),
      z=repr(self._z))

Anki.Cozmo.AccelData = AccelData
del AccelData


class GyroData(object):
  "Generated message-passing structure."

  __slots__ = (
    '_x', # float_32
    '_y', # float_32
    '_z', # float_32
  )

  @property
  def x(self):
    "float_32 x struct property."
    return self._x

  @x.setter
  def x(self, value):
    self._x = msgbuffers.validate_float(
      'GyroData.x', value, 'f')

  @property
  def y(self):
    "float_32 y struct property."
    return self._y

  @y.setter
  def y(self, value):
    self._y = msgbuffers.validate_float(
      'GyroData.y', value, 'f')

  @property
  def z(self):
    "float_32 z struct property."
    return self._z

  @z.setter
  def z(self, value):
    self._z = msgbuffers.validate_float(
      'GyroData.z', value, 'f')

  def __init__(self, x=0.0, y=0.0, z=0.0):
    self.x = x
    self.y = y
    self.z = z

  @classmethod
  def unpack(cls, buffer):
    "Reads a new GyroData from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('GyroData.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new GyroData from the given BinaryReader."
    _x = reader.read('f')
    _y = reader.read('f')
    _z = reader.read('f')
    return cls(_x, _y, _z)

  def pack(self):
    "Writes the current GyroData, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current GyroData to the given BinaryWriter."
    writer.write(self._x, 'f')
    writer.write(self._y, 'f')
    writer.write(self._z, 'f')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._x == other._x and
        self._y == other._y and
        self._z == other._z)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._x, 'f') +
      msgbuffers.size(self._y, 'f') +
      msgbuffers.size(self._z, 'f'))

  def __str__(self):
    return '{type}(x={x}, y={y}, z={z})'.format(
      type=type(self).__name__,
      x=self._x,
      y=self._y,
      z=self._z)

  def __repr__(self):
    return '{type}(x={x}, y={y}, z={z})'.format(
      type=type(self).__name__,
      x=repr(self._x),
      y=repr(self._y),
      z=repr(self._z))

Anki.Cozmo.GyroData = GyroData
del GyroData


class IMUDataChunk(object):
  "Generated message-passing structure."

  __slots__ = (
    '_aX',             # float_32[8]
    '_aY',             # float_32[8]
    '_aZ',             # float_32[8]
    '_gX',             # float_32[8]
    '_gY',             # float_32[8]
    '_gZ',             # float_32[8]
    '_seqId',          # uint_8
    '_chunkId',        # uint_8
    '_totalNumChunks', # uint_8
  )

  @property
  def aX(self):
    "float_32[8] aX struct property."
    return self._aX

  @aX.setter
  def aX(self, value):
    self._aX = msgbuffers.validate_farray(
      'IMUDataChunk.aX', value, 8,
      lambda name, value_inner: msgbuffers.validate_float(
        name, value_inner, 'f'))

  @property
  def aY(self):
    "float_32[8] aY struct property."
    return self._aY

  @aY.setter
  def aY(self, value):
    self._aY = msgbuffers.validate_farray(
      'IMUDataChunk.aY', value, 8,
      lambda name, value_inner: msgbuffers.validate_float(
        name, value_inner, 'f'))

  @property
  def aZ(self):
    "float_32[8] aZ struct property."
    return self._aZ

  @aZ.setter
  def aZ(self, value):
    self._aZ = msgbuffers.validate_farray(
      'IMUDataChunk.aZ', value, 8,
      lambda name, value_inner: msgbuffers.validate_float(
        name, value_inner, 'f'))

  @property
  def gX(self):
    "float_32[8] gX struct property."
    return self._gX

  @gX.setter
  def gX(self, value):
    self._gX = msgbuffers.validate_farray(
      'IMUDataChunk.gX', value, 8,
      lambda name, value_inner: msgbuffers.validate_float(
        name, value_inner, 'f'))

  @property
  def gY(self):
    "float_32[8] gY struct property."
    return self._gY

  @gY.setter
  def gY(self, value):
    self._gY = msgbuffers.validate_farray(
      'IMUDataChunk.gY', value, 8,
      lambda name, value_inner: msgbuffers.validate_float(
        name, value_inner, 'f'))

  @property
  def gZ(self):
    "float_32[8] gZ struct property."
    return self._gZ

  @gZ.setter
  def gZ(self, value):
    self._gZ = msgbuffers.validate_farray(
      'IMUDataChunk.gZ', value, 8,
      lambda name, value_inner: msgbuffers.validate_float(
        name, value_inner, 'f'))

  @property
  def seqId(self):
    "uint_8 seqId struct property."
    return self._seqId

  @seqId.setter
  def seqId(self, value):
    self._seqId = msgbuffers.validate_integer(
      'IMUDataChunk.seqId', value, 0, 255)

  @property
  def chunkId(self):
    "uint_8 chunkId struct property."
    return self._chunkId

  @chunkId.setter
  def chunkId(self, value):
    self._chunkId = msgbuffers.validate_integer(
      'IMUDataChunk.chunkId', value, 0, 255)

  @property
  def totalNumChunks(self):
    "uint_8 totalNumChunks struct property."
    return self._totalNumChunks

  @totalNumChunks.setter
  def totalNumChunks(self, value):
    self._totalNumChunks = msgbuffers.validate_integer(
      'IMUDataChunk.totalNumChunks', value, 0, 255)

  def __init__(self, aX=(0.0,) * 8, aY=(0.0,) * 8, aZ=(0.0,) * 8, gX=(0.0,) * 8, gY=(0.0,) * 8, gZ=(0.0,) * 8, seqId=0, chunkId=0, totalNumChunks=0):
    self.aX = aX
    self.aY = aY
    self.aZ = aZ
    self.gX = gX
    self.gY = gY
    self.gZ = gZ
    self.seqId = seqId
    self.chunkId = chunkId
    self.totalNumChunks = totalNumChunks

  @classmethod
  def unpack(cls, buffer):
    "Reads a new IMUDataChunk from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('IMUDataChunk.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new IMUDataChunk from the given BinaryReader."
    _aX = reader.read_farray('f', 8)
    _aY = reader.read_farray('f', 8)
    _aZ = reader.read_farray('f', 8)
    _gX = reader.read_farray('f', 8)
    _gY = reader.read_farray('f', 8)
    _gZ = reader.read_farray('f', 8)
    _seqId = reader.read('B')
    _chunkId = reader.read('B')
    _totalNumChunks = reader.read('B')
    return cls(_aX, _aY, _aZ, _gX, _gY, _gZ, _seqId, _chunkId, _totalNumChunks)

  def pack(self):
    "Writes the current IMUDataChunk, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current IMUDataChunk to the given BinaryWriter."
    writer.write_farray(self._aX, 'f', 8)
    writer.write_farray(self._aY, 'f', 8)
    writer.write_farray(self._aZ, 'f', 8)
    writer.write_farray(self._gX, 'f', 8)
    writer.write_farray(self._gY, 'f', 8)
    writer.write_farray(self._gZ, 'f', 8)
    writer.write(self._seqId, 'B')
    writer.write(self._chunkId, 'B')
    writer.write(self._totalNumChunks, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._aX == other._aX and
        self._aY == other._aY and
        self._aZ == other._aZ and
        self._gX == other._gX and
        self._gY == other._gY and
        self._gZ == other._gZ and
        self._seqId == other._seqId and
        self._chunkId == other._chunkId and
        self._totalNumChunks == other._totalNumChunks)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size_farray(self._aX, 'f', 8) +
      msgbuffers.size_farray(self._aY, 'f', 8) +
      msgbuffers.size_farray(self._aZ, 'f', 8) +
      msgbuffers.size_farray(self._gX, 'f', 8) +
      msgbuffers.size_farray(self._gY, 'f', 8) +
      msgbuffers.size_farray(self._gZ, 'f', 8) +
      msgbuffers.size(self._seqId, 'B') +
      msgbuffers.size(self._chunkId, 'B') +
      msgbuffers.size(self._totalNumChunks, 'B'))

  def __str__(self):
    return '{type}(aX={aX}, aY={aY}, aZ={aZ}, gX={gX}, gY={gY}, gZ={gZ}, seqId={seqId}, chunkId={chunkId}, totalNumChunks={totalNumChunks})'.format(
      type=type(self).__name__,
      aX=msgbuffers.shorten_sequence(self._aX),
      aY=msgbuffers.shorten_sequence(self._aY),
      aZ=msgbuffers.shorten_sequence(self._aZ),
      gX=msgbuffers.shorten_sequence(self._gX),
      gY=msgbuffers.shorten_sequence(self._gY),
      gZ=msgbuffers.shorten_sequence(self._gZ),
      seqId=self._seqId,
      chunkId=self._chunkId,
      totalNumChunks=self._totalNumChunks)

  def __repr__(self):
    return '{type}(aX={aX}, aY={aY}, aZ={aZ}, gX={gX}, gY={gY}, gZ={gZ}, seqId={seqId}, chunkId={chunkId}, totalNumChunks={totalNumChunks})'.format(
      type=type(self).__name__,
      aX=repr(self._aX),
      aY=repr(self._aY),
      aZ=repr(self._aZ),
      gX=repr(self._gX),
      gY=repr(self._gY),
      gZ=repr(self._gZ),
      seqId=repr(self._seqId),
      chunkId=repr(self._chunkId),
      totalNumChunks=repr(self._totalNumChunks))

Anki.Cozmo.RobotInterface.IMUDataChunk = IMUDataChunk
del IMUDataChunk


class IMURawDataChunk(object):
  "Generated message-passing structure."

  __slots__ = (
    '_g',         # int_16[3]
    '_a',         # int_16[3]
    '_order',     # uint_8
    '_timestamp', # uint_8
  )

  @property
  def g(self):
    "int_16[3] g struct property."
    return self._g

  @g.setter
  def g(self, value):
    self._g = msgbuffers.validate_farray(
      'IMURawDataChunk.g', value, 3,
      lambda name, value_inner: msgbuffers.validate_integer(
        name, value_inner, -32768, 32767))

  @property
  def a(self):
    "int_16[3] a struct property."
    return self._a

  @a.setter
  def a(self, value):
    self._a = msgbuffers.validate_farray(
      'IMURawDataChunk.a', value, 3,
      lambda name, value_inner: msgbuffers.validate_integer(
        name, value_inner, -32768, 32767))

  @property
  def order(self):
    "uint_8 order struct property."
    return self._order

  @order.setter
  def order(self, value):
    self._order = msgbuffers.validate_integer(
      'IMURawDataChunk.order', value, 0, 255)

  @property
  def timestamp(self):
    "uint_8 timestamp struct property."
    return self._timestamp

  @timestamp.setter
  def timestamp(self, value):
    self._timestamp = msgbuffers.validate_integer(
      'IMURawDataChunk.timestamp', value, 0, 255)

  def __init__(self, g=(0,) * 3, a=(0,) * 3, order=0, timestamp=0):
    self.g = g
    self.a = a
    self.order = order
    self.timestamp = timestamp

  @classmethod
  def unpack(cls, buffer):
    "Reads a new IMURawDataChunk from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('IMURawDataChunk.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new IMURawDataChunk from the given BinaryReader."
    _g = reader.read_farray('h', 3)
    _a = reader.read_farray('h', 3)
    _order = reader.read('B')
    _timestamp = reader.read('B')
    return cls(_g, _a, _order, _timestamp)

  def pack(self):
    "Writes the current IMURawDataChunk, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current IMURawDataChunk to the given BinaryWriter."
    writer.write_farray(self._g, 'h', 3)
    writer.write_farray(self._a, 'h', 3)
    writer.write(self._order, 'B')
    writer.write(self._timestamp, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._g == other._g and
        self._a == other._a and
        self._order == other._order and
        self._timestamp == other._timestamp)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size_farray(self._g, 'h', 3) +
      msgbuffers.size_farray(self._a, 'h', 3) +
      msgbuffers.size(self._order, 'B') +
      msgbuffers.size(self._timestamp, 'B'))

  def __str__(self):
    return '{type}(g={g}, a={a}, order={order}, timestamp={timestamp})'.format(
      type=type(self).__name__,
      g=msgbuffers.shorten_sequence(self._g),
      a=msgbuffers.shorten_sequence(self._a),
      order=self._order,
      timestamp=self._timestamp)

  def __repr__(self):
    return '{type}(g={g}, a={a}, order={order}, timestamp={timestamp})'.format(
      type=type(self).__name__,
      g=repr(self._g),
      a=repr(self._a),
      order=repr(self._order),
      timestamp=repr(self._timestamp))

Anki.Cozmo.RobotInterface.IMURawDataChunk = IMURawDataChunk
del IMURawDataChunk


class IMUTemperature(object):
  "Generated message-passing message."

  __slots__ = (
    '_temperature_degC', # float_32
  )

  @property
  def temperature_degC(self):
    "float_32 temperature_degC struct property."
    return self._temperature_degC

  @temperature_degC.setter
  def temperature_degC(self, value):
    self._temperature_degC = msgbuffers.validate_float(
      'IMUTemperature.temperature_degC', value, 'f')

  def __init__(self, temperature_degC=0.0):
    self.temperature_degC = temperature_degC

  @classmethod
  def unpack(cls, buffer):
    "Reads a new IMUTemperature from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('IMUTemperature.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new IMUTemperature from the given BinaryReader."
    _temperature_degC = reader.read('f')
    return cls(_temperature_degC)

  def pack(self):
    "Writes the current IMUTemperature, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current IMUTemperature to the given BinaryWriter."
    writer.write(self._temperature_degC, 'f')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._temperature_degC == other._temperature_degC
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._temperature_degC, 'f'))

  def __str__(self):
    return '{type}(temperature_degC={temperature_degC})'.format(
      type=type(self).__name__,
      temperature_degC=self._temperature_degC)

  def __repr__(self):
    return '{type}(temperature_degC={temperature_degC})'.format(
      type=type(self).__name__,
      temperature_degC=repr(self._temperature_degC))

Anki.Cozmo.RobotInterface.IMUTemperature = IMUTemperature
del IMUTemperature


