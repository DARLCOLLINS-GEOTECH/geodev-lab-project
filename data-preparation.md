# Data Quality Notes

The following quality assessment evaluates each dataset against the project question:

**Which operational wards in Abuja Municipal Area Council (AMAC), FCT Abuja, have the greatest number of residents living more than 2 km from the nearest mapped healthcare facility?**

The five quality criteria considered are:

- **Completeness:** Is everything present that should be?
- **Currency:** How recent is the dataset?
- **Positional Accuracy:** Are features located in the correct places?
- **Attribute Accuracy:** Are the names, classifications and other attributes reliable?
- **Fitness for Purpose:** Is the dataset suitable for answering the project question?

---

## GRID3 Nigeria Operational Wards v3.0 — AMAC, FCT Abuja

- Source: GRID3 Nigeria Operational Wards v3.0.
- The complete source layer contains **5,872 ward polygons**, of which **12 wards belong to Municipal Area Council (AMAC)**.
- Geometry type: MultiPolygon.
- CRS: EPSG:4326 — WGS 84.
- Dataset `date` field: **30 June 2026**.
- **COMPLETENESS:** All 12 AMAC operational wards are present and all have valid geometries. The national v3.0 dataset covers only 24 states/FCT, but this does not affect this project because AMAC, FCT Abuja is included.
- **CURRENCY:** Good for this project. All ward records carry a date of **2026-06-30**, making the ward layer considerably more recent than the older LGA boundary dataset used in the project.
- **POSITIONAL ACCURACY:** No null, empty or invalid ward geometries were found. Comparison with the older AMAC LGA boundary shows some boundary differences; the combined v3.0 AMAC wards overlap approximately **96.3% of the older AMAC LGA polygon**. This should be treated mainly as a difference between boundary versions rather than assuming the newer ward data are incorrect.
- **ATTRIBUTE ACCURACY:** Important attributes such as `state`, `lga`, `ward`, `source`, `date`, and `area_sqkm` are fully populated. Blank values mainly occur in optional alternative-name fields such as `lga_alt_names`, `ward_alt_names`, and `ward_v1_grid3`.
- **FITNESS FOR PURPOSE:** **Suitable.** This is the main geographic layer required for summarising population accessibility results by ward. The v3.0 ward boundaries should be used as the final ward geography when assigning and reporting underserved population in AMAC.

---

## GRID3 Nigeria Health Facilities v3.0 — AMAC, FCT Abuja

- Source: GRID3 Nigeria Health Facilities v3.0.
- The complete source layer contains **41,778 health-facility records**.
- **519 records are labelled as belonging to Municipal Area Council (AMAC)**.
- Of the 519 AMAC-labelled records, only **254 have point geometry**, while **265 have no latitude, longitude or geometry**.
- A spatial check identified **262 mapped health-facility points physically located inside the AMAC boundary**.
- Geometry type: Point.
- CRS: EPSG:4326 — WGS 84.
- **COMPLETENESS:** This is an important limitation. Although 519 records are attributed to AMAC, **265 AMAC-labelled records cannot be mapped because they have no coordinates**. Therefore, the mapped health-facility layer is not spatially complete and may omit facilities that actually exist.
- **CURRENCY:** The dataset is GRID3 version 3.0 and is suitable as a recent project source. However, the `date_created` field is not populated for every AMAC record and should not be interpreted as the date on which every facility was last physically verified.
- **POSITIONAL ACCURACY:** Of the geocoded facilities, **253 AMAC-labelled points fall inside the AMAC boundary, and 1 AMAC-labelled point falls outside it**. In addition, **9 mapped facilities physically inside AMAC carry another LGA label**. Facility locations should therefore preferably be selected spatially using the AMAC polygon rather than relying only on the `lga_standard` field. The exact building-level positional accuracy has not yet been independently verified against satellite imagery.
- **ATTRIBUTE ACCURACY:** `facility_name`, `state_standard`, and `lga_standard` are populated, but some important descriptive fields are incomplete within the 519 AMAC-labelled records. `facility_level` is blank for **203 records**, `facility_type` for **45**, `facility_ownership` for **16**, `functional` for **16**, and `nhfr_facility_code` for **387**.
- **FITNESS FOR PURPOSE:** **Usable with an important limitation.** The mapped facilities can be used to calculate distance to the nearest **mapped** health facility, which matches the wording of the project question. However, the 265 AMAC-labelled facilities without coordinates could cause accessibility gaps to appear larger than they really are if some of those facilities are operational and located within underserved areas. This limitation must be stated in the final analysis.

