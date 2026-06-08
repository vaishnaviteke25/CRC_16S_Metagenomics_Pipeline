#!/bin/bash

qiime tools import \
--type 'SampleData[PairedEndSequencesWithQuality]' \
--input-path manifest.tsv \
--output-path demux-paired.qza \
--input-format PairedEndFastqManifestPhred33V2
