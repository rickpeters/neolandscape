FROM tpires/neo4j

MAINTAINER Rick Peters rick.peters@kadaster.nl

# this images is used for importing data to a neo4j grpah database for visualization
# of application landscape, meaning their important objects and relation between
# them
# the assumption is that a lot of objects and relations can be inferred from
# several sources, but bringing thos together is the trick
# as such this image will gather files to be imported and runs cypher scripts
# to import and transfer the data
# in essence is is the ETL proces for the landscape visualizer
#

ADD ./data /var/data

RUN export PATH=$PATH:/var/lib/neo4j/bin

