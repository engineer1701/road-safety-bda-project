vehicles = LOAD '/user/cvanusree1706/roadsafety/raw/Vehicle_Information_sample.csv'
  USING org.apache.pig.piggybank.storage.CSVExcelStorage(',')
  AS (Accident_Index:chararray, Age_Band_of_Driver:chararray, Age_of_Vehicle:int,
      Driver_Home_Area_Type:chararray, Driver_IMD_Decile:chararray, Engine_Capacity_CC:int,
      Hit_Object_in_Carriageway:chararray, Hit_Object_off_Carriageway:chararray,
      Journey_Purpose:chararray, Junction_Location:chararray, Make:chararray,
      Model:chararray, Propulsion_Code:chararray, Sex_of_Driver:chararray,
      Skidding_and_Overturning:chararray, Towing_and_Articulation:chararray,
      Vehicle_Leaving_Carriageway:chararray, Vehicle_Restricted_Lane:chararray,
      Vehicle_Manoeuvre:chararray, Vehicle_Reference:chararray, Vehicle_Type:chararray,
      Was_Left_Hand_Drive:chararray, Point_of_Impact:chararray, Year:int);

vehicles_nohdr = FILTER vehicles BY Accident_Index != 'Accident_Index';

vehicles_clean = FILTER vehicles_nohdr BY
      Accident_Index is not null
      AND Vehicle_Type is not null;

STORE vehicles_clean INTO '/user/cvanusree1706/roadsafety/cleaned/vehicles_clean' USING PigStorage(',');
