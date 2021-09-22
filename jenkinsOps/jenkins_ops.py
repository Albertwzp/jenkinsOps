# -*- coding: utf-8 -*-

import re
import json
from xml.dom import minidom

import jenkins

class JenkinsOps(jenkins.Jenkins):
    def __init__(self, url="localhost:8080", username="admin", password="admin"):
       jenkins.Jenkins.__init__(self, url, username, password)

    def get_view_list(self):
        views = []
        viewx = self.get_views()
        print(type(viewx))
        for view in viewx:
            views.append(view["name"])
            #print(self.get_view_config(view["name"]))
        print(views)
            

    def get_job_list(self, *, view="ALL"):
        jobs = []
        urls = []
        if view == "ALL":
            data = json.dumps(self.get_all_jobs(),indent=2, ensure_ascii=False)
            projects = json.loads(data)
            for project in projects:
                jobs.append(project["fullname"])
                urls.append(project['url'])
        else:
            data = json.dumps(self.get_jobs(view_name=view))
            projects = json.loads(data)
            for project in projects:
                jobs.append(project['name'])
                urls.append(project['url'])
        return jobs
        #print("%s: %s: %s" % (view, jobs, urls))

    def get_job_param(self, jobName='default', param='remoteURL'):
        data = minidom.parseString(self.get_job_config(jobName))
        config = data.toprettyxml()
        element = data.documentElement.getElementsByTagName(param)[0].firstChild.nodeValue
        print("%s" % element)

    def re_get_job_param(self, jobName='default', regx=''):
        data = minidom.parseString(self.get_job_config(jobName))
        config = data.toprettyxml()
        reg = re.compile(regx)
        line = reg.search(config).group(1)
        print("%s" % line)

    def get_job_dump(self, jobName='default'):
        data = self.get_job_info(jobName)
        return json.dumps(data, indent=2)

    def get_build_param(self, jobName='default', num=None):
        if num is None:
            num = self.get_job_info(jobName)["lastBuild"]["number"]
        build_info = self.get_build_info(jobName, num)
        return json.dumps(build_info, indent=2)
#	
#    def create_view(self, name='default'):
#        self.create_view(name, jenkins.EMPTY_VIEW_CONFIG_XML)
#
#    def build_project(self, name='default', *, parameters=None):
#        self.build_job(name, parameters=parameters)
#
#    def rollback_project(self, name='default', id='999'):
#        self.build_job(name, {'Status': 'Rollback', 'BuildID': id})
