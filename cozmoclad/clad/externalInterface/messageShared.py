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
Source: clad/externalInterface/messageShared.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ./src/ -I ../robot/clad/src/ ../coretech/vision/clad/src/ ../coretech/common/clad/src/ ../lib/util/source/anki/clad -o ../generated/cladPython// clad/externalInterface/messageShared.clad
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
Anki.AudioMetaData = msgbuffers.Namespace()
Anki.AudioMetaData.GameEvent = msgbuffers.Namespace()
Anki.Cozmo = msgbuffers.Namespace()
Anki.Cozmo.ExternalInterface = msgbuffers.Namespace()

from clad.types.actionTypes import Anki as _Anki
Anki.update(_Anki.deep_clone())

from clad.types.advertisementTypes import Anki as _Anki
Anki.update(_Anki.deep_clone())

class CommsConstants(object):
  "Automatically-generated uint_32 enumeration."
  kDirectCommsBufferSize = 1048576
  kVizCommsBufferSize    = 131072

Anki.Cozmo.ExternalInterface.CommsConstants = CommsConstants

class Ping(object):
  "Generated message-passing message."

  __slots__ = (
    '_counter',     # uint_32
    '_timeSent_ms', # float_64
    '_isResponse',  # bool
  )

  @property
  def counter(self):
    "uint_32 counter struct property."
    return self._counter

  @counter.setter
  def counter(self, value):
    self._counter = msgbuffers.validate_integer(
      'Ping.counter', value, 0, 4294967295)

  @property
  def timeSent_ms(self):
    "float_64 timeSent_ms struct property."
    return self._timeSent_ms

  @timeSent_ms.setter
  def timeSent_ms(self, value):
    self._timeSent_ms = msgbuffers.validate_float(
      'Ping.timeSent_ms', value, 'd')

  @property
  def isResponse(self):
    "bool isResponse struct property."
    return self._isResponse

  @isResponse.setter
  def isResponse(self, value):
    self._isResponse = msgbuffers.validate_bool(
      'Ping.isResponse', value)

  def __init__(self, counter=0, timeSent_ms=0.0, isResponse=False):
    self.counter = counter
    self.timeSent_ms = timeSent_ms
    self.isResponse = isResponse

  @classmethod
  def unpack(cls, buffer):
    "Reads a new Ping from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('Ping.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new Ping from the given BinaryReader."
    _counter = reader.read('I')
    _timeSent_ms = reader.read('d')
    _isResponse = bool(reader.read('b'))
    return cls(_counter, _timeSent_ms, _isResponse)

  def pack(self):
    "Writes the current Ping, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current Ping to the given BinaryWriter."
    writer.write(self._counter, 'I')
    writer.write(self._timeSent_ms, 'd')
    writer.write(int(self._isResponse), 'b')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._counter == other._counter and
        self._timeSent_ms == other._timeSent_ms and
        self._isResponse == other._isResponse)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._counter, 'I') +
      msgbuffers.size(self._timeSent_ms, 'd') +
      msgbuffers.size(self._isResponse, 'b'))

  def __str__(self):
    return '{type}(counter={counter}, timeSent_ms={timeSent_ms}, isResponse={isResponse})'.format(
      type=type(self).__name__,
      counter=self._counter,
      timeSent_ms=self._timeSent_ms,
      isResponse=self._isResponse)

  def __repr__(self):
    return '{type}(counter={counter}, timeSent_ms={timeSent_ms}, isResponse={isResponse})'.format(
      type=type(self).__name__,
      counter=repr(self._counter),
      timeSent_ms=repr(self._timeSent_ms),
      isResponse=repr(self._isResponse))

Anki.Cozmo.ExternalInterface.Ping = Ping
del Ping


