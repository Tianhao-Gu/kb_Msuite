/*
A KBase module: kb_Msuite
This SDK module is developed to wrap the open source package CheckM which consists of a set of tools 
for assessing the quality of genomes recovered from isolates, single cells, or metagenomes. 
CheckM consists of a series of commands in order to support a number of different analyses and workflows.

References: 
CheckM in github: http://ecogenomics.github.io/CheckM/
CheckM docs: https://github.com/Ecogenomics/CheckM/wiki

Parks DH, Imelfort M, Skennerton CT, Hugenholtz P, Tyson GW. 2015. CheckM: assessing the quality of microbial genomes recovered from isolates, single cells, and metagenomes. Genome Research, 25: 1043–1055.
*/

module kb_Msuite {
    /*
    A boolean - 0 for false, 1 for true.
        @range (0, 1)
    */
    typedef int boolean;

    typedef string FASTA_format; /*".fna"*/

    /*  
        required params:
        putative_genomes_folder: folder path that holds all putative genome files with (fa as the file extension) to be checkM-ed
        checkM_workflow_name: name of the CheckM workflow,e.g., lineage_wf or taxonomy_wf
        file_extension: the extension of the putative genome file, should be "fna"
        workspace_name: the name of the workspace it gets saved to.

        optional params:
        thread: number of threads; default 1
        external_genes: indicating an external gene call instead of using prodigal, default 0
        external_genes_file: the file containing genes for gene call, default "" 

        markerset: choose between 107 marker genes by default or 40 marker genes
        min_contig_length: minimum contig length; default 1000
        plotmarker: specify this option if you want to plot the markers in each contig

        ref: https://github.com/Ecogenomics/CheckM/wiki/Installation#how-to-install-checkm
    */
    typedef structure {
        string workspace_name;
        string putative_genomes_folder;
        string checkM_workflow_name;
        string file_extension;

        int thread;
        boolean external_genes;
        string external_genes_file;
        int markerset;
        int min_contig_length;
        boolean plotmarker;
    } CheckMInputParams;

    /*
        checkM_results_folder: folder path that stores the CheckM results
        report_name: report name generated by KBaseReport
        report_ref: report reference generated by KBaseReport
    */
    typedef structure{
        string checkM_results_folder;
        string report_name;
        string report_ref;
    } CheckMResults;

    funcdef run_checkM(CheckMInputParams params)
        returns (CheckMResults returnVal) authentication required;
};
