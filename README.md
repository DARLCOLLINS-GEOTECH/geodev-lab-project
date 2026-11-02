

# GeoDev Lab Africa Project

## AMAC Healthcare Accessibility Analysis

> **Project Question:**  
> Which operational wards in Abuja Municipal Area Council (AMAC), FCT Abuja, have the greatest number of residents living more than 2 km from the nearest mapped healthcare facility?

This repository documents my **12-month GeoDev Lab Africa GIS Development Workflow Project**. The project is structured as one continuous learning and development journey, where each weekly task builds on the previous task and contributes to the overall healthcare accessibility analysis. 

See [project-brief.md](project-brief.md) for the full brief.

The project progresses from:

**Spatial Problem Definition → Data Sourcing → Data Organisation → Data Preparation → Spatial Analysis → Python Development → Advanced Geospatial Development**

---

# Project Progress

| Month | Week | Focus | Result |
|---|---|---|---|
| **Month 1** | **Week 1** | Define the spatial question and source datasets | Project question, study area and required datasets established |
| **Month 1** | **Week 2** | Get, organise and describe the data | Datasets acquired, organised and documented |
| **Month 1** | **Week 3** | Prepare data through clipping and reprojection | AMAC datasets prepared for spatial analysis |
| **Month 1** | **Week 4** | Perform spatial operations and analysis | 2 km healthcare accessibility zones and uncovered areas produced |
| **Month 2** | **Week 5** | Set up Python, VS Code and terminal | Python development environment established and `hello.py` successfully executed |
| **Month 2** | **Week 6** | Set up the project with `uv`, installed Pandas, and verified its version using `check.py` | Pandas and Python packages successfully installed and active |
| **Month 2** | **Week 7** | Python Fundamentals and Error Handling | Successfully applied Python fundamentals to read, process and classify ward data while developing practical error-diagnosis and debugging skills |
| **Month 2** | **Week 8** | Inspecting and Summarising AMAC Wards Data with Python | Successfully inspected and summarised AMAC operational wards' area data using Python, connecting the earlier QGIS spatial analysis workflow with programmatic data analysis |
| **Month 2** | **Week 9** | 

---

# Month 1 — GIS Project Foundation

**Month 1** covered **Weeks 1–4** and established the GIS foundation of the project.

During this month, I moved from defining the healthcare accessibility problem to sourcing, organising, preparing and analysing the spatial datasets required to investigate the problem.

## Week 1 — Defining the Question and Sourcing Data

### Major Tasks

- Defined the project question around residents living more than **2 km from the nearest mapped healthcare facility**.
- Selected **Abuja Municipal Area Council (AMAC), FCT Abuja** as the study area.
- Identified the datasets required for the analysis.
- Sourced:
  - Operational ward boundaries
  - Healthcare facility locations
  - Population estimates
  - LGA boundaries
  - Road data
- Created the initial project documentation and project brief.

### Result

A clearly defined spatial problem, study area and initial dataset requirements were established.

**Task documentation:** [`project-brief.md`](project-brief.md)

---

## Week 2 — Getting and Describing the Data

### Major Tasks

- Created a structured project folder.
- Organised raw datasets and project files.
- Downloaded the required operational ward, LGA, healthcare facility and population datasets.
- Obtained relevant road data from OpenStreetMap.
- Documented important characteristics of the datasets, including:
  - Data sources
  - Feature counts
  - Geometry types
  - Coordinate reference systems
  - Attributes
  - Missing values
  - Geometry quality
  - Spatial coverage
  - Potential data-quality issues

### Result

The required datasets were acquired, organised and documented before being used for spatial analysis.

**Task documentation:** [`data-notes.md`](data-notes.md)

---

## Week 3 — Data Quality Preparation: Clipping and Reprojection

### Major Tasks

- Clipped the geographic datasets to the **AMAC study area**.
- Reprojected the datasets to **WGS 84 / UTM Zone 32N (EPSG:32632)**.
- Prepared the datasets for distance and area calculations.
- Checked the resulting study area and prepared datasets for the next stage of analysis.

### Result

A consistent set of **clipped and projected datasets** was produced, creating the appropriate spatial foundation for the healthcare accessibility analysis.

**Task documentation:** [`data-preparation.md`](data-preparation.md)

---

## Week 4 — Spatial Operations and Analysis

### Major Tasks

- Created a **2,000-metre buffer** around mapped healthcare facilities.
- Dissolved overlapping healthcare facility buffers into a combined accessibility zone.
- Used a **difference operation** to identify areas of AMAC outside the 2 km accessibility zone.
- Calculated the areas of the resulting uncovered polygons.
- Performed checks on the resulting spatial outputs.

### Result

The spatial analysis produced:

1. A combined **2 km healthcare accessibility zone**.
2. Areas located **more than 2 km from mapped healthcare facilities**.
3. Area measurements for the identified uncovered locations.