class DenyGameStart(object):
  "Generated message-passing message."

  __slots__ = ()

  def __init__(self):
    pass

  @classmethod
  def unpack(cls, buffer):
    "Reads a new DenyGameStart from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('DenyGameStart.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new DenyGameStart from the given BinaryReader."
    return cls()

  def pack(self):
    "Writes the current DenyGameStart, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current DenyGameStart to the given BinaryWriter."

  def __eq__(self, other):
    if type(self) is type(other):
      return True
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return 0

  def __str__(self):
    return '{type}()'.format(type=type(self).__name__)

  def __repr__(self):
    return '{type}()'.format(type=type(self).__name__)

Anki.Cozmo.ExternalInterface.DenyGameStart = DenyGameStart
del DenyGameStart


class DeviceAccelerometerValuesRaw(object):
  "Generated message-passing message."

  __slots__ = (
    '_x_gForce', # float_32
    '_y_gForce', # float_32
    '_z_gForce', # float_32
  )

  @property
  def x_gForce(self):
    "float_32 x_gForce struct property."
    return self._x_gForce

  @x_gForce.setter
  def x_gForce(self, value):
    self._x_gForce = msgbuffers.validate_float(
      'DeviceAccelerometerValuesRaw.x_gForce', value, 'f')

  @property
  def y_gForce(self):
    "float_32 y_gForce struct property."
    return self._y_gForce

  @y_gForce.setter
  def y_gForce(self, value):
    self._y_gForce = msgbuffers.validate_float(
      'DeviceAccelerometerValuesRaw.y_gForce', value, 'f')

  @property
  def z_gForce(self):
    "float_32 z_gForce struct property."
    return self._z_gForce

  @z_gForce.setter
  def z_gForce(self, value):
    self._z_gForce = msgbuffers.validate_float(
      'DeviceAccelerometerValuesRaw.z_gForce', value, 'f')

  def __init__(self, x_gForce=0.0, y_gForce=0.0, z_gForce=0.0):
    self.x_gForce = x_gForce
    self.y_gForce = y_gForce
    self.z_gForce = z_gForce

  @classmethod
  def unpack(cls, buffer):
    "Reads a new DeviceAccelerometerValuesRaw from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('DeviceAccelerometerValuesRaw.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new DeviceAccelerometerValuesRaw from the given BinaryReader."
    _x_gForce = reader.read('f')
    _y_gForce = reader.read('f')
    _z_gForce = reader.read('f')
    return cls(_x_gForce, _y_gForce, _z_gForce)

  def pack(self):
    "Writes the current DeviceAccelerometerValuesRaw, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current DeviceAccelerometerValuesRaw to the given BinaryWriter."
    writer.write(self._x_gForce, 'f')
    writer.write(self._y_gForce, 'f')
    writer.write(self._z_gForce, 'f')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._x_gForce == other._x_gForce and
        self._y_gForce == other._y_gForce and
        self._z_gForce == other._z_gForce)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._x_gForce, 'f') +
      msgbuffers.size(self._y_gForce, 'f') +
      msgbuffers.size(self._z_gForce, 'f'))

  def __str__(self):
    return '{type}(x_gForce={x_gForce}, y_gForce={y_gForce}, z_gForce={z_gForce})'.format(
      type=type(self).__name__,
      x_gForce=self._x_gForce,
      y_gForce=self._y_gForce,
      z_gForce=self._z_gForce)

  def __repr__(self):
    return '{type}(x_gForce={x_gForce}, y_gForce={y_gForce}, z_gForce={z_gForce})'.format(
      type=type(self).__name__,
      x_gForce=repr(self._x_gForce),
      y_gForce=repr(self._y_gForce),
      z_gForce=repr(self._z_gForce))

Anki.Cozmo.ExternalInterface.DeviceAccelerometerValuesRaw = DeviceAccelerometerValuesRaw
del DeviceAccelerometerValuesRaw


