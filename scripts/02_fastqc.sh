#!/bin/bash

fastqc *.fastq.gz

multiqc .
