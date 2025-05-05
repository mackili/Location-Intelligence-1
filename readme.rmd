---
title: "Location Intelligence 1"
author: Maciej Kilijański
output: github_document
---

# Unit 1 - Exploratory point pattern analysis

Either clustering od dispersion. The dataset is tested against CSR (Complete Spatial Randomness).

There are 4 techniques:

* Quadrat Methods - arbitrary division of region into a grid, then counting points in each cell.
A histogram is then retrieved which allows to compare the distribution to CSR.
* Kernel Estimators - adds a smoothing constant, which becomes the painpoint.
* Distance Methods - utilizing exact locations to measure distances between points, allowing to identify clusters or regularity/
Then a cumulative probability distribution function is calculated from these distances and compared to a 45 degree slope.
A quick climb of a function indicates mostly small distances (clustering), a slow climb indicates regularity.
* K-Function - examines how the number of events within a given distance from any event compares to what we
should expect under a CSR. No human judgement is required.

In the article "Improving Near Miss Detection in Maritime Traffic in the Northern
Baltic Sea from AIS Data," Du et al. (2021) employed both clustering and hotspot analysis to
enhance the detection of near-miss events in maritime traffic. Clustering was used to categorize
ship behaviors and identify risk patterns, especially vessel encounters.

# Unit 2 - p-median Optimization Problem

Given a set of alternative facility locations, a set of customers to be served and the distance between then
we need to find $p$ facilities to serve customers such that the demand weighted distance is mimimized.

**Every customer has to be served**  
**Customers can only be served from open facilities**

## Variables

Variable | Meaning
--- | ---
$$I$$ | Set of warehouses/locations
$$J$$ | Set of customers
$$d_j$$ | Demand of customer $j$
$$p$$ | Number of facilities to open
$$dist_{ij}$$ | Distance between location $i$ and customer $j$
$$y_i$$ | Whether facility $i$ is open (1) or closed (0)
$$x_{ij}$$ | Whether customer $j$ is served by facility $i$ (1), 0 otherwise

$$\text{Min}\sum_{i\in I}\sum_{j\in J}dist_{ij}x_{ij}$$
$$\text{Subject to:}$$
$$\sum_{i\in I}x_{ij}=1, \forall j\in J$$
$$\sum_{i\in I}y_{i}=P$$
$$x_{ij}\leq y_i, \forall i\in I\forall j\in J$$
$$x_{ij}\in\{0,1\}, \forall i\in I\forall j\in J$$
$$x_{ij}\in\{0,1\}, \forall i\in I\forall j\in J$$
$$y_{i}\in\{0,1\}, \forall i\in I$$

### Python data model

#### List

```python
Customers = ["Chicago", "Atlanta", "NewYork"]
```

#### Dictionary

```python
demand = {
    "Chicago": 2870000,
    "Atlanta": 572000
    }
```
# Unit 3 - Core methods and tools for ESDA - Exploratory Spatial Data Analysis
 
## Local and global Moran's I

Statistical tool measuring spatial autocorrelation allowing researchers to understand
if nearby locations have similar or different attribute values. Therefore showing whether 
high or low values of an attribute are clustered with each other or not (Ratzenböck & Ecker, 2021).

### Calculation of Moran's I

We consider two factors: location of the features and attribute values represented by each data point.

Then, a null hypothesis $H_0$ assumes no spatial correlation, meaning a random distribution of attributes
around space. The $H_0$ is then tested with 5 key values:

Value | Description
---|---------
Morans'I Index | A number between -1 and +1 indicating clustering (whether points are closer to other points with similar values). -1 indicates perfect dispersion, 0 no spatial autocorrelation and +1 perfect clustering.
Expected Index | Expected index in the dataset if no spatial autocorrelation would be present
Variance | Variation of overall calculated Moran's I Indexes compared to their mean.
Z-score | How many standard deviations the observed Moran's I Index is from the expected index, which as mentioned earlier reflects a scenario with no spatial auto correlation
P-value | Significance of the result, whether spatial autocorrelation is statistically present

### Global vs. Local Moran's I
    "NewYork": 8450000,

When looking at Moran's I, it is important to understand what scope is being analysed.
Global Moran's I measure spatial autocorrelation over the entire data set, hence analysing
clustering across all data.

On the other hand, local Moran's I proceeds to the calculation for
each individual point, allowing to distinguish outliers and clusters on a local level.

## Incremental Spatial Autocorrelation

Incremental Spatial Autocorrelation evaluates spatial autocorrelation across a range of distances to identify scales at which spatial processes are most pronounced. This method helps determine the appropriate distance thresholds for further spatial analyses.

### Calculation of Incremental Spatial Autocorrelation

The process involves calculating Global Moran's I at successive distance increments. For each distance, the following values are computed:

- **Moran's I Index:** Indicates the degree of spatial autocorrelation at a specific distance.
- **Expected Index:** The expected Moran's I value under the null hypothesis of spatial randomness.
- **Variance:** Measures the variability of Moran's I values across different distances.
- **Z-score:** Indicates how many standard deviations the observed Moran's I is from the expected value.
- **P-value:** Assesses the statistical significance of the observed spatial autocorrelation.

By plotting z-scores against distances, peaks in the z-score indicate distances where spatial clustering is most significant. 

## Getis-and-Ord Statistics

Getis-Ord statistics, specifically the Gi* statistic, identify local clusters of high or low values, known as hot and cold spots. This method focuses on local spatial associations rather than global patterns.

### Calculation of Getis-and-Ord Gi*

The Gi* statistic for a feature i is calculated as:

$$G_i^*=\frac{\sum_{j} w_{ij} x_j}{\sum_{j} x_j}$$

