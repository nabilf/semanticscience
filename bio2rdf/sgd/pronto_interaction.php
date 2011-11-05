<?php

class SGD_PRONTO_INTERACTION {

	function __construct($infile, $outfile)
	{
		$this->_in = fopen($infile,"r");
		if(!isset($this->_in)) {
			trigger_error("Unable to open $infile");
			return 1;
		}
		$this->_out = fopen($outfile,"w");
		if(!isset($this->_out)) {
			trigger_error("Unable to open $outfile");
			return 1;
		}
		
	}
	function __destruct()
	{
		fclose($this->_in);
		fclose($this->_out);
	}
/*
interactions_data.tab

Contains interaction data incorporated into SGD from BioGRID (http://www.thebiogrid.org/).  Tab-separated columns are:

1) Feature Name (Bait) (Required)       	- The feature name of the gene used as the bait
2) Standard Gene Name (Bait) (Optional) 	- The standard gene name of the gene used as the bait
3) Feature Name (Hit) (Required)        	- The feature name of the gene that interacts with the bait
4) Standard Gene Name (Hit) (Optional)  	- The standard gene name of the gene that interacts with the bait
5) Experiment Type (Required)   		- A description of the experimental used to identify the interaction
6) Genetic or Physical Interaction (Required)   - Indicates whether the experimental method is a genetic or physical interaction
7) Source (Required)    			- Lists the database source for the interaction
8) Manually curated or High-throughput (Required)	- Lists whether the interaction was manually curated from a publication or added as part of a high-throughput dataset
9) Notes (Optional)     			- Free text field that contains additional information about the interaction
10) Phenotype (Optional)        		- Contains the phenotype of the interaction
11) Reference (Required)        		- Lists the identifiers for the reference as an SGDID (SGD_REF:) or a PubMed ID (PMID:)
12) Citation (Required) 			- Lists the citation for the reference
*/
	function Convert2RDF()
	{
		require ('../include.php');
//		$buf = N3NSHeader($nslist);

$buf = pronto_header();

		require ('../../lib/php/oboparser_lib.php');

		/** get the ontology terms **/
		$file = "/opt/data/obo/obo/apo.obo";
		$in = fopen($file, "r");
		if($in === FALSE) {
        		trigger_error("Unable to open $file");
        		exit;
		}
		$terms = OBOParser($in);
		fclose($in);
		BuildNamespaceSearchList($terms,$searchlist);

		$z = 0;
		while($l = fgets($this->_in,2048)) {
			list($id1,$id1name, $id2, $id2name, $method, $interaction_type, $src, $htpORman, $notes, $phenotype, $ref, $cit) = explode("\t",trim($l));;

			if($interaction_type != "physical interactions") continue;
			$tp = ($htpORman=="manually curated")?"LTP":"HTP";
			
/*
			$exp_type = array_search($interaction_type, $searchlist['experiment_type']);
			$buf .= "$sgd:$id a ".strtolower($exp_type)." .".PHP_EOL;
*/			
			$this->GetMethodID($method,$oid,$type);

			$id1 = str_replace(array("(",")"), array("",""), $id1);
			$id2 = str_replace(array("(",")"), array("",""), $id2);
			if($type == "protein") {$id1 = ucfirst(strtolower($id1))."p";$id2=ucfirst(strtolower($id2))."p";}
			
//			$buf .= "$sgd:$id $rdfs:label \"$htpORman ".substr($interaction_type,0,-1)." between $id1 and $id2 [$sgd:$id]\".".PHP_EOL;
$uri1 = "http://bio2rdf.org/sgd:$id1";
$uri2 = "http://bio2rdf.org/sgd:$id2";

			
$buf .= '
   <EquivalentClasses>
        <Class URI="&protein;'.$id1.'_'.$id2.'_'.$tp.'_interaction"/>
        <ObjectIntersectionOf>
            <Class URI="&protein;PutativeInteraction"/>
            <ObjectSomeValuesFrom>
                <ObjectProperty URI="&protein;isDetectedBy"/>
                <Class URI="&protein;'.$tp.'"/>
            </ObjectSomeValuesFrom>
            <ObjectExactCardinality cardinality="1">
                <ObjectProperty URI="&protein;hasParticipant"/>
                <Class URI="'.$uri1.'"/>
            </ObjectExactCardinality>
            <ObjectExactCardinality cardinality="1">
                <ObjectProperty URI="&protein;hasParticipant"/>
                <Class URI="'.$uri2.'"/>
            </ObjectExactCardinality>
        </ObjectIntersectionOf>
    </EquivalentClasses>
'.PHP_EOL;

/*			
			$eid = $id."exp";
			$buf .= "$sgd:$id $sgd:method $sgd:$eid .".PHP_EOL;
			$buf .= "$sgd:$eid a ".strtolower($oid)." .".PHP_EOL;
			
			if($phenotype) {
				$buf .= "$sgd:$id a ".strtolower($exp_type)." .".PHP_EOL;
				$p = explode(":",$phenotype);
				if(count($p) == 1) {
					// straight match to observable
					$observable = array_search($p[0], $searchlist['observable']);
				} else if(count($p) == 2) {
					// p[0] is the observable and p[1] is the qualifier
					$observable = array_search($p[0], $searchlist['observable']);
					$qualifier = array_search($p[1], $searchlist['qualifier']);
					$buf .= "$sgd:$id $sgd:qualifier ".strtolower($qualifier).".".PHP_EOL;
				}
				$buf .= "$sgd:$id $sgd:phenotype ".strtolower($observable).".".PHP_EOL;
			}

			$b = explode("|",$ref);
			foreach($b AS $c) {
				$d = explode(":",$c);
				if($d[0]=="PMID") $buf .= "$sgd:$id $sgd:article $pubmed:$d[1] .".PHP_EOL;
			}
*/			/*
			$buf .= "$sgd:$id1 $sgd:interactsWith $sgd:$id2 .".PHP_EOL;
			$buf .= "$sgd:$id2 $sgd:interactsWith $sgd:$id1 .".PHP_EOL;
			*/
		
			//if($z++ == 1000) {echo $buf;exit;}
		}
		$buf .= pronto_footer();
		fwrite($this->_out, $buf);
		
		return 0;
	}


