import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
# --- 1. Synthetic Data Generation ---
# Generate synthetic store location data
num_stores = 100
np.random.seed(42)  # for reproducibility
store_data = {
    'StoreID': range(1, num_stores + 1),
    'Latitude': np.random.uniform(37, 38, num_stores),
    'Longitude': np.random.uniform(-122, -121, num_stores),
    'Sales': np.random.randint(10000, 100000, num_stores),
    'CompetitorsNearby': np.random.randint(0, 5, num_stores)
}
df_stores = pd.DataFrame(store_data)
# Create shapely points for geospatial analysis
df_stores['geometry'] = df_stores.apply(lambda row: Point(row.Longitude, row.Latitude), axis=1)
gdf_stores = gpd.GeoDataFrame(df_stores, geometry='geometry', crs="EPSG:4326")
# --- 2. Analysis ---
# Calculate store density (simplified - assumes uniform area)
store_density = len(df_stores) / ((38 - 37) * (-121 - (-122)))
print(f"Approximate Store Density: {store_density:.2f} stores per degree squared")
# Identify potential areas of oversaturation (simplified - based on sales and competitors)
df_stores['Oversaturation'] = (df_stores['Sales'] < 50000) & (df_stores['CompetitorsNearby'] > 2)
oversaturated_stores = df_stores[df_stores['Oversaturation']]
print(f"Number of potentially oversaturated stores: {len(oversaturated_stores)}")
# --- 3. Visualization ---
# Plot store locations
plt.figure(figsize=(10, 8))
gdf_stores.plot(column='Sales', cmap='viridis', legend=True, markersize=30, alpha=0.7, ax=plt.gca())
plt.title('Store Locations and Sales')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('store_locations.png')
print("Plot saved to store_locations.png")
# Plot oversaturated stores
plt.figure(figsize=(10, 8))
oversaturated_stores.plot(color='red', markersize=50, alpha=0.7, ax=plt.gca())
plt.title('Potentially Oversaturated Stores')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('oversaturated_stores.png')
print("Plot saved to oversaturated_stores.png")
#Note:  A more sophisticated analysis would involve clustering algorithms (e.g., KMeans) and incorporating demographic data for a more robust assessment of market saturation and optimal new store locations.  This example provides a basic framework.