---

## GRID3 / WorldPop Nigeria Gridded Population v3.0 — AMAC, FCT Abuja

- Source: GRID3 / WorldPop.
- Dataset: `NGA_population_v3_0_gridded.tif`.
- Population estimate year: **2025**.
- Version: **v3.0**.
- Data type: Raster / GeoTIFF.
- Raster size: **14,392 columns × 11,532 rows**.
- Number of bands: **1**.
- Pixel data type: **Float32**.
- Spatial resolution: approximately **100 m × 100 m**.
- CRS: **EPSG:4326 — WGS 84**.
- Valid population cells: **7,184,901**.
- Raster values range from approximately **0.67 to 1,204.35 persons per populated grid cell**.
- The sum of all valid grid-cell values is approximately **237.53 million people for Nigeria**.

- **COMPLETENESS:** The raster provides nationwide coverage and therefore completely covers AMAC, FCT Abuja. Population estimates are provided for grid cells identified as settled. NoData cells inside Nigeria represent areas classified as unsettled using building-footprint information, while NoData cells outside the national boundary represent areas outside Nigeria. The raster is therefore spatially complete for the intended model rather than having random missing population cells.

- **CURRENCY:** The dataset represents **2025 modelled population estimates** and version 3.0 was released in **August 2025**. It is sufficiently recent for the current project, although it represents an estimated 2025 population surface rather than live or continuously updated population counts.

- **POSITIONAL ACCURACY:** Population is distributed across approximately **100 m grid cells**, providing much finer spatial detail than ward- or LGA-level population totals. However, each cell represents a modelled estimate of the population within that area and should not be interpreted as the exact location of individual households or residents. The approximately 100 m resolution is appropriate for identifying broad spatial patterns of population in relation to health facilities.

- **ATTRIBUTE ACCURACY:** Each valid raster cell contains an **estimated population count**, not a binary settled/unsettled value. Values can contain decimals or fractions of a person because the population surface is statistically modelled. These fractional values are expected and should be summed across multiple cells rather than rounded individually. The dataset contains only positive population estimates in valid cells, ranging from approximately 0.67 to 1,204.35 persons per cell.

- **FITNESS FOR PURPOSE:** **Suitable for the project.** Unlike the previously uploaded master-grid raster, this dataset contains actual estimated population counts and can therefore be used to estimate how many residents live more than 2 km from the nearest mapped healthcare facility. The appropriate workflow is to identify population cells outside the 2 km health-facility coverage areas, sum their population values, and aggregate the results by GRID3 operational ward. This directly supports the project question of identifying which AMAC wards have the greatest number of residents living more than 2 km from a mapped healthcare facility.

### Important Interpretation Note

This dataset contains **modelled population estimates rather than census counts for individual grid cells**. Therefore, final results should be described as estimated numbers of residents rather than exact population counts.

For example, the final analysis should use wording such as:

> "Estimated number of residents living more than 2 km from the nearest mapped healthcare facility."

rather than:

> "Exact number of residents living more than 2 km from a healthcare facility."
---

## GRID3 Nigeria Operational LGA Boundaries — AMAC, FCT Abuja

