#include <KBaseCommon.spec>
/* A module containing specifications for various file types stored in Shock
    with references in the workspace.
*/
module KBaseFile {

    typedef int bool;
    
    /* An id for a shock node.
      @id shock
    */
    typedef string shock_id;
    
    /* A file stored in Shock.
      id - the id for the shock node
      type - the file type (e.g. XML, FASTA, GFF)
      size - the file size in bytes.
      md5 - the md5 digest of the file.
      sha1 - the sha1 digest of the file.
      
      @optional md5 sha1
    */
    typedef structure {
      shock_id id;
      string type;
      int size;
      string md5;
      string sha1;
    } ShockFile;
    
    /* A reference to a file stored in Shock.
      file - the location of and information about a file stored in Shock
      encoding - the encoding of the file (e.g. UTF8)
      name - the file name
      description - a description of the file

      @optional description
      @meta ws file.type
      @meta ws file.size
      @meta ws encoding
      @meta ws name
      @meta ws description
    */
    typedef structure {
      ShockFile file;
      string encoding;
      string name;
      string description;
    } FileRef;

    /* A library of paired end reads. If data is interleaved lib2 will be null
        or absent.
      lib1 - the left reads
      lib2 - the right reads
      strain - information about the genetic source
      source - information about the source of this data
      insert_size_mean - the mean size of the genetic fragments
      insert_size_std_dev - the standard deviation of the size of the genetic
        fragments
      interleaved - whether the left and right reads are interleaved in a
        single file
      read_orientation_outward - the orientation of the reads. If false or
        absent, the read directions face each other. Otherwise, the sequencing
        occurs in in an outward direction from the primer pairs.
      sequencing_tech - the technology used to sequence the genetic information
      read_count - the number of reads in the this dataset
      read_size - the total size of the reads, in bases
      gc_content - the GC content of the reads.
     
      @optional lib2
      @optional insert_size_mean insert_size_std_dev interleaved
      @optional read_orientation_outward gc_content source
      @meta ws strain.genus
      @meta ws strain.species
      @meta ws strain.strain
      @meta ws strain.ncbi_taxid
      @meta ws source.source
      @meta ws source.source_id
      @meta ws source.project_id
      @meta ws read_count
      @meta ws read_size
      @meta ws gc_content
      @meta ws sequencing_tech
    */
    typedef structure {
      ShockFile lib1;
      ShockFile lib2;
      KBaseCommon.StrainInfo strain;
      KBaseCommon.SourceInfo source;
    
      float insert_size_mean;
      float insert_size_std_dev;
      bool interleaved;
      bool read_orientation_outward;
     
      string sequencing_tech;
      int read_count;
      int read_size;
      float gc_content;
    } PairedEndLibrary;
    
    /*  A library of single end reads.
      lib - the reads
      strain - information about the genetic source
      source - information about the source of this data
      sequencing_tech - the technology used to sequence the genetic information
      read_count - the number of reads in the this dataset
      read_size - the total size of the reads, in bases
      gc_content - the GC content of the reads.
    
      @optional gc_content source
      @meta ws strain.genus
      @meta ws strain.species
      @meta ws strain.strain
      @meta ws strain.ncbi_taxid
      @meta ws source.source
      @meta ws source.source_id
      @meta ws source.project_id
      @meta ws read_count
      @meta ws read_size
      @meta ws gc_content
      @meta ws sequencing_tech
    */
    typedef structure {
      ShockFile lib;
      KBaseCommon.StrainInfo strain;
      KBaseCommon.SourceInfo source;

      string sequencing_tech;
      int read_count;
      int read_size;
      float gc_content;
    } SingleEndLibrary;
    
    /* A workspace id for a paired end library.
      @id ws KBaseFile.PairedEndLibrary
    */
    typedef string pairedlib_id;
    
    /* A workspace id for a single end library.
      @id ws KBaseFile.SingleEndLibrary
    */
    typedef string singlelib_id;
    
    /* An assembly of reads.
      Note it is *strongly* encouraged that the read libraries are included,
      but the fields are optional because for some data sources there is
      currently no way to map the assembly to the source reads.
    
      assembly_file - the assembly
      strain - information about the genetic source
      source - information about the source of this data
      size - the total size of the assembly, in bases
      gc_content - the GC content of the assembly
      contigs - the number of contigs in the assembly
      pairedlibs - references to the paired end libraries used to construct
          this assembly
      singlelibs - references to the single end libraries used to construct
          this assembly
    
      @optional gc_content source
      @optional pairedlibs singlelibs
      @meta ws strain.genus
      @meta ws strain.species
      @meta ws strain.strain
      @meta ws strain.ncbi_taxid
      @meta ws source.source
      @meta ws source.source_id
      @meta ws source.project_id
      @meta ws size
      @meta ws contigs
      @meta ws gc_content
    
      TODO: What assembly parameters can we store? Need JGI and the Assembly
          team’s help here.
    */
    typedef structure {
      ShockFile assembly_file;
      KBaseCommon.StrainInfo strain;
      KBaseCommon.SourceInfo source;
    
      int size;
      int gc_content;
      int contigs;
     
      list<pairedlib_id> pairedlibs;
      list<singlelib_id> singlelibs;
    } AssemblyFile;
    
    /* A workspace id for an assembly file.
      @id ws KBaseFile.AssemblyFile
    */
    typedef string assembly_id;
    
    /* A type for a DNA feature.
    
      CDS - A coding sequence of DNA, e.g. a protein encoding gene
      locus - a gene with potentially many mRNAs and CDSs
      mRNA - messenger RNA
      tRNA - transfer RNA
      sRNA - small RNA
      siRNA - small interfering RNA
      promoter - a promoter for a gene
      operon - an operon
      bind - a binding site
      pbind - a binding site for a protein
      operator - an operator site for a promoter
      atten - an attenuator
      term - a terminator
      CRISPR - a CRISPR
      pseudo - a pseudogene
      proph - a prophage
      ribosw - a riboswitch
      transp - a transposon
      pathis - a pathogenicity island
    */
    typedef string dna_feature_type;
    
    /* A file containing annotation data.
      Note it is *strongly* recommended to include the assembly id, but the
      field is optional since for some data sources the mapping is not
      maintained.
    
      annotation_file - the annotation file
      strain - information about the genetic source
      source - information about the source of this data
      features_by_type - the count of features by the type of the feature
      assembly_id - a reference to the assembly used to construct this annotation.
    
      @optional source
      @optional assembly
      @optional features_by_type
      @meta ws strain.genus
      @meta ws strain.species
      @meta ws strain.strain
      @meta ws strain.ncbi_taxid
      @meta ws source.source
      @meta ws source.source_id
      @meta ws source.project_id
    */
    typedef structure {
      ShockFile annotation_file;
      KBaseCommon.StrainInfo strain;
      KBaseCommon.SourceInfo source;
    
      mapping<dna_feature_type, int> features_by_type;
    
      assembly_id assembly;
    } AnnotationFile;
};

