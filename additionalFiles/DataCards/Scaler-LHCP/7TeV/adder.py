#! /usr/bin/env python

import sys
import os
import commands
import string
mass=["110","110.5","111","111.5","112","112.5","113","113.5","114","114.5","115","115.5","116","116.5","117","117.5","118","118.5","119","119.5","120","120.5","121","121.5","122","122.5","123","123.5","124","124.5","125","125.5","126","126.5","127","127.5","128","128.5","129","129.5","130","130.5","131","131.5","132","132.5","133","133.5","134","134.5","135","124.6","124.7","124.8","124.9","125.1","125.2","125.3","125.4","125.6","125.7","125.8","125.9","126.1","126.2","126.3","126.4"];


for item in mass2:
    print item
    os.system("hadd %s/vhbb_Wenu_7TeV.inputR.root %s/vhbb_Wenu_7TeV.input_Rebin.root %s/vhbb_Wenu_7TeV.input_2_Rebin.root" %(item,item,item))
    os.system("hadd %s/vhbb_Wmnu_7TeV.inputR.root %s/vhbb_Wmnu_7TeV.input_Rebin.root %s/vhbb_Wmnu_7TeV.input_2_Rebin.root" %(item,item,item))

