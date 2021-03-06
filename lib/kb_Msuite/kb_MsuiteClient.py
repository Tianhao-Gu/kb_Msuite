# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_Msuite(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def run_checkM(self, params, context=None):
        """
        :param params: instance of type "CheckMInputParams" (Runs CheckM as a
           command line local function. subcommand - specify the subcommand
           to run; supported options are lineage_wf, tetra, bin_qa_plot,
           dist_plot bin_folder - folder with fasta files representing each
           contig (must end in .fna) out_folder - folder to store output
           plots_folder - folder to save plots to seq_file - the full
           concatenated FASTA file (must end in .fna) of all contigs in your
           bins, used just for running the tetra command tetra_File - specify
           the output/input tetra nucleotide frequency file (generated with
           the tetra command) dist_value - when running dist_plot, set this
           to a value between 0 and 100 thread -  number of threads
           reduced_tree - if set to 1, run checkM with the reduced_tree flag,
           which will keep memory limited to less than 16gb (otherwise needs
           40+ GB, which NJS worker nodes do have) quiet - pass the --quite
           parameter to checkM, but doesn't seem to work for all subcommands)
           -> structure: parameter "subcommand" of String, parameter
           "bin_folder" of String, parameter "out_folder" of String,
           parameter "plots_folder" of String, parameter "seq_file" of
           String, parameter "tetra_file" of String, parameter "dist_value"
           of Long, parameter "thread" of Long, parameter "reduced_tree" of
           type "boolean" (A boolean - 0 for false, 1 for true. @range (0,
           1)), parameter "quiet" of type "boolean" (A boolean - 0 for false,
           1 for true. @range (0, 1))
        """
        return self._client.call_method(
            'kb_Msuite.run_checkM',
            [params], self._service_ver, context)

    def run_checkM_lineage_wf(self, params, context=None):
        """
        :param params: instance of type "CheckMLineageWfParams" (input_ref -
           reference to the input Assembly, AssemblySet, Genome, GenomeSet,
           or BinnedContigs data) -> structure: parameter "input_ref" of
           String, parameter "workspace_name" of String, parameter
           "reduced_tree" of type "boolean" (A boolean - 0 for false, 1 for
           true. @range (0, 1)), parameter "save_output_dir" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1)),
           parameter "save_plots_dir" of type "boolean" (A boolean - 0 for
           false, 1 for true. @range (0, 1))
        :returns: instance of type "CheckMLineageWfResult" -> structure:
           parameter "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method(
            'kb_Msuite.run_checkM_lineage_wf',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_Msuite.status',
                                        [], self._service_ver, context)
