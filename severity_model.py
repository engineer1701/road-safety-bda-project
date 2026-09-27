from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder.appName("SeverityPrediction").enableHiveSupport().getOrCreate()

df = spark.sql("SELECT Accident_Severity, Weather_Conditions, Road_Surface_Conditions, Light_Conditions, Speed_limit, Number_of_Vehicles, Urban_or_Rural FROM accidents_clean")

df = df.na.drop()

cat_cols = ["Weather_Conditions", "Road_Surface_Conditions", "Light_Conditions", "Urban_or_Rural"]
indexers = [StringIndexer(inputCol=c, outputCol=c+"_idx", handleInvalid="keep") for c in cat_cols]
label_indexer = StringIndexer(inputCol="Accident_Severity", outputCol="label", handleInvalid="keep")

feature_cols = [c+"_idx" for c in cat_cols] + ["Speed_limit", "Number_of_Vehicles"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")

rf = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=50)

from pyspark.ml import Pipeline
pipeline = Pipeline(stages=indexers + [label_indexer, assembler, rf])

train, test = df.randomSplit([0.8, 0.2], seed=42)

model = pipeline.fit(train)
predictions = model.transform(test)

evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)

print("=" * 50)
print(f"MODEL ACCURACY: {accuracy}")
print("=" * 50)

predictions.select("Accident_Severity", "label", "prediction").show(20)

model.write().overwrite().save("/user/cvanusree1706/roadsafety/models/severity_rf_model")
