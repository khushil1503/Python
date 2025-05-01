#Q.1 Write a program to create a csv file that we can directly open in MS-Excel.

import csv

# Data to be written into the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# File path where the CSV will be saved
file_path = 'output.csv'

# Writing data to the CSV file
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Writing the header and data rows
    writer.writerows(data)

print(f"CSV file '{file_path}' created successfully!")

#Q.2Read the data stored in MS-Excel file and convert it into a dictionary.
#The record contains rollno, name of student, marks of three subjects. Also calculate total. Display the dictionary data on the monitor.

import pandas as pd

# Read the Excel file (replace 'data.xlsx' with your actual file path)
df = pd.read_excel('data.xlsx', engine='openpyxl')

# Assuming your Excel columns are named 'Rollno', 'Name', 'Marks1', 'Marks2', 'Marks3'
student_data = []

# Iterate through each row to create a dictionary for each student
for _, row in df.iterrows():
    # Calculate total marks for the student
    total_marks = row['Marks1'] + row['Marks2'] + row['Marks3']
    
    # Create a dictionary for each student
    student_dict = {
        'Rollno': row['Rollno'],
        'Name': row['Name'],
        'Marks1': row['Marks1'],
        'Marks2': row['Marks2'],
        'Marks3': row['Marks3'],
        'Total': total_marks
    }
    
    # Append the dictionary to the list
    student_data.append(student_dict)

# Display the data on the monitor
for student in student_data:
    print(student)

#Q.3 Accept contact details from the user and create a vcard that we can directly store in our mobile.

def create_vcard():
    # Accept user input for contact details
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    address = input("Enter Address: ")
    
    # Format the data into vCard format
    vcard_content = f"""
BEGIN:VCARD
VERSION:3.0
FN:{first_name} {last_name}
TEL:{phone_number}
EMAIL:{email}
ADR:{address}
END:VCARD
"""
    
    # Specify the file name for the vCard
    file_name = f"{first_name}_{last_name}.vcf"
    
    # Write the vCard content to a file
    with open(file_name, 'w') as vcard_file:
        vcard_file.write(vcard_content.strip())
    
    print(f"vCard for {first_name} {last_name} has been created and saved as {file_name}")

# Call the function to create a vCard
create_vcard()

#Q.4 Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory.

import os
import shutil

def copy_file_to_new_subdirectory(src_file, dest_dir):
    # Check if the destination directory exists, create it if it doesn't
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Subdirectory '{dest_dir}' created.")
    else:
        print(f"Subdirectory '{dest_dir}' already exists.")
    
    # Ensure the source file exists before attempting to copy
    if os.path.exists(src_file):
        # Copy the source file to the destination directory
        shutil.copy(src_file, dest_dir)
        print(f"File '{src_file}' copied to '{dest_dir}'.")
    else:
        print(f"Source file '{src_file}' does not exist.")

# Specify the source file and the destination directory
source_file = "path_to_source_subdirectory/source_file.txt"  # Replace with your source file path
destination_directory = "path_to_new_subdirectory"  # Replace with your destination subdirectory

# Call the function to copy the file
copy_file_to_new_subdirectory(source_file, destination_directory)


#Q.5 Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters.

