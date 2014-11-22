#neolandscape
============

Application Landscape Virtualization using Neo4j
## Global Structure
###Landscape Importer (ETL)
This container will be used to import the different landscape resources into the neo4j database. It is based on the tpires/neo4j image, it start a database instance and used the neo4j toolset for importing data.

The importer will take all query's in the /var/data/cypher directory (ending on .cy extension) sort them alphabetically and feed them into the neo4j-shell for execution. This action will be performed by the default launch script for the container

## Interesting queries
### Import data
	// Import CSV
	load csv with headers from "file:///var/data/registratie_totaal.csv" as csvLine
	merge (c:Customer {naam: csvLine.Customer})
	merge (a:Application {naam: csvLine.Application})
	merge (c) -[:OWNS]-> (a)

###Delete all
	// delete all
	match (n) -[r]-> () delete n,r

###Show Customer Infra
	// select customer
	match (c:Customer) -[:OWNS *]-> (n) where c.naam = 'klic' return c, n