class DeviceAccelerometerValuesUser(object):
  "Generated message-passing message."

  __slots__ = (
    '_x_gForce', # float_32
    '_y_gForce', # float_32
    '_z_gForce', # float_32
  )

  @property
  def x_gForce(self):
    "float_32 x_gForce struct property."
    return self._x_gForce

  @x_gForce.setter
  def x_gForce(self, value):
    self._x_gForce = msgbuffers.validate_float(
      'DeviceAccelerometerValuesUser.x_gForce', value, 'f')

  @property
  def y_gForce(self):
    "float_32 y_gForce struct property."
    return self._y_gForce

  @y_gForce.setter
  def y_gForce(self, value):
    self._y_gForce = msgbuffers.validate_float(
      'DeviceAccelerometerValuesUser.y_gForce', value, 'f')

  @property
  def z_gForce(self):
    "float_32 z_gForce struct property."
    return self._z_gForce

  @z_gForce.setter
  def z_gForce(self, value):
    self._z_gForce = msgbuffers.validate_float(
      'DeviceAccelerometerValuesUser.z_gForce', value, 'f')

  def __init__(self, x_gForce=0.0, y_gForce=0.0, z_gForce=0.0):
    self.x_gForce = x_gForce
    self.y_gForce = y_gForce
    self.z_gForce = z_gForce

  @classmethod
  def unpack(cls, buffer):
    "Reads a new DeviceAccelerometerValuesUser from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('DeviceAccelerometerValuesUser.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new DeviceAccelerometerValuesUser from the given BinaryReader."
    _x_gForce = reader.read('f')
    _y_gForce = reader.read('f')
    _z_gForce = reader.read('f')
    return cls(_x_gForce, _y_gForce, _z_gForce)

  def pack(self):
    "Writes the current DeviceAccelerometerValuesUser, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current DeviceAccelerometerValuesUser to the given BinaryWriter."
    writer.write(self._x_gForce, 'f')
    writer.write(self._y_gForce, 'f')
    writer.write(self._z_gForce, 'f')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._x_gForce == other._x_gForce and
        self._y_gForce == other._y_gForce and
        self._z_gForce == other._z_gForce)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._x_gForce, 'f') +
      msgbuffers.size(self._y_gForce, 'f') +
      msgbuffers.size(self._z_gForce, 'f'))

  def __str__(self):
    return '{type}(x_gForce={x_gForce}, y_gForce={y_gForce}, z_gForce={z_gForce})'.format(
      type=type(self).__name__,
      x_gForce=self._x_gForce,
      y_gForce=self._y_gForce,
      z_gForce=self._z_gForce)

  def __repr__(self):
    return '{type}(x_gForce={x_gForce}, y_gForce={y_gForce}, z_gForce={z_gForce})'.format(
      type=type(self).__name__,
      x_gForce=repr(self._x_gForce),
      y_gForce=repr(self._y_gForce),
      z_gForce=repr(self._z_gForce))

Anki.Cozmo.ExternalInterface.DeviceAccelerometerValuesUser = DeviceAccelerometerValuesUser
del DeviceAccelerometerValuesUser


