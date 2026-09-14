# Data Notes

---

## 1. GRID3 Nigeria Operational Wards v3.0

- **Source:** GRID3 Data Hub https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v3-0/about 
- **Dataset version:** v3.0
- **Release:** July 2026
- **Downloaded:** 13 September 2026
- **Number of features/rows:** 5,872
- **Geometry type:** Polygon / MultiPolygon
- **Format:** Vector dataset

### Columns and Data Types

| Column | Type |
|---|---|
| `country` | String |
| `iso3` | String |
| `state` | String |
| `statecode` | String |
| `lga` | String |
| `lga_alt_names` | String |
| `ward` | String |
| `ward_alt_names` | String |
| `ward_v1_grid3` | String |
| `ward_in_grid3_ward_list` | Real/Float |
| `multipart_count` | Real/Float |
| `source` | String |
| `date` | String |
| `area_sqkm` | Real/Float |

### Null and Blank-Value Check

There are **no true NULL values** in the attribute fields. However, some text fields contain blank strings:

- `lga_alt_names`: **4,614 blank values**
- `ward_alt_names`: **2,533 blank values**
- `ward_v1_grid3`: **5,513 blank values**

### Coverage and completeness

The ward layer covers my study LGA fully, with no obvious spatial gaps
observed within the study area.

The dataset should, however, be treated as an operational rather than an
official legal boundary dataset. GRID3 notes that the v3.0 ward boundaries
have not yet been fully validated by all relevant government authorities.

---

## 2. GRID3 Nigeria Health Facilities v3.0

- **Source:** GRID3 Data Hub https://data.grid3.org/datasets/827e3638dc204f4b9ddbbd19b00954d6/about 
- **Dataset version:** v3.0
- **Release:** August 2026
- **Downloaded:** 13 September 2026
- **Number of features/rows:** 41,778
- **Geometry type:** Point
- **Format:** Vector dataset

### Columns and Data Types

| Column | Type |
|---|---|
| `unique_id` | String |
| `latitude` | Real/Float |
| `longitude` | Real/Float |
| `country` | String |
| `iso` | String |
| `state_standard` | String |
| `lga_standard` | String |
| `ward_standard` | String |
| `ward_bdry` | String |
| `ward_in_grid3_ward_list` | Real/Float |
| `facility_name` | String |
| `alt_name` | String |
| `settlement_name` | String |
| `facility_level` | String |
| `facility_type` | String |
| `facility_ownership` | String |
| `facility_ownership_type` | String |
| `functional` | String |
| `date_created` | String |
| `sett_ext_type` | String |
| `mgrs_code` | String |
| `input_data_record_ids` | String |
| `input_data_sources` | String |
| `nhfr_facility_code` | String |
| `gps_accuracy` | Real/Float |
| `sett_ext_dist_m` | Real/Float |
| `dist_ward_grid3_bdry_km` | Real/Float |
| `flag1` | Real/Float |
| `flag2` | Real/Float |
| `flag3` | Real/Float |
| `flag4` | Real/Float |
| `flag5` | Real/Float |
| `flag6` | Real/Float |
| `issues` | String |
| `flag_count` | Real/Float |

### Null values

Null values are expected in some optional attributes because information
such as ownership details, alternative administrative matching,
facility level, registry identifiers, or other facility information may
not be available for every record.

### Null and Blank-Value Check

Missing data occur as both true `NULL` values and blank strings.

| Field | Missing Values |
|---|---:|
| `latitude` | 6,004 NULL |
| `longitude` | 6,004 NULL |
| `ward_standard` | 15 blank |
| `ward_bdry` | 1,347 blank |
| `ward_in_grid3_ward_list` | 1,347 NULL |
| `alt_name` | 22,695 NULL + 5 blank |
| `settlement_name` | 40,039 blank |
| `facility_level` | 7,524 blank |
| `facility_type` | 3,031 blank |
| `facility_ownership` | 2,673 blank |
| `facility_ownership_type` | 11,584 blank |
| `functional` | 2,673 blank |
| `date_created` | 19,137 blank |
| `sett_ext_type` | 2,702 blank |
| `mgrs_code` | 2,702 blank |
| `nhfr_facility_code` | 37,715 blank |
| `gps_accuracy` | 19,256 NULL |
| `dist_ward_grid3_bdry_km` | 35,989 NULL |
| `flag1` | 41,756 NULL |
| `flag2` | 41,104 NULL |
| `flag3` | 37,618 NULL |
| `flag4` | 36,338 NULL |
| `flag5` | 36,916 NULL |
| `flag6` | 36,049 NULL |
| `issues` | 26,439 blank |

The following important fields are fully populated:

- `unique_id`
- `country`
- `iso`
- `state_standard`
- `lga_standard`
- `facility_name`
- `input_data_record_ids`
- `input_data_sources`
- `sett_ext_dist_m`
- `flag_count`

### Coverage and completeness

The health-facility points provide coverage for the study area and it can be used to examine the spatial distribution and accessibility of health services.
However, the dataset should not be interpreted as a guaranteed complete register of every existing health facility. GRID3 describes the health facility dataset as operational and non-exhaustive.

