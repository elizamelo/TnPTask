#!/bin/csh

cmsRun fitMuonJPsi.py Run2017B tightid gentrack data data_RunB pt default >& pt_tightid_DataRun2017B.log & 
cmsRun fitMuonJPsi.py Run2017C tightid gentrack data data_RunC pt default >& pt_tightid_DataRun2017C.log & 

cmsRun fitMuonJPsi.py Run2017D tightid gentrack data data_RunD pt default  >& pt_tightid_DataRun2017D.log & 

cmsRun fitMuonJPsi.py Run2017E tightid gentrack data data_RunE pt default >& pt_tightid_DataRun2017E.log & 


cmsRun fitMuonJPsi.py Run2017B tightid gentrack data data_RunB eta default>& eta_tightid_DataRun2017B.log & 

cmsRun fitMuonJPsi.py Run2017C tightid gentrack data data_RunC eta default>& eta_tightid_DataRun2017C.log & 

cmsRun fitMuonJPsi.py Run2017D tightid gentrack data data_RunD eta default>& eta_tightid_DataRun2017D.log & 

cmsRun fitMuonJPsi.py Run2017E tightid gentrack data data_RunE eta default>& eta_tightid_DataRun2017E.log & 


cmsRun fitMuonJPsi.py Run2017B tightid gentrack data data_RunB vtx default>& vtx_tightid_DataRun2017B.log & 

cmsRun fitMuonJPsi.py Run2017C tightid gentrack data data_RunC vtx default>& vtx_tightid_DataRun2017C.log & 

cmsRun fitMuonJPsi.py Run2017D tightid gentrack data data_RunD vtx default>& vtx_tightid_DataRun2017D.log & 

cmsRun fitMuonJPsi.py Run2017E tightid gentrack data data_RunE vtx default>& vtx_tightid_DataRun2017E.log & 

cmsRun fitMuonJPsi.py Run2017B tightid gentrack data data_RunB pt_eta default>& pt_eta_tightid_DataRun2017B.log & 

cmsRun fitMuonJPsi.py Run2017C tightid gentrack data data_RunC pt_eta default>& pt_eta_tightid_DataRun2017C.log & 

cmsRun fitMuonJPsi.py Run2017D tightid gentrack data data_RunD pt_eta default>& pt_eta_tightid_DataRun2017D.log & 

cmsRun fitMuonJPsi.py Run2017E tightid gentrack data data_RunE pt_eta default>& pt_eta_tightid_DataRun2017E.log & 

