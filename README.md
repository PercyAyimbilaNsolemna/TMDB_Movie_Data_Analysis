# TMDB Movie Analytics Pipeline

A **production-grade data analytics project** that extracts, processes, analyzes, and visualizes movie data from **The Movie Database (TMDB) API** using Python. The project is designed with **robust data engineering principles**, reusable utility functions, and clean analytical workflows suitable for **research, portfolio, or production use**.

---

## Project Overview

This project performs **end-to-end movie data analysis**, including:

* Securely fetching movie metadata from the TMDB API
* Persisting raw data to disk in a structured format
* Cleaning and transforming complex nested JSON fields
* Engineering analytical features such as **ROI**, **cast size**, and **director extraction**
* Performing advanced filtering and ranking queries
* Comparing **franchise vs standalone movie performance**
* Identifying **top-performing directors and franchises**
* Producing insightful **data visualizations** using Matplotlib

The codebase is modular, extensible, and follows **best practices in data validation, error handling, and efficiency**.

---

## Project Structure

```text
.
├── data/
│   └── movieData.csv              # Persisted movie dataset
│
├── requirements/
│   └── requirements.txt           # Project dependencies
│
├── Data_Extraction/
│   ├── api/                        # API extraction utilities
│   ├── preprocessing/              # Cleaning & transformation logic
│   ├── analysis/                   # Ranking, filtering & aggregations
│   ├── visualization/              # Matplotlib visualizations
│   └── utils/                      # Reusable helper functions
│
├── Data Cleaning/
|   ├── convertDataType              # Converts the DataType of a specified column
│   ├── convertNumeric               # Converts the datatype of a column to numeric
│   ├── extractColumn                # Extracts specific data from a column
│   ├── getColumnSize                # Gets the number of data in each row in a column
│   └── removeColumn                 # Remove a column from the dataFrame
|   
|── Data Analysis/
|   ├── Data Visualization/          # All functions related to data visualization
│   ├── KPI Analysis/                # Handles all KPI Analysis Logic
|                              
├── notebooks/                      # Presents the entire workflow in a clear and concise manner
│
└── README.md                       # Project documentation
```

---

## ⚙️ Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/PercyAyimbilaNsolemna/TMDB_Movie_Data_Analysis.git
cd TMDB_Movie_Data_Analysis
```


### Install Dependencies

All required packages are defined in:

```text
requirements/requirements.txt
```

Install them using:

```bash
pip install -r requirements/requirements.txt
```

---

## TMDB API Configuration

This project requires a **TMDB API Bearer Token**.

1. Create an account at: [https://www.themoviedb.org/](https://www.themoviedb.org/)
2. Generate an API Read Access Token
3. Store the token securely (recommended: environment variable)

```bash
export TMDB_API_KEY="your_api_key_here"
```

---

## Data Extraction

Movie data is fetched using the TMDB endpoint:

```text
https://api.themoviedb.org/3/movie/{movie_id}?append_to_response=credits
```

### Extracted Data Includes:

* Movie metadata (title, runtime, budget, revenue, popularity)
* Genre information
* Cast and crew (via `credits`)
* Collection membership

The pipeline:

* Skips missing movie IDs gracefully
* Handles network and API errors robustly
* Saves the extracted dataset to:

```text
./data/movieData.csv
```

---

## Data Processing & Feature Engineering

Key transformations include:

### Column Normalization

* Flattening nested JSON structures
* Separating pipe-delimited genre fields

### Numeric Engineering

* Revenue & budget scaling (e.g. millions USD)
* ROI calculation:

```text
ROI = revenue / budget
```

### Crew & Cast Analysis

* Cast size per movie
* Crew size per movie
* Director name extraction from `credits.crew`

### Grouping Logic

* Franchise vs Standalone classification based on `belongs_to_collection`

---

## Advanced Queries Implemented

### Search Queries

* Best-rated **Science Fiction Action** movies starring *Bruce Willis*
* Movies starring *Uma Thurman* directed by *Quentin Tarantino*

### Performance Comparisons

* Franchise vs Standalone movies:

  * Mean revenue
  * Median ROI
  * Mean budget
  * Popularity & rating trends

### Rankings

* Most successful franchises
* Most successful directors based on:

  * Total movies directed
  * Total revenue
  * Mean rating

---

## Data Visualizations

Visualizations are built using **Pandas + Matplotlib** and include:

* Revenue vs Budget trends
* ROI distribution by genre (boxplots)
* Popularity vs Rating scatter plots
* Yearly box office performance
* Franchise vs Standalone comparisons

All plots are designed to be **publication-ready and interpretable**.

---

## Error Handling & Robustness

The pipeline includes:

* Custom exception handling (`ApiRequestError`)
* Safe JSON parsing
* Graceful handling of missing values
* Validation of inputs and schema assumptions

---

## Reproducibility

* Deterministic transformations
* Clean separation of concerns
* Modular functions for reuse in notebooks or production systems

---

## Future Improvements

* Store raw JSON responses alongside CSV

* Add Parquet support for efficient storage

* Integrate Seaborn / Plotly dashboards

* Automate ingestion using Airflow or Prefect

* Extend to TV shows & person endpoints

## License

This project is licensed under the MIT License.

## Author

Percy Ayimbila Nsolemna
Data Scientist | Machine Learning Engineer

## Acknowledgements

The Movie Database (TMDB) API

Open‑source Python ecosystem
