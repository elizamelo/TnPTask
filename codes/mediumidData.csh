#!/bin/csh

cmsRun fitMuonJPsi.py Run2017B mediumid gentrack data data_RunB pt default >& pt_mediumid_DataRun2017B.log & 
cmsRun fitMuonJPsi.py Run2017C mediumid gentrack data data_RunC pt default >& pt_mediumid_DataRun2017C.log & 

cmsRun fitMuonJPsi.py Run2017D mediumid gentrack data data_RunD pt default  >& pt_mediumid_DataRun2017D.log & 

cmsRun fitMuonJPsi.py Run2017E mediumid gentrack data data_RunE pt default >& pt_mediumid_DataRun2017E.log & 


cmsRun fitMuonJPsi.py Run2017B mediumid gentrack data data_RunB eta default>& eta_mediumid_DataRun2017B.log & 

cmsRun fitMuonJPsi.py Run2017C mediumid gentrack data data_RunC eta default>& eta_mediumid_DataRun2017C.log & 

cmsRun fitMuonJPsi.py Run2017D mediumid gentrack data data_RunD eta default>& eta_mediumid_DataRun2017D.log & 

cmsRun fitMuonJPsi.py Run2017E mediumid gentrack data data_RunE eta default>& eta_mediumid_DataRun2017E.log & 


cmsRun fitMuonJPsi.py Run2017B mediumid gentrack data data_RunB vtx default>& vtx_mediumid_DataRun2017B.log & 

cmsRun fitMuonJPsi.py Run2017C mediumid gentrack data data_RunC vtx default>& vtx_mediumid_DataRun2017C.log & 

cmsRun fitMuonJPsi.py Run2017D mediumid gentrack data data_RunD vtx default>& vtx_mediumid_DataRun2017D.log & 

cmsRun fitMuonJPsi.py Run2017E mediumid gentrack data data_RunE vtx default>& vtx_mediumid_DataRun2017E.log & 

cmsRun fitMuonJPsi.py Run2017B mediumid gentrack data data_RunB pt_eta default>& pt_eta_mediumid_DataRun2017B.log & 

cmsRun fitMuonJPsi.py Run2017C mediumid gentrack data data_RunC pt_eta default>& pt_eta_mediumid_DataRun2017C.log & 

cmsRun fitMuonJPsi.py Run2017D mediumid gentrack data data_RunD pt_eta default>& pt_eta_mediumid_DataRun2017D.log & 

cmsRun fitMuonJPsi.py Run2017E mediumid gentrack data data_RunE pt_eta default>& pt_eta_mediumid_DataRun2017E.log & 


