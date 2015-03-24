from com.xebialabs.deployit.plugin.api.reflect import Descriptor
from com.xebialabs.deployit.plugin.api.reflect import DescriptorRegistry
from com.xebialabs.deployit.plugin.api.reflect import PropertyDescriptor
from java.util import Iterator

#SET THE APP_ENV to limit data searched
APP_ENV = 'klic-fto'

header = 'Deployed App Name;Deployed App Id;Deployed Name;Deployed Id;Deployed Type;Deployed Container;Property Name;Property Kind;Property Value'
fo = open("neo4j.csv","w")
fo.write(header + '\n')
envs = repository.search('udm.Environment', 'Environments/%s/environment' % (APP_ENV))
for env in envs:
  apps = repository.search('udm.DeployedApplication', env)
  for appId in apps:
    deployedApp = repository.read(appId)
    for deployedId in deployedApp.deployeds:
      deployed = repository.read(deployedId)
      descriptor = DescriptorRegistry.getDescriptor(deployed.type)
      iterator = descriptor.getPropertyDescriptors().iterator()
      for pd in iterator:
        row = '%s;%s;%s;%s;%s;%s;%s;%s;%s' % (deployedApp.name, deployedApp.id, deployed.name, deployed.id, deployed.type, deployed.container, pd.getName(), pd.getKind(), pd.get(deployed._ci))
        fo.write(row + '\n')
fo.close()
