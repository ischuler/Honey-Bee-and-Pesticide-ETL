CREATE SCHEMA honeybees;

USE honeybees;

CREATE TABLE bees_data(
    id INT AUTO_INCREMENT NOT NULL,
   state VARCHAR(10),
   start_colonies INT,
   end_colonies INT,
   colony_change INT,
   added_colonies INT,
   lost_colonies INT,
   renovated_colonies INT,
   colony_yield INT,
   production INT,
   PRIMARY KEY (id)
   );
   
CREATE TABLE pesticides(
	id INT AUTO_INCREMENT NOT NULL,
	state VARCHAR(10),
    compound VARCHAR(100),
    low_estimate float,
    high_estimate float,
    PRIMARY KEY (id)
    );