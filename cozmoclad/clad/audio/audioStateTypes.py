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
Source: clad/audio/audioStateTypes.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ./src/ -I ../robot/clad/src/ ../coretech/vision/clad/src/ ../coretech/common/clad/src/ ../lib/util/source/anki/clad -o ../generated/cladPython// clad/audio/audioStateTypes.clad
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
Anki.AudioMetaData.GameState = msgbuffers.Namespace()

class External_Language(object):
  "Automatically-generated uint_32 enumeration."
  English  = 3383237639
  French   = 3133094709
  German   = 4290373403
  Invalid  = 0
  Japanese = 2008704848

Anki.AudioMetaData.GameState.External_Language = External_Language
del External_Language


class External_Name(object):
  "Automatically-generated uint_32 enumeration."
  Design_Pre_Generated_Name = 309148475
  External_Name_On          = 4053302206
  Invalid                   = 0
  Unit_Test_Mock            = 3937202207

Anki.AudioMetaData.GameState.External_Name = External_Name
del External_Name


class GenericState(object):
  "Automatically-generated uint_32 enumeration."
  Invalid = 0

Anki.AudioMetaData.GameState.GenericState = GenericState
del GenericState


class Mood(object):
  "Automatically-generated uint_32 enumeration."
  Happy   = 1427264549
  Invalid = 0
  Neutral = 670611050
  Sad     = 443572635

Anki.AudioMetaData.GameState.Mood = Mood
del Mood


class Music(object):
  "Automatically-generated uint_32 enumeration."
  Alarm_Clock                        = 3653788539
  Codelab                            = 730889831
  Connectivity                       = 1264085260
  Cozmo_Says                         = 2338198982
  Cozmo_Says_Speaking                = 739906331
  Freeplay                           = 150865113
  Invalid                            = 0
  Minigame__Generic                  = 713847863
  Minigame__Keep_Away                = 579475288
  Minigame__Keep_Away_Between_Rounds = 274928299
  Minigame__Keep_Away_Player_Fail    = 2987088935
  Minigame__Keep_Away_Pounce         = 3317810949
  Minigame__Keep_Away_Tension        = 22918831
  Minigame__Meet_Cozmo               = 1580491744
  Minigame__Meet_Cozmo_Say_Name      = 2582275442
  Minigame__Memory_Match             = 1731176119
  Minigame__Memory_Match_Fanfare     = 2262040721
  Minigame__Memory_Match_Full_Life   = 1451808254
  Minigame__Memory_Match_No_Lives    = 2282047959
  Minigame__Quick_Tap_Between_Rounds = 2865488202
  Minigame__Quick_Tap_Round1         = 3954622599
  Minigame__Quick_Tap_Round2         = 3954622596
  Minigame__Quick_Tap_Round3         = 3954622597
  Minigame__Quick_Tap_Win            = 2079381016
  Minigame__Ride_Along               = 3234084100
  Minigame__Setup                    = 1317044071
  Nurture_Repair                     = 3081923682
  Onboarding                         = 3360093794
  Onboarding__Core_Upgrades          = 102695299
  Onboarding__Meet_Cozmo             = 4195748652
  Onboarding__Meet_Cozmo_Say_Name    = 3775866302
  Onboarding__Play_Tab               = 2360281734
  Onboarding__Show_Cube              = 3253479049
  Pause                              = 3092587493
  Silent                             = 3160623154
  Sleep                              = 3671647190
  Spark                              = 155090436

Anki.AudioMetaData.GameState.Music = Music
del Music


class Music_Dimmer(object):
  "Automatically-generated uint_32 enumeration."
  Invalid      = 0
  Music_Dimmed = 920031429
  Music_Full   = 2880332950

Anki.AudioMetaData.GameState.Music_Dimmer = Music_Dimmer
del Music_Dimmer


class StateGroupType(object):
  "Automatically-generated uint_32 enumeration."
  External_Language   = 944413709
  External_Name       = 2869506494
  Invalid             = 0
  Mood                = 3128647864
  Music               = 3991942870
  Music_Dimmer        = 920031443
  Voice_Commands_Mode = 522893720

Anki.AudioMetaData.GameState.StateGroupType = StateGroupType
del StateGroupType


class Voice_Commands_Mode(object):
  "Automatically-generated uint_32 enumeration."
  Invalid     = 0
  Vc_Mode_Off = 1444240748
  Vc_Mode_On  = 2411592966

Anki.AudioMetaData.GameState.Voice_Commands_Mode = Voice_Commands_Mode
del Voice_Commands_Mode

