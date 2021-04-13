# -*- coding: utf-8 -*-
"""
This example will produce a ROOT file with a TEfficiency with fBeta_bin_params filled.
"""
import ROOT

fp = ROOT.TFile.Open("uproot-issue38c.root", "RECREATE")

nbins = 11

h_den = ROOT.TH1F("h_den", "h_den", nbins, 0, 100)
h_num = ROOT.TH1F("h_num", "h_num", nbins, 0, 100)

for i in range(1, nbins):
    h_num.SetBinContent(i, 2 ** i)
    h_den.SetBinContent(i, 2 ** (i + 1))

eff = ROOT.TEfficiency(h_num, h_den)
eff.SetName("TEfficiencyName")
eff.SetTitle("TEfficiencyTitle")

eff.SetBetaBinParameters(0, -1.0, -2.0)
for i in range(1, nbins):
    eff.SetBetaBinParameters(i, 2 ** i, 2 ** (i + 1))

eff.SetBetaBinParameters(nbins, -1.0, -2.0)

h_den.Write()
h_num.Write()
eff.Write()
fp.Close()
