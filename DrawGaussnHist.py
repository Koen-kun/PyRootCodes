#!/usr/bin/python
#import ROOT as root
import ROOT
from ROOT import TCanvas
from ROOT import TProfile2D
from ROOT import TH2D
from ROOT import gROOT
from array import array

#from ROOT import std 
import sys
import re
import os, os.path
import math

gROOT.Reset()

#Historgram
hpx = ROOT.TH1F("hpx","This is the px distribution",64,-4,4)

#Function
sqroot = ROOT.TF1("sqroot","gaus(0)",-4,4)
sqroot.SetParameters(2500,0,1)
sqroot.SetLineColor(4)
sqroot.SetLineWidth(4)

c1 = ROOT.TCanvas("c1","Filling Example",800,600)

benchmarkName = "hsimple"
ROOT.gBenchmark.Start(benchmarkName)

r = ROOT.TRandom3()
rD = ROOT.Double
px, py, pz = rD(0.), rD(0.), rD(0.)
for i in range(50000):
  r.Rannor(px,py)
  hpx.Fill(px)

ROOT.gBenchmark.Show(benchmarkName)

hpx.SetFillColor(0)

hpx.SetFillColor(ROOT.kBlue-10)
hpx.SetLineColor(ROOT.kBlue)
hpx.Draw()
sqroot.Draw("same")
c1.Draw()

var = raw_input("Please enter something to end the script!")