---

## 3. GRID3 Nigeria Gridded Population v3.0

- **Source:** GRID3 DATA HUB https://data.grid3.org/maps/6966d625aea0488496d01debd3bb80f9/about 
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

- **Raster width:** **14392**
- **Raster height:** **11532**
- **Number of bands:** **1**

### Columns/fields

A raster does not have ordinary vector attribute columns. Instead, each raster cell contains a population estimate.

The principal raster band represents estimated population counts for approximately 100 m grid cells.

### Data type

- **Raster data type:** **Float32**

### Coverage and completeness

The population surface provides nationwide coverage and therefore covers the study LGA.

No obvious geographic gaps should occur within the study area provided the correct Nigeria v3.0 raster has been loaded and clipped correctly.

The values are modelled population estimates rather than direct census counts and should therefore be interpreted as estimates.

---

## 4. GRID3 Nigeria Operational LGA Boundaries 

- **Source:** GRID3 Data Hub https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about 
- **Dataset:** GRID3 Nigeria Operational LGA Boundaries
- **Number of features/rows:** 774
- **Geometry type:** Polygon / MultiPolygon
- **Format:** Vector dataset
- **Geographic coverage:** Nigeria

### Columns and Data Types

| Column | Type |
|---|---|
| `globalid` | String |
| `uniq_id` | Integer32 |
| `timestamp` | DateTime |
| `editor` | String |
| `lganame` | String |
| `lgacode` | String |
| `statename` | String |
| `statecode` | String |
| `source` | String |
| `amapcode` | String |

### Null and Blank-Value Check

There are **no true NULL values** in the attribute fields.

Only one field contains blank values:

- `amapcode`: **10 blank values**

The important administrative fields are fully populated:

- `lganame`
- `lgacode`
- `statename`
- `statecode`

### Coverage and completeness

The layer contains the 774 Local Government Areas of Nigeria and provides
complete national LGA coverage. It therefore covers MY study LGA completely, with no obvious spatial
gap expected within the study area.

The boundaries are operational GIS boundaries and should not necessarily be interpreted as legally authoritative cadastral boundaries.

---

## 5. OpenStreetMap Roads Extracted with QuickOSM

- **Source:** OpenStreetMap contributors
- **Extraction tool:** QuickOSM plugin in QGIS
- **Extraction date:** 13 September 2026
- **Query key:** `highway`
- **Query values:** Tertiary
- **Dataset type:** Vector
- **Geometry type:** LineString / MultiLineString
- **Number of features/rows:** 843

### Columns

The layer contains the following fields:

- `full_id`
- `osm_id`
- `osm_type`
- `highway`
- `covered`
- `bridge:movable`
- `maxspeed:backward`
- `lane_markings`
- `maxspeed`
- `smoothness`
- `ford`
- `maxheight`
- `layer`
- `bridge`
- `junction`
- `old_name`
- `surface`
- `oneway`
- `name`
- `lanes`

### Column Types

All attribute columns are stored as **String/Text**.

### Null Values

Important missing values include:

| Field | NULL Values |
|---|---:|
| `name` | 689 |
| `surface` | 547 |
| `lanes` | 772 |
| `maxspeed` | 842 |
| `oneway` | 388 |
| `bridge` | 778 |

The `highway` field is fully populated.

### Coverage and completeness

The road extraction covers the selected study-area extent.

However, OpenStreetMap is a continuously updated volunteered geographic database. Road coverage and attribute completeness may therefore vary between locations.

A visual inspection was carried out against satellite imagery and another reference basemap to identify possible missing roads, incomplete connections, or incorrectly classified road segments.

---

# Overall Data Quality Summary

| Dataset | Main Type | Records / Cells | Geometry / Raster Type | Main Observation |
|---|---|---:|---|---|
| GRID3 Operational Wards v3.0 | Vector | 5,872 | MultiPolygon | Covers 24 states/FCT rather than all Nigeria |
| GRID3 Health Facilities v3.0 | Vector | 41,778 | Point | 6,004 records have no coordinates; covers 24 states/FCT |
| GRID3/WorldPop Population Master Grid | Raster | 11,532 × 14,392 | Approx. 100 m raster |covers Nigeria extent|
| GRID3 Operational LGA Boundaries | Vector | 774 | MultiPolygon | Complete nationwide LGA coverage |
| OSM Roads / QuickOSM | Vector | 843 raw features | LineString / MultiLineString |differing extents|

## Data Quality Summary

The five datasets represent different spatial data types and therefore required different quality checks:

- The Operational Wards and LGA datasets provide polygon administrative boundaries.
- The Health Facilities dataset contains point locations.
- The Population dataset is a gridded raster surface.
- The OpenStreetMap Roads dataset contains line features.
- Null values in optional descriptive fields do not necessarily indicate an error.
- Administrative boundary completeness was checked visually.
- Health facility and OpenStreetMap completeness was not assumed solely from the absence of visible gaps.
- Raster `NoData` values were distinguished from valid zero values.
- All datasets was checked for coordinate reference system, spatial extent, geometry validity and consistency before analysis.
