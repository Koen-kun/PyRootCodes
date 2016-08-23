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

#H1 and H0 hypothesis
H1 = ROOT.TF1("H1","gausn(0)",-9,8)
H1.SetParameters(1,0,2.2)
H0 = ROOT.TF1("H0","gausn(0)",-9,8)
H0.SetParameters(1,-2,2)

#Expected areas
expH1 = ROOT.TF1("expH1","gausn(0)",-9,-2)
expH1.SetParameters(1,0,2.2)
expH0 = ROOT.TF1("expH0","gausn(0)",0,8)
expH0.SetParameters(1,-2,2)

#Expected lines
medH1 = ROOT.TLine(0,0.22,0,0.)
medH1.SetLineColor(ROOT.kRed)
medH1.SetLineWidth(3)
medH1.SetLineStyle(7)
medH0 = ROOT.TLine(-2,0.22,-2,0.)
medH0.SetLineColor(ROOT.kBlue)
medH0.SetLineWidth(3)
medH0.SetLineStyle(7)

c1 = ROOT.TCanvas("c1","Filling Example",800,600)

#Draw settings for H1 and H0 histograms
#H1.SetFillStyle(1001)
H1.SetFillColor(ROOT.kRed-10)
H1.SetLineColor(ROOT.kRed)
H1.SetLineWidth(4)
#H0.SetFillStyle(1001)
H0.SetFillColor(ROOT.kBlue-10)
H0.SetLineColor(ROOT.kBlue)
H0.SetLineWidth(4)
H0.SetMaximum(0.27)
H0.SetTitle("")
H0.GetXaxis().SetTitle("Test statistic (q)")
H0.GetXaxis().SetTitleOffset(0.9)
H0.GetXaxis().SetTitleSize(0.05) #0.04
H0.GetXaxis().SetLabelSize(0.04) 
H0.GetYaxis().SetTitle("Probability density")
H0.GetYaxis().SetTitleOffset(1.0)
H0.GetYaxis().SetTitleSize(0.05) #0.04
H0.GetYaxis().SetLabelSize(0.04) 

#Expected areas
expH1.SetFillStyle(1001)
expH1.SetFillColor(ROOT.kRed-10)
expH1.SetLineColor(ROOT.kRed)
expH1.SetLineWidth(4)
expH0.SetFillStyle(1001)
expH0.SetFillColor(ROOT.kBlue-10)
expH0.SetLineColor(ROOT.kBlue)
expH0.SetLineWidth(4)

#Draw Functions
H0.Draw()
H1.Draw("same")
expH0.Draw("same")
expH1.Draw("same")

#Draw Lines
medH1.Draw()
medH0.Draw()

#Add some text to the lines
text = ROOT.TPaveText(.38,0.75,0.50,0.9,"NDC") #Doesn't show up without NDC!
text.SetFillStyle(0)
text.SetTextSize(0.06) #0.04
text.SetBorderSize(0)
text.SetFillColor(0)
text.SetTextFont(42)
text.AddText("q^{exp}_{H0}")
text.Draw()
text2 = ROOT.TPaveText(.47,0.75,0.60,0.9,"NDC") #Doesn't show up without NDC!
text2.SetFillStyle(0)
text2.SetTextSize(0.06) #0.04
text2.SetBorderSize(0)
text2.SetFillColor(0)
text2.SetTextFont(42)
text2.AddText("q^{exp}_{H1}")
text2.Draw()

#Draw Legend
leg = ROOT.TLegend(0.70,0.75,0.93,0.88)
leg.SetFillStyle(0)
leg.SetTextSize(0.06)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetTextFont(42)
leg.AddEntry(H0,"H0","l")
leg.AddEntry(H1,"H1","l")
leg.Draw()
leg2 = ROOT.TLegend(0.70,0.56,0.93,0.75)
leg2.SetFillStyle(0)
leg2.SetTextSize(0.06)
leg2.SetBorderSize(0)
leg2.SetFillColor(0)
leg2.SetTextFont(42)
leg2.AddEntry(expH0,"p^{exp}_{H0}","f")
leg2.AddEntry(expH1,"p^{exp}_{H1}","f")
leg2.Draw()


#Draw Canvas
c1.Draw()

var = raw_input("Please enter something to end the script!")