- Source: GRID3 Nigeria Operational LGA Boundaries.
- The source layer contains **774 LGA polygons**, representing the 774 Local Government Areas of Nigeria.
- Municipal Area Council (AMAC) is present in the dataset.
- Geometry type: MultiPolygon.
- CRS: EPSG:4326 — WGS 84.
- Internal timestamps range from **August 2019 to August 2020**.
- **COMPLETENESS:** Complete for the purpose of identifying AMAC. All 774 Nigerian LGAs are represented, and the AMAC polygon has valid geometry.
- **CURRENCY:** This is the oldest major boundary dataset being used in the project. Its internal records date mainly from 2019–2020, while the operational ward dataset is dated 2026. Therefore, differences between the LGA boundary and newer ward boundaries should be expected.
- **POSITIONAL ACCURACY:** The AMAC geometry is valid, but it does not align perfectly with the newer GRID3 v3.0 ward boundaries. The combined AMAC ward polygons overlap approximately **96.3% of the older AMAC LGA polygon**, showing that the two boundary products should not be assumed to be identical.
- **ATTRIBUTE ACCURACY:** Important administrative fields such as `lganame`, `lgacode`, `statename`, and `statecode` are fully populated. There are no true NULL values in these key fields. Only the optional `amapcode` field contains blank values for 10 records nationally.
- **FITNESS FOR PURPOSE:** **Suitable as a study-area boundary and selection layer.** It can be used to identify and extract AMAC from national datasets. However, because the operational wards are newer, the ward v3.0 boundaries should take priority for the final ward-level analysis where the two datasets differ.

---

## OpenStreetMap Tertiary Roads — AMAC, FCT Abuja

- Source: OpenStreetMap contributors.
- Extracted through QuickOSM using:

  `key = highway`  
  `value = tertiary`

- The supplied extract contains **843 tertiary-road features**.
- **554 of the extracted tertiary-road features intersect AMAC**.
- Geometry type: LineString.
- CRS: EPSG:4326 — WGS 84.
- All 843 features have `highway = tertiary`.
- **COMPLETENESS:** The dataset is deliberately incomplete as a representation of the entire road network because only roads tagged `highway=tertiary` were extracted. Primary, secondary, residential, service, unclassified and other roads that people may use to reach health facilities are not included.
- **CURRENCY:** OpenStreetMap is continuously edited, so this dataset represents the condition of OSM at the time it was extracted in **September 2026**. Future OSM edits will not automatically appear in the saved GeoPackage.
- **POSITIONAL ACCURACY:** All 843 road features have valid line geometry and the AMAC roads fall within the expected FCT geographic area. However, their exact alignment with real roads has not yet been independently verified against satellite imagery. A visual satellite-imagery check should therefore be completed before using the roads for detailed routing.
- **ATTRIBUTE ACCURACY:** The main `highway` attribute is consistent because every feature is classified as `tertiary`. However, many optional road attributes are incomplete. Among the **554 tertiary-road features intersecting AMAC**, approximately:
  - **25.6%** have a road `name`;
  - **20.4%** have a `surface` value;
  - **12.3%** have a `lanes` value;
  - **0%** have a `maxspeed` value; and
  - **70.2%** have an `oneway` value.

  This means the layer cannot reliably answer questions about road surface, lane count or travel speed.
- **FITNESS FOR PURPOSE:** **Suitable mainly as supporting map context, but not as a complete accessibility network.** For a straight-line 2 km health-facility accessibility analysis, the tertiary-road layer is not required to calculate the 2 km distance and can instead provide useful geographic context on the final map. If the project later changes to **road-network or travel-distance accessibility**, `highway=tertiary` alone would not be sufficient because many roads used by residents to reach health facilities are excluded.

---

## Overall Quality Assessment

| Dataset | Completeness | Currency | Positional / Spatial Quality | Fitness for This Project |
|---|---|---|---|---|
| GRID3 Operational Wards v3.0 | Good for AMAC | Very recent | Valid geometry; minor mismatch with older LGA boundary | **Suitable** |
| GRID3 Health Facilities v3.0 | Limited by missing coordinates | Recent source, but individual verification dates vary | 265 AMAC-labelled records cannot be mapped | **Usable with limitation** |
| Population Master Grid | Complete spatial coverage | Current project version | Approx. 100 m grid | **Not suitable for population counts; replace with gridded population raster** |
| GRID3 LGA Boundaries | Complete | Older, mainly 2019–2020 | Valid geometry but differs from newer ward boundary | **Suitable for defining/selecting AMAC** |
| OSM Tertiary Roads | Incomplete as a full road network | September 2026 extraction | Valid geometry; satellite verification still required | **Suitable as map context; not sufficient for network-access analysis** |

---

