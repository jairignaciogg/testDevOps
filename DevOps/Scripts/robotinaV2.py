import os
import sys

def diff(origen, destino, filter, file):
    os.system("git fetch")
    os.system("git checkout "+destino)
    os.system("git pull ")
    os.system("git checkout "+origen)
    os.system("git pull ")
    os.system("git config --global core.quotepath off")
    os.system("git config --global i18n.logoutputencoding utf8")
    os.system("git config --global i18n.commitencoding utf8")
    os.system("git config --global --unset svn.pathnameencoding")
    os.system("git diff --name-only --diff-filter=" + filter + " remotes/origin/" + 
                destino + "...remotes/origin/" + origen + " | sort > " + file)

def copyTempFiles(carpeta, s, a=''):
    if type(s) is list:
        str1 = "/"
        comm = 'cp --parents "'+ str1.join(s) + '"' + a + ' ' + carpeta
    else:
        comm = 'cp --parents "'+ s + '"' + a + ' ' + carpeta
    return comm

def createTempFiles(file, carpeta):
    diffCheck = {'package': False, 'vlocity': False}
    lstComms = set()
    fileOpen = open(file, 'r')
    lines = fileOpen.readlines()
    for line in lines:
        componente = line.replace(chr(0), "")
        s = line.split("/")
        if len(s) > 1:
            s.pop()
        if s[0] == "Salesforce":
            diffCheck['package'] = True
            if s[3] == "lwc" or s[3] == "aura":
            # Carpeta por metadato
                lstComms.add(copyTempFiles(carpeta, s[0:5], '/*'))
            elif s[3] == "classes" or s[3]=="contentassets" or s[3]=="email" or s[3]=="pages" or s[3]=="staticresources" or s[3]=="triggers":
            # Dos archivos por metadato
                w = componente.split('.')
                lstComms.add(copyTempFiles(carpeta, w[0], '.*'))
            else:
            # Un archivo por metadato
                lstComms.add(copyTempFiles(carpeta, componente[0:-1]))
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
                diffCheck['vlocity'] = True
                lstComms.add(copyTempFiles(carpeta, s, '/*'))
    for comm in lstComms:
        print(comm)
        os.system(comm)
    return diffCheck
            

def createXML(path,types):
    os.system("sf project generate manifest --source-dir " + path + " --type " + types)

if __name__ == "__main__":
    origen = sys.argv[1]
    destino = sys.argv[2]

    carpeta = 'temp-Deploy'
    os.system("rm -r " + carpeta)
    os.system("mkdir " + carpeta)
    diff(origen, destino, 'AMR', 'temp-diff.txt')
    diffcheck = createTempFiles('temp-diff.txt', carpeta)
    if diffcheck['package']:
        createXML("temp-Deploy/Salesforce",'package')