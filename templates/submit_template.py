import sys
import os
from subprocess import getstatusoutput
from subprocess import getoutput
import datetime

import glob
import argparse

def submit(run, path, inpath, prefix, minamp, maxamp, queue, job_dir):
    jobname = f'{job_dir}/corrected_templates_{prefix}'
    fsh = open (jobname+'.sh', 'w')
    fsh.write ('#!/bin/sh' + '\n\n')
    fsh.write ('cd '+path+' \n')
    fsh.write ('source scripts/setup.sh \n')
    fsh.write (f'python templates/corrected_template.py --run {run} --prefix {prefix} --minamp {minamp} --maxamp {maxamp} --path {inpath}\n\n')
    fsh.close ()
    #---HTCondor submit file
    fsub = open (f'{jobname}.sub', 'w')
    fsub.write('+JobFlavour = "'+queue+'"\n\n')
    fsub.write('executable  = '+jobname+'.sh\n')
    fsub.write('arguments   = $(ProcId)\n')
    fsub.write('output      = '+job_dir+'/output/templ.$(ClusterId).$(ProcId).out\n')
    fsub.write('error       = '+job_dir+'/output/templ.$(ClusterId).$(ProcId).err\n')
    fsub.write('log         = '+job_dir+'/log/templ.$(ClusterId).log\n\n')
    fsub.write('max_retries = 3\n')
    fsub.write('queue 1\n')
    fsub.close()
    #---submit
    getstatusoutput('chmod 755 '+jobname+ '*')
    getstatusoutput('mkdir -p '+job_dir+'/output')
    getstatusoutput('mkdir -p '+job_dir+'/log')
    ret = getstatusoutput('condor_submit '+jobname+'.sub')
    print(ret)

if __name__ == '__main__':
    parser = argparse.ArgumentParser (description = 'submit corrected_template.py to condor')
    parser.add_argument('-r', '--run' , help='run to be processed')
    parser.add_argument('-q', '--queue' , default = 'espresso', help='batch queue/condor flavour (def: longlunch)')
    parser.add_argument('--minamp' , type = int, default = 1500)
    parser.add_argument('--maxamp' , type = int, default = 3000)
    parser.add_argument('--path' , default = '/eos/home-c/camendol/ECALTB/ECAL_TB_Oct2021/ntuples/ECAL_H4_Oct2021_templates/ntuples_templates_v5/')
    
    args = parser.parse_args ()

    local_path = getoutput('pwd')
    date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    job_dir = local_path+"/JobReport/"+date+"_templates"
    print ("Jobs directory: " + job_dir)
    getstatusoutput('mkdir -p '+job_dir)

    run = args.run
    #dummy splitting: just split in 9 or less jobs
    files = glob.glob(f'{args.path}/{run}/*.root')
    njobs = int(len(files)/10)
    print(f'... I should do {njobs} jobs')
    if njobs > 9: njobs = 9
    print(f'submitting run {run}, {njobs} jobs to queue {args.queue}')

    for prefix in range(1, njobs+1):
        #print(prefix)
        #print(f'{args.path}/{run}/{prefix}*.root')
        submit(run, local_path, args.path, prefix, args.minamp, args.maxamp, args.queue, job_dir)
