// Import CSV
load csv with headers from "file:///var/data/registratie_totaal.csv" as csvLine
  merge (c:Customer {naam: csvLine.Customer})
  merge (a:Application {naam: csvLine.Application})
  merge (c) -[:OWNS]-> (a);
