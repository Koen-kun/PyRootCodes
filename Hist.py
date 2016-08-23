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


filename = "hsimple.root"
hfile = ROOT.TFile(filename,"RECREATE","Demo ROOT file with histograms")
hpx = ROOT.TH1F("hpx","This is the px distribution",64,-4,4)

hpxpy = ROOT.TH2F("hpxpy","py vs px",64,-4,4,64,-4,4)
hprof = ROOT.TProfile("hprof","Profile of pz versus px",64,-4,4,0,20)
ntuple = ROOT.TNtuple("ntuple","Demo ntuple","px:py:pz:random:i")

c1 = ROOT.TCanvas("c1","Filling Example",800,600)

benchmarkName = "hsimple"
ROOT.gBenchmark.Start(benchmarkName)

r = ROOT.TRandom3()
rD = ROOT.Double
px, py, pz = rD(0.), rD(0.), rD(0.)
for i in range(50000):
    r.Rannor(px,py)
    pz = px*px + py*py
    rnd = r.Rndm()
    hpx.Fill(px)
    hpxpy.Fill(px,py)
    hprof.Fill(px,pz)
    ntuple.Fill(px,py,pz,rnd,i)

ROOT.gBenchmark.Show(benchmarkName)

hpx.SetFillColor(0)
print "Bytes written:", hfile.Write()

hpx.SetFillColor(ROOT.kBlue-10)
hpx.SetLineColor(ROOT.kBlue)
hpx.Draw()
c1.Draw()

var = raw_input("Please enter something to end the script!")

