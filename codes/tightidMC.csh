#!/bin/csh

cmsRun fitMuonJPsi.py Run2017B tightid gentrack mc mc_RunB pt default >& pt_tightid_mcRun2017B.log & 
cmsRun fitMuonJPsi.py Run2017C tightid gentrack mc mc_RunC pt default >& pt_tightid_mcRun2017C.log & 

cmsRun fitMuonJPsi.py Run2017D tightid gentrack mc mc_RunD pt default  >& pt_tightid_mcRun2017D.log & 

cmsRun fitMuonJPsi.py Run2017E tightid gentrack mc mc_RunE pt default >& pt_tightid_mcRun2017E.log & 


cmsRun fitMuonJPsi.py Run2017B tightid gentrack mc mc_RunB eta default>& eta_tightid_mcRun2017B.log & 

cmsRun fitMuonJPsi.py Run2017C tightid gentrack mc mc_RunC eta default>& eta_tightid_mcRun2017C.log & 

cmsRun fitMuonJPsi.py Run2017D tightid gentrack mc mc_RunD eta default>& eta_tightid_mcRun2017D.log & 

cmsRun fitMuonJPsi.py Run2017E tightid gentrack mc mc_RunE eta default>& eta_tightid_mcRun2017E.log & 


cmsRun fitMuonJPsi.py Run2017B tightid gentrack mc mc_RunB vtx default>& vtx_tightid_mcRun2017B.log & 

cmsRun fitMuonJPsi.py Run2017C tightid gentrack mc mc_RunC vtx default>& vtx_tightid_mcRun2017C.log & 

cmsRun fitMuonJPsi.py Run2017D tightid gentrack mc mc_RunD vtx default>& vtx_tightid_mcRun2017D.log & 

cmsRun fitMuonJPsi.py Run2017E tightid gentrack mc mc_RunE vtx default>& vtx_tightid_mcRun2017E.log & 

cmsRun fitMuonJPsi.py Run2017B tightid gentrack mc mc_RunB pt_eta default>& pt_eta_tightid_mcRun2017B.log & 

cmsRun fitMuonJPsi.py Run2017C tightid gentrack mc mc_RunC pt_eta default>& pt_eta_tightid_mcRun2017C.log & 

cmsRun fitMuonJPsi.py Run2017D tightid gentrack mc mc_RunD pt_eta default>& pt_eta_tightid_mcRun2017D.log & 

cmsRun fitMuonJPsi.py Run2017E tightid gentrack mc mc_RunE pt_eta default>& pt_eta_tightid_mcRun2017E.log & 

