import inspect
from Bio import Entrez
from Bio import Medline
from Bio import SeqIO
from Bio.Seq import Seq
import Bio
import pandas as pd
import re
from time import sleep
from rich.console import Console

# <---------- Entrez Access --------->
Entrez.api_key = ''
Entrez.email = ''

def gene_info(gene_name):
    gene_search = Entrez.esearch(db="gene", term=gene_name)
    gene_record = Entrez.read(gene_search)
    gene_id = gene_record["IdList"][0]
    gene_info = Entrez.efetch(db="gene", id=gene_id, rttype='fasta', retmode='text')
    return gene_info.read()

def gene_id(gene_id):
    gene_info = Entrez.efetch(db="gene", id=gene_id, rttype='fasta', retmode='text')
    return gene_info.read()