	function GetMethodID($label, &$id, &$type) {
	$gi = array(
		'Dosage Rescue' => 'APO:0000173',
		'Dosage Lethality' => 'APO:0000172',
		'Dosage Growth Defect' => 'APO:0000171',
		'Epistatic MiniArray Profile' => 'APO:0000174',
		'Synthetic Lethality' => 'APO:0000183',
		'Synthetic Growth Defect' => 'APO:000018',
		'Synthetic Rescue' => 'APO:0000184',
		'Synthetic Haploinsufficiency'=> 'APO:0000272',
		'Phenotypic Enhancement' => 'APO:0000177',
		'Phenotypic Suppression' => 'APO:0000178'
	);
	$pi = array(
		'Affinity Capture-MS' => 'APO:0000162',
		'Affinity Capture-Western' => 'APO:0000165',
		'Affinity Capture-RNA' => 'APO:0000163',
		'Affinity Chromatography' => 'APO:0000188',
		'Affinity Precipitation' => 'APO:0000189',
		'Biochemical Activity' => 'APO:0000166',
		'Biochemical Assay' => 'APO:0000190',
		'Co-crystal Structure' => 'APO:0000167',
		'Co-fractionation' => 'APO:0000168',
		'Co-localization' => 'APO:0000169',
		'Co-purification' => 'APO:0000170',
		'Far Western' => 'APO:0000176',
		'FRET' => 'APO:0000175',
		'PCA' => 'APO:0000244',
		'Protein-peptide' => 'APO:0000180',
		'Protein-RNA' => 'APO:0000179',
		'Purified Complex' => 'APO:0000191',
		'Reconstituted Complex' => 'APO:0000181',
		'Two-hybrid' => 'APO:0000185',
	);
	if(isset($gi[$label])) {$id=$gi[$label];$type='gene';return;}
	if(isset($pi[$label])) {$id=$pi[$label];$type='protein';return;}
	echo "No match for $label\n";
	}
};

function pronto_header() {
return '
<?xml version="1.0"?>
<!DOCTYPE Ontology [
    <!ENTITY owl "http://www.w3.org/2002/07/owl#" >
    <!ENTITY xsd "http://www.w3.org/2001/XMLSchema#" >
    <!ENTITY owl2xml "http://www.w3.org/2006/12/owl2-xml#" >
    <!ENTITY rdfs "http://www.w3.org/2000/01/rdf-schema#" >
    <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#" >
    <!ENTITY protein "file:/C:/kl/java/pronto/examples/protein/protein.owl#" >
]>
<Ontology xmlns="http://www.w3.org/2006/12/owl2-xml#"
     xml:base="http://www.w3.org/2006/12/owl2-xml#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:owl2xml="http://www.w3.org/2006/12/owl2-xml#"
     xmlns:protein="&protein;"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     ontologyIRI="file:/C:/kl/java/pronto/examples/protein/protein.owl">
';

}

function pronto_footer() {
 return '
</Ontology>
';

}

?>
