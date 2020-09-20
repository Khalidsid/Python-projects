from atlassian import Bitbucket
def connstring(url,username,password):
   return url, username, password
   ''' #print("URL = ", url)
    #print("username = ", username)
    #print("password = ", password)
    url = input("Bitbucket URL:")
    username = input("Username:")
    password = input("Password:")
    '''
    
def projectdefn():


    name = input("Project Name:")
    key = input("Project Key:")
    description = input("Project Desc:")
def projpermission():


    project_key = key
    group_name = input("GroupName:")
    perm = input("Project Permission:")
    permission = "Project_" + perm()
print("Hello bitbucket")
#connstring()
url = input("Bitbucket URL:")
username = input("Username:")
password = input("Password:")
bitbucket = Bitbucket(connstring(url,username,password))
print(url,username,password)

#bitbucket.create_project(projectdefn(key="BOI", name="CBSP Infra", desc="IMF Team"))
#bitbucket.project_grant_group_permissions(projpermission(project_key, group_name, permission))


#projectdefn()
