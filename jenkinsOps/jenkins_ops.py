# -*- coding: utf-8 -*-

import json
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
        if view == "ALL":
            data = json.dumps(self.conn.get_all_jobs(),indent=2, ensure_ascii=False)
            projects = json.loads(data)
            for project in projects:
                jobs.append(project["fullname"])
                #print(project["fullname"])
            print("ALL: ", jobs)
        else:
            data = json.dumps(self.conn.get_jobs(view_name=view))
            projects = json.loads(data)
            for project in projects:
                jobs.append(project['name'])
            print("%s: %s" % (view, jobs))

    def create_view(self, name='default'):
        self.conn.create_view(name, jenkins.EMPTY_VIEW_CONFIG_XML)

    def build_project(self, name='default', *, parameters=None):
        self.conn.build_job(name, {'Status': 'Deploy', 'BuildID': ''})

    def rollback_project(self, name='default', id='999'):
        self.conn.build_job(name, {'Status': 'Rollback', 'BuildID': id})
