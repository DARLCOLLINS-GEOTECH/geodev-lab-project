# Data Notes

---

## 1. GRID3 Nigeria Operational Wards v3.0

- **Source:** GRID3 Data Hub
- **Dataset version:** v3.0
- **Release:** July 2026
- **Downloaded:** 13 September 2026
- **Number of features/rows:** 5,872
- **Geometry type:** Polygon / MultiPolygon
- **Format:** Vector dataset

### Columns

The layer contains the following fields:

- `OBJECTID`
- `country`
- `iso3`
- `state`
- `statecode`
- `lga`
- `lga_alt_names`
- `ward`
- `ward_alt_names`
- `ward_v1_grid3`
- `rd_in_grid3_ward`
- `multipart_count`
- `source`
- `date`
- `area_sqkm`

### Column types

- `OBJECTID` — Integer64
- `multipart_count` — Real
- `area_sqkm` — Real
- Remaining fields — String/Text

### Null values

No null values were observed in the following important fields:

- `OBJECTID`
- `country`
- `state`
- `lga`
- `ward`
- `area_sqkm`

Some of the alternative-name or supporting metadata fields may contain
blank/null values where an alternative name or corresponding value does
not exist.

### Coverage and completeness

The ward layer covers the study LGA fully, with no obvious spatial gaps
observed within the study area.

The dataset should, however, be treated as an operational rather than an
official legal boundary dataset. GRID3 notes that the v3.0 ward boundaries
have not yet been fully validated by all relevant government authorities.

---

## 2. GRID3 Nigeria Health Facilities v3.0

- **Source:** GRID3 Data Hub
- **Dataset version:** v3.0
- **Release:** August 2026
- **Downloaded:** 13 September 2026
- **Geometry type:** Point
- **Format:** Vector dataset
- **Number of features/rows:** **[ENTER FEATURE COUNT FROM QGIS]**

### Columns

The GRID3 health-facility dataset uses a standardized health-facility
attribute structure. Important fields include:

- `OBJECTID`
- `globalid`
- `nhfr_uid`
- `nhfr_facility_code`
- `country`
- `iso`
- `state`
- `lga`
- `lga_name_disagreement`
- `ward`
- `ward_name_disagreement`
- `facility_name`
- `facility_name_source`
- `ownership`
- `ownership_type`
- `facility_level`
- `facility_level_option`
- `latitude`
- `longitude`
- `geocoordinates_source`
- `last_updated`

**Note:** The exact v3.0 field list should be copied from  
`Layer Properties → Fields` because v3.0 contains updates to the health
facility dataset and may include additional quality-control or spatial
matching fields.

### Column types

The principal field types are:

- `OBJECTID` — Integer / Integer64
- `nhfr_uid` — Integer
- `lga_name_disagreement` — Integer / Boolean-type indicator
- `ward_name_disagreement` — Integer / Boolean-type indicator
- `latitude` — Real/Double
- `longitude` — Real/Double
- Most descriptive fields such as facility name, state, LGA, ward,
  ownership and facility level — String/Text

### Null values

Null values are expected in some optional attributes because information
such as ownership details, alternative administrative matching,
facility level, registry identifiers, or other facility information may
not be available for every record.

The following fields should be specifically checked in QGIS for nulls:

- `facility_name`
- `state`
- `lga`
- `ward`
- `latitude`
- `longitude`
- `nhfr_facility_code`
- `ownership`
- `facility_level`

**Recorded null result:** **[ENTER YOUR QGIS NULL CHECK RESULT HERE]**

### Coverage and completeness

The health-facility points provide coverage for the study area and can be
used to examine the spatial distribution and accessibility of health
services.

However, the dataset should not be interpreted as a guaranteed complete
register of every existing health facility. GRID3 describes the health
facility dataset as operational and non-exhaustive.

The v3.0 release currently covers 24 Nigerian states, including the
Federal Capital Territory, rather than all 36 states plus the FCT.

---

## 3. GRID3 Nigeria Gridded Population v3.0

- **Source:** GRID3 / WorldPop
- **Dataset version:** v3.0
- **Release:** August 2025
- **Downloaded:** 13 September 2026
- **Dataset type:** Raster
- **Format:** GeoTIFF
- **Spatial resolution:** Approximately 100 m × 100 m
- **Coverage:** Nigeria
- **Geometry:** Raster grid cells/pixels rather than vector geometry

### Rows and columns

Because this is a raster dataset, "rows" do not refer to individual
vector features.

The appropriate values to record are the raster dimensions:

- **Raster columns/width:** **[ENTER VALUE FROM QGIS]**
- **Raster rows/height:** **[ENTER VALUE FROM QGIS]**
- **Number of bands:** **[ENTER VALUE FROM QGIS]**

These values can be found under:

`Layer Properties → Information`

### Columns/fields

A raster does not have ordinary vector attribute columns such as
`state`, `lga`, or `ward`.

Instead, each raster cell contains a population estimate.

The principal raster band represents estimated population counts for
approximately 100 m grid cells.

### Data type

- **Raster data type:** **[ENTER EXACT QGIS DATA TYPE, e.g. Float32]**
- Pixel values represent estimated population counts.

### Null / NoData values

The raster may contain `NoData` cells outside the valid population
surface or national/study-area extent.

`NoData` should not automatically be interpreted as zero population.
A value of `0` and a `NoData` value have different meanings and should
be treated separately during analysis.

### Coverage and completeness

