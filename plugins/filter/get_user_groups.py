#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'get_user_groups': self.get_user_groups
        }

    def get_user_groups(self, origin_dict):
        tresult=[]
        main_group=origin_dict['main_groupname']
        if 'groups' in origin_dict:
            for key, value in origin_dict['groups'].items():
                if value:
                    if main_group!=key:
                        tresult.append(key)
        result=""
        for item in tresult:
            result=result+item+","
        if result!="":
            result=result[:-1]
        return result
