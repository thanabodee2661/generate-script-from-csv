import os
import csv

full_path = os.path.realpath(__file__)
current_path = os.path.dirname(full_path)
print(current_path)

file_path = "${current_path}/../resources"
file_name = "myFile0.csv"

# normal readfile
# print(f"{file_path}/{file_name}")
# f = open(f"{file_path}/{file_name}", mode="r")
# print(f.read())

table_temp = "table_name"

query_list = []
# Open the file for reading
with open(f"{file_path}/{file_name}", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        column_temp = ", ".join(row.keys())
        value_temp = ", ".join([f"\"{value}\"" for value in row.values()])
        query_str_temp = f"insert into {table_temp} ({column_temp}) values ({value_temp});"
        query_list.append(query_str_temp)

csv_file.close()

output_file_name = "test.sql"
# Open the file for writing
with open(f"{file_path}/{output_file_name}", "w") as file:
    # Write the SQL query to the file
    file.write("\n".join(query_list))

file.close()

print("Generate File Successful....")