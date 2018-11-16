#!/bin/csh

cmsRun fitMuonJpsi.py Run2016B_H mediumid gentrack mc mc_all pt_eta default >& pt_eta_mediumid_mc.log &
cmsRun fitMuonJpsi.py Run2016B_H mediumid gentrack mc mc_all pt default >& pt_mediumid_mc.log &
cmsRun fitMuonJpsi.py Run2016B_H mediumid gentrack mc mc_all vtx default>& vtx_mediumid_mc.log &
cmsRun fitMuonJpsi.py Run2016B_H mediumid gentrack mc mc_all eta default >& eta_mediumid_mc.log &


