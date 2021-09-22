# -*- coding: utf-8 -*-

import yaml
import sys

def load_yaml(file):
    with open(file, encoding='utf-8') as f:
        data = f.read()
        return yaml.safe_load_all(data)

if __name__ == '__main__':
    abc = load_yaml("./appinfo.yml")
    for item in abc:
        #print(item['project'].keys())
        projects =item['project']
        project ={}
        for k,v in projects.items():
            if 'backend' in v:
                 backends = v['backend']['models']
                 for i in backends:
                     #print(i)
                     app = i['appname']
                     if app not in project:
                         project[app] = {}
                     #print(v['backend'])
                     project[app]['env_list'] = list(v['env_list'])
                     if 'backend' not in project[app]:
                         project[app]['backend'] = {}
                     project[app]['backend']['description'] = v['backend']['description']
                     project[app]['backend']['git_url'] = v['backend']['git_url']
                     if 'models' not in project[app]['backend']:
                         project[app]['backend']['models'] = []
                     project[app]['backend']['models'].append(i)
                     #dicb = {}
                     #print(dicb)
                     #if 'frontend' in dicb[app]:
                     #    dicb[app].pop('frontend')
                     #dicb[app]['backend']['models'] = i
                     #if app in project:
                     #    project[app]['backend'] = dicb[app]['backend']
                     #else:
                     #    project[app] = dicb
                     #print(dicb)
            if 'frontend' in v:
                 fronts = v['frontend']['info']
                 for i in fronts:
                     #print(i)
                     if i['type'] == 'h5':
                         app = i['service_name']
                         project[app] = {}
                         project[app]['env_list'] = list(v['env_list'])
                     else:
                         app = list(i['backend_appname'].keys())[0]
                         #print(app)
                     #project[app]['frontend']['info'].append(i)
                         if app not in project:
                             print(err)
                         #project[svc] = {}
                     #project[app]['env_list'] = v['env_list']
                     if 'frontend' not in project[app]:
                         project[app]['frontend'] = {}
                     if 'info' not in project[app]['frontend']:
                         project[app]['frontend']['info'] = []
                     project[app]['frontend']['info'].append(i)
                     #dicf = {}
                     #dicf[svc] = v
                     #if 'backend' in dicf[svc]:
                     #    dicb[svc].pop('backend')
                     #dicb[app].pop('backend')
                     #dicf[svc]['frontend']['info'] = i
                     #if svc in projects:
                     #    project[svc]['frontend']['info'].append(dicf[svc]['frontend']['info'][1])
                     #else:
                     #    project[svc] = dicf
                     #print(dicf)
    #print(project)
    proj = {'project': project}
    print(yaml.dump(proj,stream=sys.stdout, allow_unicode=True, default_flow_style=False, sort_keys=False))
    #with open("./abc.txt", 'w') as f:
    #    print(yaml.safe_dump_all(project, f))
