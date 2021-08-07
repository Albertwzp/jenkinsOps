# -*- coding: utf-8 -*-

import re
import json
from xml.dom import minidom

import jenkins

class JenkinsOps(object):
    def __init__(self, addr="localhost:8080", username="admin", password="admin"):
        self.addr = addr
        self.username = username
        self.password = password
        self.conn = jenkins.Jenkins(self.addr, self.username, self.password)

    def get_view(self):
        views = []
        viewx = self.conn.get_views()
        print(type(viewx))
        for view in viewx:
            views.append(view["name"])
            #print(self.conn.get_view_config(view["name"]))
        print(views)
            

    def get_project(self, *, view="ALL"):
        jobs = []
        urls = []
        if view == "ALL":
            data = json.dumps(self.conn.get_all_jobs(),indent=2, ensure_ascii=False)
            projects = json.loads(data)
            for project in projects:
                jobs.append(project["fullname"])
                urls.append(project['url'])
        else:
            data = json.dumps(self.conn.get_jobs(view_name=view))
            projects = json.loads(data)
            for project in projects:
                jobs.append(project['name'])
                urls.append(project['url'])
        return jobs
        #print("%s: %s: %s" % (view, jobs, urls))

    def get_job_config(self, jobName='default'):
        data = minidom.parseString(self.conn.get_job_config(jobName))
        config = data.toprettyxml()
        element = data.documentElement.getElementsByTagName('remoteURL')[0].firstChild.nodeValue
        print("%s" % element)

    def re_get_job_config(self, jobName='default', regx=''):
        data = minidom.parseString(self.conn.get_job_config(jobName))
        config = data.toprettyxml()
        reg = re.compile(regx)
        line = reg.search(config).group(1)
        print("%s" % line)

    def create_view(self, name='default'):
        self.conn.create_view(name, jenkins.EMPTY_VIEW_CONFIG_XML)

    def build_project(self, name='default', *, parameters=None):
        self.conn.build_job(name, {'Status': 'Deploy', 'BuildID': ''})

    def rollback_project(self, name='default', id='999'):
        self.conn.build_job(name, {'Status': 'Rollback', 'BuildID': id})
