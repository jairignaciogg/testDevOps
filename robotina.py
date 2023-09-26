import os
import sys
origen = sys.argv[1]
destino = sys.argv[2]

os.system("git fetch")
os.system("git checkout "+destino)
os.system("git pull "+destino)
os.system("git checkout "+origen)
os.system("git pull "+origen)
os.system("git config --global core.quotepath off")
os.system("git config --global i18n.logoutputencoding utf8")
os.system("git config --global i18n.commitencoding utf8")
os.system("git config --global --unset svn.pathnameencoding")
#os.system("git diff --name-only --diff-filter=AMR " +
#         destino + " " + origen + " > cambios.txt")
os.system("git diff --name-only --diff-filter=AMR remotes/origin/" +
         destino + " remotes/origin/" + origen + " > cambios.txt")
os.system("git rm -r .")
os.system("git reset .")
file1 = open('cambios.txt', 'r')
Lines = file1.readlines()

def listToString(s, a=''):
    str1 = "/"
    strComm = "git checkout \"" + str1.join(s) + a + "\""
    print("Print ====== "+ strComm)
    os.system(strComm)


for line in Lines:
    componente = line.replace(chr(0), "")
    s = line.split("/")
    if len(s) > 1:
        s.pop()
    if s[0] == "Salesforce" or s[0] == "force-app" :
        if s[3] == "lwc" or s[3] == "objects" or s[3] == "aura" or s[3] == "email":
            listToString(s[0:5])
        elif s[3] == "experiences" or s[3] == "staticresources":
            listToString(s[0:4])
        elif s[3] == "classes" or s[3]=="pages":
            w = componente.split('.')
            w.pop()
            listToString(w, '.*')
        else:
            os.system("git checkout \"" + componente[0:-1] + "\"")
        if len(s) > 4 and  s[4] == "unfiled$public":
            w = componente.split('.')
            w.pop()
            listToString(w, '.*')
    else:
        if s[0] == "Vlocity" and (s[1]=="VlocityPicklist" or s[1]=="VlocityAttachment" or s[1]=="IUSection" or s[1]=="IUFacet" or s[1]=="Promotion" or 
        s[1]=="PricingVariable" or s[1]=="PriceList" or s[1]=="Pricebook2" or s[1]=="ObjectLayout" or s[1]=="ObjectClass" or s[1]=="Catalog" or s[1]=="AttributeCategory" or 
        s[1]=="AttributeAssignmentRule" or s[1]=="CalculationMatrix" or s[1]=="CalculationProcedure" or s[1]=="DataRaptor" or s[1]=="IntegrationProcedure" or 
        s[1]=="ItemImplementation" or s[1]=="OmniScript" or s[1]=="OrchestrationDependencyDefinition" or s[1]=="OrchestrationItemDefinition" or 
        s[1]=="OrchestrationPlanDefinition" or s[1]=="SObject_DecompositionRelationship" or s[1]=="SObject_OrchestrationScenario" or s[1]=="SObject_SystemInterface" or 
        s[1]=="Product2" or s[1]=="RelationshipGraph" or s[1]=="VlocityCard" or s[1]=="VlocityUILayout" or s[1]=="VlocityUITemplate" or s[1]=="SObject_VlocityErrorLogEntry" or 
        s[1]=="VlocityAction" or s[1]=="DocumentTemplate" or s[1]=="ContentVersion" or s[1]=="Rule" or s[1]=="EntityFilter" or s[1]=="InterfaceImplementation" or
        s[1]=="ContextDimension" or s[1]=="ContextScope" or s[1]=="UISection" or s[1]=="UIFacet" or s[1]=="System" or s[1]=="PricingPlan"or s[1]=="IntegrationRetryPolicy" or
        s[1]=="SObject_ContentVersion" or s[1]=="VlocityFunction" or s[1]=="FlexCard" or s[1]=="SObject_System" or s[1]=="Document"):
            listToString(s)
        else:
            os.system("git checkout \"" + componente + "\"")
file1.close()
os.system("git checkout .gitignore")
os.system("git checkout sfdx-project.json")
#os.system("del cambios.txt")