def copy_and_convert_case(src_file, dest_file):
    try:
        # Open the source file in read mode
        with open(src_file, 'r') as src:
            # Read the content of the source file
            content = src.read()

        # Convert all lowercase characters to uppercase
        content_upper = content.upper()

        # Open the destination file in write mode
        with open(dest_file, 'w') as dest:
            # Write the modified content to the destination file
            dest.write(content_upper)
        
        print(f"Contents copied from '{src_file}' to '{dest_file}' with all lowercase characters converted to uppercase.")
    except FileNotFoundError:
        print(f"Error: The file '{src_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the source and destination file paths
source_file = 'source.txt'  # Replace with the path to your source file
destination_file = 'destination.txt'  # Replace with the path to your destination file

# Call the function to copy and convert case
copy_and_convert_case(source_file, destination_file)

#Q.6 Write a program that merges lines alternatively from two files and writes the results to new file.
#If one file has less number of lines than the other, the remaining lines from the larger file should be simply copied into the target file.

def merge_alternate_lines(file1, file2, output_file):
    try:
        # Open the two source files in read mode
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            # Read all lines from both files
            lines1 = f1.readlines()
            lines2 = f2.readlines()

        # Open the output file in write mode
        with open(output_file, 'w') as out_file:
            # Get the maximum number of lines to process
            max_lines = max(len(lines1), len(lines2))

            # Merge lines alternatively
            for i in range(max_lines):
                # Write from the first file if available
                if i < len(lines1):
                    out_file.write(lines1[i])

                # Write from the second file if available
                if i < len(lines2):
                    out_file.write(lines2[i])

        print(f"Lines from both files have been merged into '{output_file}' successfully.")
    
    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the paths of the two input files and the output file
file1 = 'file1.txt'  # Replace with the path of the first file
file2 = 'file2.txt'  # Replace with the path of the second file
output_file = 'merged_output.txt'  # Replace with the desired output file path

# Call the function to merge the lines
merge_alternate_lines(file1, file2, output_file)


#Q.7 If an Employee object contains following details:
#empcode, empname, Date of Joining, Salary
#Write a program to serialize and deserialize this data.

import pickle
from datetime import datetime

# Define the Employee class
class Employee:
    def __init__(self, empcode, empname, date_of_joining, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = date_of_joining
        self.salary = salary
    
    def __str__(self):
        return f"Employee Code: {self.empcode}, Name: {self.empname}, Date of Joining: {self.date_of_joining}, Salary: {self.salary}"

# Function to serialize the Employee object to a file
def serialize_employee(employee, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(employee, file)
        print("Employee object serialized successfully.")
    except Exception as e:
        print(f"Error during serialization: {e}")

# Function to deserialize the Employee object from a file
def deserialize_employee(filename):
    try:
        with open(filename, 'rb') as file:
            employee = pickle.load(file)
        return employee
    except Exception as e:
        print(f"Error during deserialization: {e}")
        return None

# Create an Employee object
emp1 = Employee(
    empcode=101,
    empname="John Doe",
    date_of_joining=datetime(2020, 5, 1),
    salary=50000
)

# File where the serialized object will be saved
filename = 'employee.dat'

# Serialize the Employee object
serialize_employee(emp1, filename)

# Deserialize the Employee object
emp2 = deserialize_employee(filename)

# Print the deserialized object
if emp2:
    print("Deserialized Employee Data:")
    print(emp2)


#Q.8 Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and replacing each one of
    #them with a blank space.

import pickle
from datetime import datetime

# Define the Employee class
class Employee:
    def __init__(self, empcode, empname, date_of_joining, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = date_of_joining
        self.salary = salary
    
    def __str__(self):
        return f"Employee Code: {self.empcode}, Name: {self.empname}, Date of Joining: {self.date_of_joining}, Salary: {self.salary}"

# Function to serialize the Employee object to a file
def serialize_employee(employee, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(employee, file)
        print("Employee object serialized successfully.")
    except Exception as e:
        print(f"Error during serialization: {e}")

# Function to deserialize the Employee object from a file
def deserialize_employee(filename):
    try:
        with open(filename, 'rb') as file:
            employee = pickle.load(file)
        return employee
    except Exception as e:
        print(f"Error during deserialization: {e}")
        return None

# Create an Employee object
emp1 = Employee(
    empcode=101,
    empname="John Doe",
    date_of_joining=datetime(2020, 5, 1),
    salary=50000
)

# File where the serialized object will be saved
filename = 'employee.dat'

# Serialize the Employee object
serialize_employee(emp1, filename)

# Deserialize the Employee object
emp2 = deserialize_employee(filename)

# Print the deserialized object
if emp2:
    print("Deserialized Employee Data:")
    print(emp2)
