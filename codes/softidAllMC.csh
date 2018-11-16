#!/bin/csh

cmsRun fitMuonJpsi.py Run2016B_H softid gentrack mc mc_all pt_eta default >& pt_eta_softid_mc.log &
cmsRun fitMuonJpsi.py Run2016B_H softid gentrack mc mc_all pt default >& pt_softid_mc.log &
cmsRun fitMuonJpsi.py Run2016B_H softid gentrack mc mc_all vtx default>& vtx_softid_mc.log &
cmsRun fitMuonJpsi.py Run2016B_H softid gentrack mc mc_all eta default >& eta_softid_Data.log &