These outputs provide the spatial foundation for determining the number of residents living beyond the project's defined healthcare accessibility threshold.

**Task documentation:** [`month-1-summary.md`](month-1-summary.md)

---

# Month 2 — Python Development Foundations

**Month 2 begins with Week 5** and marks the transition from the initial GIS workflow (graphic interface) into programming and geospatial development (terminal).

## Week 5 — Set Up Python, VS Code and Terminal

### Major Tasks

- Set up and verified **Python** through the terminal.
- Practised basic **terminal/PowerShell** commands.
- Created and organised the required development (`dev`) workspace.
- Created a screenshots folder for documenting the learning activities.
- Set up the project environment in **Visual Studio Code (VS Code)**.
- Installed and configured the **Python extension**.
- Opened and verified the VS Code integrated terminal.
- Created and executed a basic `hello.py` Python program.

### Result

A functional Python development environment was successfully established.

> **Python, VS Code and the terminal worked together correctly, and `hello.py` ran successfully.**

This establishes the programming foundation required for subsequent Python and geospatial development tasks.

**Task:** [`hello.py`](hello.py)

---

# How the Weeks Connect

The weekly tasks are designed as **one continuous project**, rather than independent exercises.

```text
MONTH 1
│
├── WEEK 1
│   Define the spatial question
│   ↓
│   Identify the study area and required datasets
│
├── WEEK 2
│   Acquire and organise the data
│   ↓
│   Document dataset characteristics and quality
│
├── WEEK 3
│   Prepare the data
│   ↓
│   Clip datasets to AMAC
│   ↓
│   Reproject to EPSG:32632
│
└── WEEK 4
    Perform spatial analysis
    ↓
    Create 2 km healthcare accessibility zones
    ↓
    Identify areas outside the accessibility zone
    ↓
    Calculate uncovered areas

MONTH 2
│
└── WEEK 5
    Set up Python development environment
    ↓
    Python + VS Code + Terminal
    ↓
    Run hello.py successfully
    ↓
    Establish foundation for programmable geospatial workflows
```
---

## Week 6 — Set Up a Python Project with `uv` and Install Pandas

Week 6 focused on managing a Python project using **uv** and installing **Pandas** for data analysis. I also created a simple verification script to confirm that Pandas was installed correctly.

### Major Tasks

- Set up the Python project using `uv`.
- Added and installed the **Pandas** library as a project dependency.
- Created a `check.py` Python script to verify the installed Pandas version.
- Executed the script to print the Pandas version in the terminal.

### Result

Successfully configured a Python project with `uv`, installed Pandas, and verified the installation by running `check.py` to display the installed Pandas version.

**Key Files:**
- [`pyproject.toml`](pyproject.toml) — Project configuration and dependency management.
- [`check.py`](check.py) — Script for verifying the installed Pandas version.

---

## Week 7 — Python Fundamentals and Error Handling

Week 7 focused on understanding six core Python concepts and applying them in a practical data analysis task using `analyse.py`.

### Major Tasks

- Learned the six fundamental Python concepts:
  - **Variables** — storing and managing values.
  - **Data Types** — understanding different kinds of data.
  - **Lists** — storing collections of values.
  - **Loops** — iterating through data.
  - **Conditions** — applying logic to make decisions.
  - **Functions** — organising reusable blocks of code.
- Created and worked with the `analyse.py` script.
- Read `wards.csv` into Python for analysis.
- Converted each ward's area value into the appropriate numerical format.
- Used conditions to classify each ward based on its area.
- Practised reading and understanding error messages calmly to identify and fix problems during execution.

### Result

Successfully applied Python fundamentals in a practical data analysis task. The `analyse.py` script reads `wards.csv`, converts ward area values, and classifies each ward. This exercise strengthened my understanding of Python's core concepts and helped me develop a more systematic approach to troubleshooting errors.

---

## Week 8 — Inspecting and Summarising AMAC Wards Data with Python

Week 8 focused on using Python to inspect and summarise the **Abuja Municipal Area Council (AMAC) operational wards dataset**. The dataset was exported in CSV format from the Month 1 QGIS project and used as input for Python-based data inspection and analysis.

### Major Tasks

- Exported the AMAC operational wards data from the Month 1 QGIS project into **CSV format**.
- Imported and inspected the exported CSV dataset using Python.
- Examined the dataset's structure, columns and available attributes.
- Used Python to inspect the ward records and their corresponding area values.
- Summarised the area information for the operational wards within AMAC.
- Connected the Python data analysis workflow to the spatial data preparation and analysis previously completed in QGIS.

### Result

Successfully used Python to inspect and summarise the **area of operational wards within Abuja Municipal Area Council (AMAC)** using data exported from the Month 1 QGIS project.

This exercise strengthened my ability to transition between GIS-generated datasets and Python-based data analysis, providing a foundation for further geospatial data processing and statistical exploration.

---

