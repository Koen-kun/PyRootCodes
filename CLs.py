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
H1 = ROOT.TF1("H1","gausn(0)",-7,10)
H1.SetParameters(1,0,2.2)
H0 = ROOT.TF1("H0","gausn(0)",-7,10)
H0.SetParameters(1,-0.5,2)

#Expected areas
obsH1 = ROOT.TF1("expH1","gausn(0)",3.5,10)
obsH1.SetParameters(1,0,2.2)
obsH0 = ROOT.TF1("expH0","gausn(0)",3.5,10)
obsH0.SetParameters(1,-0.5,2)

#Expected lines
medH1 = ROOT.TLine(0,0.22,0,0.)
medH1.SetLineColor(ROOT.kRed)
medH1.SetLineWidth(3)
medH1.SetLineStyle(7)
medH0 = ROOT.TLine(-0.5,0.22,-0.5,0.)
medH0.SetLineColor(ROOT.kBlue)
medH0.SetLineWidth(3)
medH0.SetLineStyle(7)

#Observed line
obs = ROOT.TLine(3.5,0.22,3.5,0.)
obs.SetLineColor(ROOT.kBlack)
obs.SetLineWidth(3)
obs.SetLineStyle(7)

#Canvas
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

#Observed areas
obsH1.SetFillStyle(3004)
obsH1.SetFillColor(ROOT.kRed)
obsH1.SetLineColor(ROOT.kRed)
obsH1.SetLineWidth(4)
obsH0.SetFillStyle(3005)
obsH0.SetFillColor(ROOT.kBlue)
obsH0.SetLineColor(ROOT.kBlue)
obsH0.SetLineWidth(4)

#Draw Functions
H0.Draw()
H1.Draw("same")
obsH0.Draw("same")
obsH1.Draw("same")

#Draw Lines
medH1.Draw()
medH0.Draw()
obs.Draw()

#Add some text to the lines
#text = ROOT.TPaveText(.38,0.75,0.50,0.9,"NDC") #Doesn't show up without NDC!
#text.SetFillStyle(0)
#text.SetTextSize(0.04)
#text.SetBorderSize(0)
#text.SetFillColor(0)
#text.SetTextFont(42)
#text.AddText("q^{exp}_{H0}")
#text.Draw()
#text2 = ROOT.TPaveText(.47,0.75,0.60,0.9,"NDC") #Doesn't show up without NDC!
#text2.SetFillStyle(0)
#text2.SetTextSize(0.04)
#text2.SetBorderSize(0)
#text2.SetFillColor(0)
#text2.SetTextFont(42)
#text2.AddText("q^{exp}_{H1}")
#text2.Draw()
textobs = ROOT.TPaveText(.6,0.72,0.60,0.9,"NDC") #Doesn't show up without NDC!
textobs.SetFillStyle(0)
textobs.SetTextSize(0.06)
textobs.SetBorderSize(0)
textobs.SetFillColor(0)
textobs.SetTextFont(42)
textobs.AddText("q^{obs}")
textobs.Draw()

#Draw Legend
#leg = ROOT.TLegend(0.70,0.55,0.93,0.91)
#leg.SetFillStyle(0)
#leg.SetTextSize(0.05)
#leg.SetBorderSize(0)
#leg.SetFillColor(0)
#leg.SetTextFont(42)
#leg.AddEntry(H0,"H0","l")
#leg.AddEntry(H1,"H1","l")
#leg.AddEntry(obsH0,"p^{obs}_{H0}","f")
#leg.AddEntry(obsH1,"p^{obs}_{H1}","f")
#leg.Draw()

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
leg2.AddEntry(obsH0,"p^{obs}_{H0}","f")
leg2.AddEntry(obsH1,"p^{obs}_{H1}","f")
leg2.Draw()


#Draw Canvas
c1.Draw()

var = raw_input("Please enter something to end the script!")

