from pyspark.sql import SparkSession
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

spark = SparkSession.builder.appName("Charts").enableHiveSupport().getOrCreate()

# Chart 1: Top 10 hotspot districts
hotspots = spark.sql("SELECT district, total_accidents FROM accident_hotspots ORDER BY total_accidents DESC").toPandas()
plt.figure(figsize=(10,6))
plt.barh(hotspots['district'], hotspots['total_accidents'], color='crimson')
plt.xlabel('Total Accidents')
plt.title('Top Accident Hotspot Districts')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('/home/cvanusree1706/hotspots_chart.png')
plt.close()

# Chart 2: Accidents by speed limit
speed = spark.sql("SELECT Speed_limit, COUNT(*) as total FROM accidents_clean GROUP BY Speed_limit ORDER BY Speed_limit").toPandas()
plt.figure(figsize=(10,6))
plt.bar(speed['Speed_limit'].astype(str), speed['total'], color='steelblue')
plt.xlabel('Speed Limit (mph)')
plt.ylabel('Number of Accidents')
plt.title('Accidents by Speed Limit')
plt.tight_layout()
plt.savefig('/home/cvanusree1706/speedlimit_chart.png')
plt.close()

# Chart 3: Severity distribution
severity = spark.sql("SELECT Accident_Severity, COUNT(*) as total FROM accidents_clean GROUP BY Accident_Severity").toPandas()
plt.figure(figsize=(7,7))
plt.pie(severity['total'], labels=severity['Accident_Severity'], autopct='%1.1f%%', colors=['lightcoral','gold','lightgreen'])
plt.title('Accident Severity Distribution')
plt.tight_layout()
plt.savefig('/home/cvanusree1706/severity_chart.png')
plt.close()

print("Charts saved successfully!")