Where:

* \( x_j \) is the attribute value at location j.
* \( w_{ij} \) is the spatial weight between locations i and j.

The numerator represents the weighted sum of the attribute values within the neighborhood of feature i, and the denominator is the sum of all attribute values. A high positive Gi* indicates a cluster of high values (hot spot), while a high negative Gi* indicates a cluster of low values (cold spot). 

## Multi-Distance Spatial Cluster Analysis (Ripley's K Function)

Ripley's K function assesses spatial clustering or dispersion over a range of distances, providing insights into spatial patterns at multiple scales.

### Calculation of Ripley's K Function

Ripley's K function is defined as:

\[ K(d) = \lambda^{-1} E[\text{number of additional points within distance } d \text{ of a randomly chosen point}] \]

Where:
- \( \lambda \) is the average density of points.

In practice, the L(d) transformation is often used:

\[ L(d) = \sqrt{\frac{K(d)}{\pi}} - d \]

If L(d) > 0, it indicates clustering at distance d; if L(d) < 0, it indicates dispersion. 

## Space-Time Clustering

> Useful for clustering seasonal events like wildfires.

Patterns are clustered not only in space but also in time. Let's say car traffic is clustered not only based on street but also based on hour it occured.

### Calculation of Space-Time Clustering

This method involves:

1. **Data Aggregation:** Aggregating data into space-time bins.
2. **Trend Analysis:** Evaluating trends within each bin.
3. **Hotspot Detection:** Identifying statistically significant clusters over time.

This analysis is crucial for monitoring phenomena that evolve over time, such as wildfires or crime trends.

## Kernel Density Estimation

Kernel Density Estimation (KDE) creates a continuous surface representing the density of point or line features, useful for visualizing concentrations.

### Calculation of Kernel Density Estimation

KDE is calculated as:

\[ \hat{f}(x) = \frac{1}{n h} \sum_{i=1}^{n} K\left( \frac{x - x_i}{h} \right) \]

Where:
- \( n \) is the number of data points.
- \( h \) is the bandwidth (smoothing parameter).
- \( K \) is the kernel function.

The choice of bandwidth and kernel function affects the smoothness and accuracy of the density estimate.

Each of these methods provides unique insights into spatial patterns, aiding in comprehensive spatial analysis. 

# Unit 5 - Location Intelligence in the Cloud

Data (especially transactional) generated by businesses often contains a georaphical components, allowing for another
dimension of analysis and insights.

Location analytics is then a visual way of interpreting and analyzing the information being portrayed by the data when used in conjunction with a geographical information system.

## Essential characteristics of Cloud Computing

**NOREM**

* **N** as **Network access**. Cloud computing can be accessed from any device connected to the internet.
* **O** as **On-demand self-service**. Cloud computing is accessible at will, without a need for permission from other human being.
* **R** as **Resource pooling**. Cloud computing uses shared resources for different clients. Thanks to this we have a benefit of balanced load.
* **E** as **Elasticity**. Cloud computing can be scaled up or down to meet demand and decrease waste.
* **M** as **Measured service**. Cloud computing is billed by resources used. Look at Snowflake.

## Cloud Computing Service Models

1. Packaged Software
2. Infrastructure as a service (IaaS)
3. Platform as a service (PaaS)
4. Software as a service (SaaS)

## Cloud Computing Standards

1. WMS - Web Map Services
2. WFS - Web Feature Services
3. WMTS - Web Map Tile Services
4. WCS - Web Coverage Services

## Geolibraries vs. Geoportals

Geolibrary | Geoportal
--|--
A digital library containing georeferenced information | Geolibrary + set of GIS Services
More of a database | A shop for information relevant to GIS offering some basing data processing.

# Unit 4 + 6 - Optimization problem types

## Location-Routing problems

Location planning and vehicle routing combined in one model. These are mostly
discrete problems. Thei objective is to minimize the total cost: *fixed cost per opened facility + variable per routing*.

### Solving LRPs

Heuristics | Metaheuristics | Exact Methods
---|---|---
Hierarchical methods | Complex problems | Algorithms
Near-exact method | Many variables | For capacitated problems

### Real-life applications

* Time windows
    - Fixed delivery time & SLA
* Multiobjective
    - SLA & $\text{CO}_\text{2}$ reduction
* Capacitated
    - Limit on trucks per depot
* Time dynamics
    - Live traffic input

## Location-Arc Routing Problems

Problems, where demand is allocated on links instead of the nodes.  
Heuristics rely on the solution of subproblems

### Real-life applications

* Banking Industry
    - Time windows in cash supply centers and banking units
* Public transport scheduling
    - Necessity to move people from station A to B
* Waste management
    - Capacitated using electric
vehicles, involving
charging stations & waste
collection centres

## Covering Location Problems

Problems where the goal is to cover all demand or maximize the demand coverage.
An example can be emergency response time within 5 minutes in the entire city. Where to locate facilities?

## Hierarchical Facility location problems

Given a set of customers that demand one ore multiple services, and a set of $k$ facilities
providing these services, we select facilities to open so that each customer receives requested services,
while optimizing the objective.

> Facilities do interact within the network.  

> Facilities answer different needs or customer types.

### Categorization

Category | Description
--|----
Nature of demand | Single vs Multiple demand. Can one facility cover all demands, or are multiple needed for a customer.
Inclusiveness | Can a facility above provide the service offered at the lower level?  Yes: Successfully Inlcusive.  No: cussessfully exclusive.  Or mixed.
Flow pattern | Single vs Multi flow.
Objectives | Fixed Charge Model: mimimize fixed cost, Median Model: minimize variable cost, Coverage-based model: maximize coverage