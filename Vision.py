from pyniryo2 import *
import math
import numpy as np
import sqlite3  # Import the SQLite library
import pandas as pd
from datetime import datetime

maintenant = datetime.now()

Heureetdate = maintenant.strftime("%m/%d/%Y, %H:%M:%S")

robot_ip_address = "192.168.0.201"
learning = False
# Robot's workspace Name
workspace_name = "MAGA_BLC"
# connect to robot and calibrate
print("Starting robot")
robot = NiryoRobot(robot_ip_address)
robot.arm.calibrate_auto()
robot.tool.update_tool()
robot.arm.set_learning_mode(learning)
print("Robot bring up!")

# Task parameters
expected_shape = ObjectShape.ANY
expected_color = ObjectColor.ANY

# Define robots position
#observation_pose = ([0.009, -0.186, 0.219, 2.868, 1.497,1.11]) #observation
observation_pose = ([-0.008, -0.218, 0.212, -2.995, 1.282, 1.718])
place_pose = ([0.031, 0.149, 0.235, -3.03, 1.329, -2.979])

# Initializing variables
max_catch_count = 3
catch_count = 0

# Establish a connection to the SQL database
conn = sqlite3.connect('my_robot_data.db')  # Replace with your desired database name
c = conn.cursor()

# Create the table if it doesn't exist
c.execute("""
CREATE TABLE IF NOT EXISTS object_data (
    heure TEXT,
    color TEXT,
    position TEXT,
    shape TEXT
)
""")

print("Starting task")
while catch_count <= max_catch_count:
    # Moving the arm into observation position
    print("Moving to observation position")
    robot.arm.move_pose(observation_pose)
    print("Robot is in observation position")

    # Try to get object via vision pick
    robot.wait(4)
    obj_found, pos_array, shape_ret, color_ret = robot.vision.detect_object('MAG_BLANC', shape=expected_shape, color=expected_color)

    print(obj_found, ' ', pos_array, ' ', shape_ret)

    if obj_found:
        maintenant = datetime.now()

        Heureetdate = maintenant.strftime("%m/%d/%Y, %H:%M:%S")
        # Gather data for SQL insertion
        color = color_ret
        # Convert position array to comma-separated string
        x_str = str(pos_array.x)
        y_str = str(pos_array.y)
        z_str = str(pos_array.z)
        # Combine the strings into the desired format
        pos_array_str = x_str + ',' + y_str + ',' + z_str

        shape = shape_ret
        Heureetdate_str = str(Heureetdate)

        # Print data types for verification (optional)
        print(type(color))
        print(color)
        print(type(pos_array_str))
        print(pos_array_str)
        print(type(shape))
        print(shape)
        try:
            # Insert data into the SQL table
            c.execute("INSERT INTO object_data VALUES (?, ?, ?, ?)", (Heureetdate_str, str(color), pos_array_str, str(shape)))
            conn.commit()  # Commit the changes to the database
            print("Data added to SQL table successfully.")
        except sqlite3.Error as e:
            print("Error inserting data into SQL table:", e)

    if not obj_found:
        print('Object was not found')
        robot.wait(0.1)
        break
    else:
        print("object " + str(catch_count + 1) + " has been found")

        robot.wait(1)
        #robot.vision.vision_pick(workspace_name, 0.003)
        robot.vision.vision_pick(workspace_name)
        robot.arm.move_pose(place_pose)
        robot.pick_place.place_from_pose(place_pose)

        catch_count += 1
    print("Object count: " + str(catch_count))

# Display the SQL table content (after the loop)
print("Affichage du tableau SQL: \n  Date/Heure             Couleur                    Position                                 Forme ")
c.execute("SELECT * FROM object_data")
for row in c.fetchall():
    print(row)

# Close the database connection (after displaying the table)
conn.close()

print("Task finished")
robot.arm.go_to_sleep()
print("Stopping robot")
robot.end()
print("Robot stopped")
