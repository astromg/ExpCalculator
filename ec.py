#!/usr/bin/env python3
#  mgorski
#  25.07.2022

import numpy


class TelInstrument():
      
      
      def __init__(self,parent=None):
          # telescope parameters
          self.mirror=1.5
          
          # instrument parameters
          self.pixsize=0.07
          self.dark = 0.1
          self.readoutnoise = 5.

          # conditions
          self.seeing=0.1
          self.background_V = 5.
          
          # star parameters
          self.V=20
          self.VI=1.0
          
          # exposure conditions
          self.exp_time = 600.0
          self.StN = False
      
      def calc(self):
          self.background=self.background_V
          self.m = 15. - self.V
          self.radiation= 610 * (0.1/self.seeing)**2

          self.star_ADU = self.radiation * 10**(self.m/2.5) * (self.mirror*self.mirror) /1.0   * self.exp_time
          self.background_ADU = (self.dark + self.background * (self.pixsize/0.07)**2. ) * self.exp_time
          self.noise_ADU = (self.star_ADU+self.background_ADU) ** 0.5 + self.readoutnoise

          
          self.StN = self.star_ADU / self.noise_ADU
          
          print(self.StN)
          print(self.star_ADU+self.background_ADU)
          
DibiImg = TelInstrument()
DibiImg.calc()
