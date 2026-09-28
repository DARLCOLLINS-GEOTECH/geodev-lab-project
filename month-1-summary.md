# Month One Summary

## Project Overview

September 2026 marked my first month in the **GeoDev Lab GIS Development Workflow Programme**. Over the first four weeks, I progressed from defining a spatial question and sourcing data to documenting, cleaning, projecting, and analysing the datasets needed for the project.

My work during Month One followed a gradual workflow:

**Question Definition → Data Sourcing → Project Organisation → Data Quality Checks → Clipping → Reprojection → Analysis Operations**

---

# Week 1 – Defining the Question and Sourcing Data

---

The first week focused on defining a **specific, place-based and answerable spatial question**. After considering several possible project topics, I selected healthcare accessibility in AMAC because it could be answered using clearly defined spatial datasets and measurable geographic relationships.

## The Question

> **Which operational wards in Abuja Municipal Area Council (AMAC), FCT Abuja, have the greatest number of residents living more than 2 km from the nearest mapped healthcare facility?**

### Study Area

I selected my study area to be **Abuja Municipal Area Council (AMAC), Federal Capital Territory, Nigeria.** I then identified and sourced the datasets needed for the project.

---

## Main Project Datasets

| Dataset Needed | Source | Result |
|---|---|---|
| Operational Wards Boundary | GRID3 | Found, FCT is included |
| Health Facilities | GRID3 | Found, FCT dataset available |
| Population Estimates | Worldpop estimated gridded population | Found |
| Operational LGA Boundaries | GRID3 | Found, AMAC is included |
| Roads | OSM via Quick OSM | Available |

I also created the initial **project brief and README**, documenting:

- the project question;
- why the question matters;
- the study area;
- the datasets required;
- the sources of the datasets; and
- the type of final product I intend to build.

---

# Week 2 – Getting and describing the data, Folder Setup and Data Notes

---

I first created a structured project folder so that original datasets could remain unchanged while processed outputs is stored separately.

A simplified version of the project structure is:

```text
project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── README.md
└── project.qgz
```
I then downloaded the operational wards, LGA, health facility, and population datasets. For OSM, I used key = highway and value = tertiary.

I then prepared detailed data notes for the datasets.
The data notes documented information such as:
- dataset source;
- version;
- number of features;
- geometry type;
- coordinate reference system;
- important attributes;
- missing values;
- geometry quality;
- spatial coverage; and
- potential data-quality problems.
  
## Important Findings from the Data Notes

| Dataset	| Observation |
|---|---|
| Operational Wards v3.0 |	5,872 features with MultiPolygon geometry and EPSG:4326 |
| Health Facilities v3.0	|41,778 records, but only 35,774 have valid point geometry |
| Gridded Population |	Contains actual modelled 2025 population estimates per approximately 100 m grid cell |
| Operational LGA Boundaries |	Contains all 774 Nigerian LGAs and was useful for defining AMAC |
| OSM Roads	| Represents only tertiary-class roads and not the complete road network. The original layer contained 843 LineString features in EPSG:4326 |


One of the most important lessons from this week was that a dataset loading successfully does not automatically mean it is appropriate for the intended analysis.

---

# Week 3 – Data Quality Preparation (Clipping and Projections)

---

Week 3 focused on preparing the datasets for reliable spatial analysis.
The original datasets were mainly stored in:
EPSG:4326 – WGS 84

Because EPSG:4326 uses geographic coordinates measured in degrees, it is not appropriate for directly calculating distances such as 2 km or accurate areas in square kilometres.
I therefore prepared the datasets through clipping and reprojection.