class DeviceGyroValues(object):
  "Generated message-passing message."

  __slots__ = (
    '_w', # float_32
    '_x', # float_32
    '_y', # float_32
    '_z', # float_32
  )

  @property
  def w(self):
    "float_32 w struct property."
    return self._w

  @w.setter
  def w(self, value):
    self._w = msgbuffers.validate_float(
      'DeviceGyroValues.w', value, 'f')

  @property
  def x(self):
    "float_32 x struct property."
    return self._x

  @x.setter
  def x(self, value):
    self._x = msgbuffers.validate_float(
      'DeviceGyroValues.x', value, 'f')

  @property
  def y(self):
    "float_32 y struct property."
    return self._y

  @y.setter
  def y(self, value):
    self._y = msgbuffers.validate_float(
      'DeviceGyroValues.y', value, 'f')

  @property
  def z(self):
    "float_32 z struct property."
    return self._z

  @z.setter
  def z(self, value):
    self._z = msgbuffers.validate_float(
      'DeviceGyroValues.z', value, 'f')

  def __init__(self, w=0.0, x=0.0, y=0.0, z=0.0):
    self.w = w
    self.x = x
    self.y = y
    self.z = z

  @classmethod
  def unpack(cls, buffer):
    "Reads a new DeviceGyroValues from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('DeviceGyroValues.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new DeviceGyroValues from the given BinaryReader."
    _w = reader.read('f')
    _x = reader.read('f')
    _y = reader.read('f')
    _z = reader.read('f')
    return cls(_w, _x, _y, _z)

  def pack(self):
    "Writes the current DeviceGyroValues, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current DeviceGyroValues to the given BinaryWriter."
    writer.write(self._w, 'f')
    writer.write(self._x, 'f')
    writer.write(self._y, 'f')
    writer.write(self._z, 'f')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._w == other._w and
        self._x == other._x and
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
    return (msgbuffers.size(self._w, 'f') +
      msgbuffers.size(self._x, 'f') +
      msgbuffers.size(self._y, 'f') +
      msgbuffers.size(self._z, 'f'))

  def __str__(self):
    return '{type}(w={w}, x={x}, y={y}, z={z})'.format(
      type=type(self).__name__,
      w=self._w,
      x=self._x,
      y=self._y,
      z=self._z)

  def __repr__(self):
    return '{type}(w={w}, x={x}, y={y}, z={z})'.format(
      type=type(self).__name__,
      w=repr(self._w),
      x=repr(self._x),
      y=repr(self._y),
      z=repr(self._z))

Anki.Cozmo.ExternalInterface.DeviceGyroValues = DeviceGyroValues
del DeviceGyroValues


class EnableDeviceIMUData(object):
  "Generated message-passing message."

  __slots__ = (
    '_enableAccelerometerRaw',  # bool
    '_enableAccelerometerUser', # bool
    '_enableGyro',              # bool
  )

  @property
  def enableAccelerometerRaw(self):
    "bool enableAccelerometerRaw struct property."
    return self._enableAccelerometerRaw

  @enableAccelerometerRaw.setter
  def enableAccelerometerRaw(self, value):
    self._enableAccelerometerRaw = msgbuffers.validate_bool(
      'EnableDeviceIMUData.enableAccelerometerRaw', value)

  @property
  def enableAccelerometerUser(self):
    "bool enableAccelerometerUser struct property."
    return self._enableAccelerometerUser

  @enableAccelerometerUser.setter
  def enableAccelerometerUser(self, value):
    self._enableAccelerometerUser = msgbuffers.validate_bool(
      'EnableDeviceIMUData.enableAccelerometerUser', value)

  @property
  def enableGyro(self):
    "bool enableGyro struct property."
    return self._enableGyro

  @enableGyro.setter
  def enableGyro(self, value):
    self._enableGyro = msgbuffers.validate_bool(
      'EnableDeviceIMUData.enableGyro', value)

  def __init__(self, enableAccelerometerRaw=False, enableAccelerometerUser=False, enableGyro=False):
    self.enableAccelerometerRaw = enableAccelerometerRaw
    self.enableAccelerometerUser = enableAccelerometerUser
    self.enableGyro = enableGyro

  @classmethod
  def unpack(cls, buffer):
    "Reads a new EnableDeviceIMUData from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('EnableDeviceIMUData.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new EnableDeviceIMUData from the given BinaryReader."
    _enableAccelerometerRaw = bool(reader.read('b'))
    _enableAccelerometerUser = bool(reader.read('b'))
    _enableGyro = bool(reader.read('b'))
    return cls(_enableAccelerometerRaw, _enableAccelerometerUser, _enableGyro)

  def pack(self):
    "Writes the current EnableDeviceIMUData, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current EnableDeviceIMUData to the given BinaryWriter."
    writer.write(int(self._enableAccelerometerRaw), 'b')
    writer.write(int(self._enableAccelerometerUser), 'b')
    writer.write(int(self._enableGyro), 'b')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._enableAccelerometerRaw == other._enableAccelerometerRaw and
        self._enableAccelerometerUser == other._enableAccelerometerUser and
        self._enableGyro == other._enableGyro)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._enableAccelerometerRaw, 'b') +
      msgbuffers.size(self._enableAccelerometerUser, 'b') +
      msgbuffers.size(self._enableGyro, 'b'))

  def __str__(self):
    return '{type}(enableAccelerometerRaw={enableAccelerometerRaw}, enableAccelerometerUser={enableAccelerometerUser}, enableGyro={enableGyro})'.format(
      type=type(self).__name__,
      enableAccelerometerRaw=self._enableAccelerometerRaw,
      enableAccelerometerUser=self._enableAccelerometerUser,
      enableGyro=self._enableGyro)

  def __repr__(self):
    return '{type}(enableAccelerometerRaw={enableAccelerometerRaw}, enableAccelerometerUser={enableAccelerometerUser}, enableGyro={enableGyro})'.format(
      type=type(self).__name__,
      enableAccelerometerRaw=repr(self._enableAccelerometerRaw),
      enableAccelerometerUser=repr(self._enableAccelerometerUser),
      enableGyro=repr(self._enableGyro))