The population surface provides nationwide coverage and therefore
covers the study LGA.

No obvious geographic gaps should occur within the study area provided
the correct Nigeria v3.0 raster has been loaded and clipped correctly.

The values are modelled population estimates rather than direct census
counts and should therefore be interpreted as estimates.

---

## 4. GRID3 Nigeria Operational LGA Boundaries

- **Source:** GRID3 Data Hub
- **Dataset:** GRID3 Nigeria Operational LGA Boundaries
- **Number of features/rows:** 774
- **Geometry type:** Polygon / MultiPolygon
- **Format:** Vector dataset
- **Geographic coverage:** Nigeria

### Version/date note

The local project copy has been identified as a September 2025 layer/copy.

However, the official GRID3 catalogue currently identifies the nationwide
Operational LGA Boundaries product as the December 2020 product, which was
released in March 2021.

Therefore, September 2025 should only be recorded as the dataset version
date if this is explicitly stated in the metadata of the downloaded file.
Otherwise, it should be recorded as the local download/update date.

### Columns

The operational LGA boundary dataset contains the following principal
fields:

- `OBJECTID`
- `globalid`
- `uniq_id`
- `timestamp`
- `editor`
- `lganame`
- `lgacode`
- `statename`
- `statecode`
- `source`
- `amapcode`
- `Shape__Area`
- `Shape__Length`

Depending on the downloaded file format, QGIS may display minor naming
differences for the geometry-derived area and length fields.

### Column types

- `OBJECTID` — Integer / Object ID
- `globalid` — String/Text
- `uniq_id` — Integer
- `timestamp` — Date/DateTime
- `editor` — String/Text
- `lganame` — String/Text
- `lgacode` — String/Text
- `statename` — String/Text
- `statecode` — String/Text
- `source` — String/Text
- `amapcode` — String/Text
- `Shape__Area` — Real/Double
- `Shape__Length` — Real/Double

### Null values

The key administrative fields that should be checked for null values are:

- `lganame`
- `lgacode`
- `statename`
- `statecode`

Supporting fields such as editor, timestamp, source or other metadata
fields may permit null values.

**Recorded null result:** **[ENTER YOUR QGIS NULL CHECK RESULT HERE]**

### Coverage and completeness

The layer contains the 774 Local Government Areas of Nigeria and provides
complete national LGA coverage.

It therefore covers the study LGA completely, with no obvious spatial
gap expected within the study area.

The boundaries are operational GIS boundaries and should not necessarily
be interpreted as legally authoritative cadastral boundaries.

---

## 5. OpenStreetMap Roads Extracted with QuickOSM

- **Source:** OpenStreetMap contributors
- **Extraction tool:** QuickOSM plugin in QGIS
- **Extraction date:** 13 September 2026
- **Query key:** `highway`
- **Query values:** All relevant highway/road classes
- **Dataset type:** Vector
- **Geometry type:** LineString / MultiLineString
- **Number of features/rows:** **[ENTER FEATURE COUNT FROM QGIS]**

### Columns

The exact columns returned by QuickOSM depend on the OpenStreetMap tags
available for the features in the selected study area.

Common road attributes include:

- `osm_id`
- `osm_type`
- `name`
- `highway`
- `surface`
- `lanes`
- `maxspeed`
- `oneway`
- `bridge`
- `tunnel`
- `access`
- `service`

Additional OSM tag fields may also occur.

**Exact fields in downloaded layer:**  
**[COPY THE FIELD NAMES FROM `Layer Properties → Fields`]**

### Column types

Most OpenStreetMap descriptive attributes are stored as String/Text
because OSM tags are primarily key-value text pairs.

Typical types include:

- `osm_id` — Integer64 or String, depending on the QuickOSM output
- `osm_type` — String
- `name` — String
- `highway` — String
- `surface` — String
- `lanes` — String or Integer depending on output
- `maxspeed` — String
- `oneway` — String
- Other OSM tags — generally String/Text

### Null values

Null values are common and expected in OpenStreetMap road data.

For example, many roads may have a `highway` classification but may not
have information for:

- `name`
- `surface`
- `lanes`
- `maxspeed`
- `oneway`
- `bridge`
- `access`

The `highway` attribute should normally be populated for features returned
through a `highway` query.

**Recorded null result:** **[ENTER YOUR QGIS NULL CHECK RESULT HERE]**

### Coverage and completeness

The road extraction covers the selected study-area extent.

However, OpenStreetMap is a continuously updated volunteered geographic
database. Road coverage and attribute completeness may therefore vary
between locations.

A visual inspection should be carried out against satellite imagery or
another reference basemap to identify possible missing roads, incomplete
connections, or incorrectly classified road segments.

The date of extraction is important because OpenStreetMap data may change
after the dataset has been downloaded.

---

## Data Quality Summary

The five datasets represent different spatial data types and therefore
require different quality checks:

- The Operational Wards and LGA datasets provide polygon administrative
  boundaries.
- The Health Facilities dataset contains point locations.
- The Population dataset is a gridded raster surface.
- The OpenStreetMap Roads dataset contains line features.
- Null values in optional descriptive fields do not necessarily indicate
  an error.
- Administrative boundary completeness should be checked visually.
- Health facility and OpenStreetMap completeness should not be assumed
  solely from the absence of visible gaps.
- Raster `NoData` values should be distinguished from valid zero values.
- All datasets should be checked for coordinate reference system,
  spatial extent, geometry validity and consistency before analysis.
