REGISTER /usr/lib/pig/piggybank.jar;

accidents = LOAD '/user/cvanusree1706/roadsafety/raw/Accident_Information_sample.csv'
  USING org.apache.pig.piggybank.storage.CSVExcelStorage(',')
  AS (Accident_Index:chararray, Road_Class_1:chararray, Road_Number_1:chararray,
      Road_Class_2:chararray, Road_Number_2:chararray, Accident_Severity:chararray,
      Carriageway_Hazards:chararray, Date:chararray, Day_of_Week:chararray,
      Police_Attend:chararray, Junction_Control:chararray, Junction_Detail:chararray,
      Latitude:double, Light_Conditions:chararray, Local_Authority_District:chararray,
      Local_Authority_Highway:chararray, Location_Easting_OSGR:double,
      Location_Northing_OSGR:double, Longitude:double, LSOA:chararray,
      Number_of_Casualties:int, Number_of_Vehicles:int, Ped_Crossing_Human:chararray,
      Ped_Crossing_Physical:chararray, Police_Force:chararray,
      Road_Surface_Conditions:chararray, Road_Type:chararray, Special_Conditions:chararray,
      Speed_limit:int, Time:chararray, Urban_or_Rural:chararray,
      Weather_Conditions:chararray, Year:int, InScotland:chararray);

accidents_nohdr = FILTER accidents BY Accident_Index != 'Accident_Index';

accidents_clean = FILTER accidents_nohdr BY
      Accident_Index is not null
      AND Latitude is not null
      AND Longitude is not null
      AND Number_of_Casualties is not null;

STORE accidents_clean INTO '/user/cvanusree1706/roadsafety/cleaned/accidents_clean' USING PigStorage(',');