Anki.Cozmo.ExternalInterface.EnableDeviceIMUData = EnableDeviceIMUData
del EnableDeviceIMUData


class IsDeviceIMUSupported(object):
  "Generated message-passing message."

  __slots__ = (
    '_isAccelerometerSupported', # bool
    '_isGyroSupported',          # bool
  )

  @property
  def isAccelerometerSupported(self):
    "bool isAccelerometerSupported struct property."
    return self._isAccelerometerSupported

  @isAccelerometerSupported.setter
  def isAccelerometerSupported(self, value):
    self._isAccelerometerSupported = msgbuffers.validate_bool(
      'IsDeviceIMUSupported.isAccelerometerSupported', value)

  @property
  def isGyroSupported(self):
    "bool isGyroSupported struct property."
    return self._isGyroSupported

  @isGyroSupported.setter
  def isGyroSupported(self, value):
    self._isGyroSupported = msgbuffers.validate_bool(
      'IsDeviceIMUSupported.isGyroSupported', value)

  def __init__(self, isAccelerometerSupported=False, isGyroSupported=False):
    self.isAccelerometerSupported = isAccelerometerSupported
    self.isGyroSupported = isGyroSupported

  @classmethod
  def unpack(cls, buffer):
    "Reads a new IsDeviceIMUSupported from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('IsDeviceIMUSupported.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new IsDeviceIMUSupported from the given BinaryReader."
    _isAccelerometerSupported = bool(reader.read('b'))
    _isGyroSupported = bool(reader.read('b'))
    return cls(_isAccelerometerSupported, _isGyroSupported)

  def pack(self):
    "Writes the current IsDeviceIMUSupported, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current IsDeviceIMUSupported to the given BinaryWriter."
    writer.write(int(self._isAccelerometerSupported), 'b')
    writer.write(int(self._isGyroSupported), 'b')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._isAccelerometerSupported == other._isAccelerometerSupported and
        self._isGyroSupported == other._isGyroSupported)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._isAccelerometerSupported, 'b') +
      msgbuffers.size(self._isGyroSupported, 'b'))

  def __str__(self):
    return '{type}(isAccelerometerSupported={isAccelerometerSupported}, isGyroSupported={isGyroSupported})'.format(
      type=type(self).__name__,
      isAccelerometerSupported=self._isAccelerometerSupported,
      isGyroSupported=self._isGyroSupported)

  def __repr__(self):
    return '{type}(isAccelerometerSupported={isAccelerometerSupported}, isGyroSupported={isGyroSupported})'.format(
      type=type(self).__name__,
      isAccelerometerSupported=repr(self._isAccelerometerSupported),
      isGyroSupported=repr(self._isGyroSupported))

