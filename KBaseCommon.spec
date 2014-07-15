/* Common types that may be reused in multiple other modules.
*/
module KBaseCommon {
    
    typedef int bool;
    
    /* An id for a shock node.
      @id shock
    */
    typedef string shock_id;
    
    /* An ID used for a piece of data at its source.
      @id external
    */
    typedef string source_id;
    
    /* An ID used for a project encompassing a piece of data at its source.
      @id external
    */
    typedef string project_id;
    
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
    
    /* Information about the source of a piece of data.
      source - the name of the source (e.g. NCBI, JGI, Swiss-Prot)
      source_id - the ID of the data at the source
      project_id - the ID of a project encompassing the data at the source
      
      @optional source source_id project_id
    */
    typedef structure {
      string source;
      source_id source_id;
      project_id project_id;
    } SourceInfo;
    
    /* Information about a location.
      lat - latitude of the site, recorded as a decimal number. North latitudes
          are positive values and south latitudes are negative numbers.
      lon - longitude of the site, recorded as a decimal number. West
          longitudes are positive values and east longitudes are negative
          numbers.
      elevation - elevation of the site, expressed in meters above sea level.
          Negative values are allowed.
      date - date of an event at this location (for example, sample
          collection), expressed in the format YYYY-MM-DDThh:mm:ss.SSSZ
      description - a free text description of the location and, if applicable,
          the associated event.
    
      @optional date description
    */
    typedef structure {
      int lat;
      int lon;
      int elevation;
      string date;
      string description;
    } Location;

    /* Information about a strain.
      genetic_code - the genetic code of the strain.
          See http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?mode=c
      genus - the genus of the strain
      species - the species of the strain
      strain - the identifier for the strain
      source - information about the source of the strain
      organelle - the organelle of interest for the related data (e.g.
          mitochondria)
      ncbi_taxid - the NCBI taxonomy ID of the strain
      location - the location from which the strain was collected
      
      @optional genetic_code source ncbi_taxid organelle location
    */
    typedef structure {
      int genetic_code;
      string genus;
      string species;
      string strain;
      string organelle
      SourceInfo source;
      int ncbi_taxid;
      Location location;
    } StrainInfo;
};
