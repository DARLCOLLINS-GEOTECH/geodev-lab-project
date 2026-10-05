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
I first clipped all geographic datasets using the AMAC boundary. The cleaned and clipped datasets were reprojected to:
WGS 84 / UTM Zone 32N – EPSG:32632

This CRS uses metres, which makes it suitable for the distance and area calculations required by my project.
The resulting AMAC study area was approximately:
1,446.57 km²

By the end of Week 3, I had a consistent set of clipped and projected datasets ready for spatial analysis.

---

# Week 4 – Spatial Operations and Analysis

---

The final week of month one marked the beginning of the actual spatial analysis.
The key part of my research question is the phrase:
"living more than 2 km from the nearest mapped healthcare facility"

## **The Operation**

Buffered the health facilities by 2000m, dissolved into one shape, then found which wards have areas falling outside it using difference, and calculated their areas.

### **Why I Used a Buffer**

A buffer allows me to create an area extending a specified distance around each healthcare facility.
Since my project defines healthcare accessibility using a distance of 2 km, I created a:
2,000 metre buffer around each mapped healthcare facility.

---

### **What I wrote down as expectation statement**

---

I expect the 2 km buffer operation to produce buffer polygons around all mapped healthcare facilities in and around AMAC, but just one buffer feature as output because I set it to dissolve, representing the combined geographic area of AMAC within 2km of at least one mapped health facility.

---

## The Result

---

### **What I Got**

The buffer operation successfully produced 2 km accessibility zones around the healthcare facility points. I obtained a combined healthcare-accessibility layer in which overlapping buffers were merged. Then the difference operation produced polygons of all the AMAC areas outside the 2km buffer. These polygons now represent the geographic areas that will be investigated further to determine how many people live within them.

---
## Expected vs Actual Results

---

| Operation |	What I Expected |	What I Got |
|---|---|---|
| Buffer |	A dissolved 2 km polygon around healthcare facilities	| A single feature 2km accessibility zones around facility points |
| Difference |	Portions of AMAC outside the buffer	| Polygons representing areas more than 2 km from mapped facilities |
| Area Calculation	| Area of uncovered locations in km² |	Calculated area values for the uncovered polygons |

In summary, the operations behaved largely as expected and provided the spatial foundation required for answering the project question.

**What Surprised Me**

My biggest shock was the realisation that the healthcare facility dataset contained records without valid geometry. This reinforced the importance of examining dataset quality before beginning analysis.
I also observed how strongly the choice of coordinate reference system affects GIS operations. A buffer value of 2000 only represents 2,000 metres when the data is stored in an appropriate projected CRS. Performing the same operation in EPSG:4326 would incorrectly interpret the distance in degrees.

---
## The Four Checks 

---

I also carried out the four checks immediately after running each of my operations. 

- I looked at the map to confirm location accuracy
- Checked and counted the number of rows and features to make sure it tallied with my expected result.
- Since I had one dissolved feature, I checked it easily
- And then finally determined if there was a geometry


# Month 2: Python Development Foundations

## Week 5: Set Up Python, VS Code and Terminal — `hello.py` Runs

Week 5 marked the beginning of **Month 2**, with a focus on establishing the Python development environment needed for subsequent programming and development tasks.

### Major Tasks Completed

* Set up and verified **Python** through the terminal.
* Practised basic **terminal/PowerShell** commands, including checking the Python version and navigating directories.
* Created the required **development (`dev`) folder** and organised the project workspace.
* Created a **screenshots folder** to document the learning activities.
* Set up the project in **Visual Studio Code (VS Code)**.
* Installed and configured the **Python extension** in VS Code.
* Opened and verified the **integrated terminal** in VS Code.
* Created and executed a basic **`hello.py`** Python program.

### Result

I successfully established a functional Python development environment, with **Python, VS Code, and the terminal working together correctly**. The successful execution of `hello.py` confirmed that the environment was ready for the next stages of Python learning.