Anki.Cozmo.ExternalInterface.IsDeviceIMUSupported = IsDeviceIMUSupported
del IsDeviceIMUSupported


class GameToGame(object):
  "Generated message-passing message."

  __slots__ = (
    '_messagePartIndex', # uint_8
    '_messagePartCount', # uint_8
    '_messageType',      # string[uint_8]
    '_payload',          # string[uint_16]
  )

  @property
  def messagePartIndex(self):
    "uint_8 messagePartIndex struct property."
    return self._messagePartIndex

  @messagePartIndex.setter
  def messagePartIndex(self, value):
    self._messagePartIndex = msgbuffers.validate_integer(
      'GameToGame.messagePartIndex', value, 0, 255)

  @property
  def messagePartCount(self):
    "uint_8 messagePartCount struct property."
    return self._messagePartCount

  @messagePartCount.setter
  def messagePartCount(self, value):
    self._messagePartCount = msgbuffers.validate_integer(
      'GameToGame.messagePartCount', value, 0, 255)

  @property
  def messageType(self):
    "string[uint_8] messageType struct property."
    return self._messageType

  @messageType.setter
  def messageType(self, value):
    self._messageType = msgbuffers.validate_string(
      'GameToGame.messageType', value, 255)

  @property
  def payload(self):
    "string[uint_16] payload struct property."
    return self._payload

  @payload.setter
  def payload(self, value):
    self._payload = msgbuffers.validate_string(
      'GameToGame.payload', value, 65535)

  def __init__(self, messagePartIndex=0, messagePartCount=0, messageType='', payload=''):
    self.messagePartIndex = messagePartIndex
    self.messagePartCount = messagePartCount
    self.messageType = messageType
    self.payload = payload

  @classmethod
  def unpack(cls, buffer):
    "Reads a new GameToGame from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('GameToGame.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new GameToGame from the given BinaryReader."
    _messagePartIndex = reader.read('B')
    _messagePartCount = reader.read('B')
    _messageType = reader.read_string('B')
    _payload = reader.read_string('H')
    return cls(_messagePartIndex, _messagePartCount, _messageType, _payload)

  def pack(self):
    "Writes the current GameToGame, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current GameToGame to the given BinaryWriter."
    writer.write(self._messagePartIndex, 'B')
    writer.write(self._messagePartCount, 'B')
    writer.write_string(self._messageType, 'B')
    writer.write_string(self._payload, 'H')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._messagePartIndex == other._messagePartIndex and
        self._messagePartCount == other._messagePartCount and
        self._messageType == other._messageType and
        self._payload == other._payload)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._messagePartIndex, 'B') +
      msgbuffers.size(self._messagePartCount, 'B') +
      msgbuffers.size_string(self._messageType, 'B') +
      msgbuffers.size_string(self._payload, 'H'))

  def __str__(self):
    return '{type}(messagePartIndex={messagePartIndex}, messagePartCount={messagePartCount}, messageType={messageType}, payload={payload})'.format(
      type=type(self).__name__,
      messagePartIndex=self._messagePartIndex,
      messagePartCount=self._messagePartCount,
      messageType=msgbuffers.shorten_string(self._messageType),
      payload=msgbuffers.shorten_string(self._payload))

  def __repr__(self):
    return '{type}(messagePartIndex={messagePartIndex}, messagePartCount={messagePartCount}, messageType={messageType}, payload={payload})'.format(
      type=type(self).__name__,
      messagePartIndex=repr(self._messagePartIndex),
      messagePartCount=repr(self._messagePartCount),
      messageType=repr(self._messageType),
      payload=repr(self._payload))

Anki.Cozmo.ExternalInterface.GameToGame = GameToGame
del GameToGame

