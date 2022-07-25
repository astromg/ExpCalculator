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
          
          # conditions
          self.seeing=0.1
          
          # star parameters
          self.V=20
          self.VI=1.0
          
          # exposure conditions
          self.exp_time = 100.0
          self.StN = False
      
      def calc(self):
          self.star_ADU = 610 * 10**((15-self.V)/2.5) * (self.mirror*self.mirror) /1.0     * self.exp_time
          self.noise_ADU = self.star_ADU ** 0.5
          
          self.StN = self.star_ADU / self.noise_ADU
          
          print(self.StN)
          
DibiImg = TelInstrument()
DibiImg.calc()
