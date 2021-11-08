import uuid
import json


def create_file(filename='data.json'):
    snapshotdb={"snapshot_list":[]}
    with open(filename,'a+') as jsonFile:
         json.dump(snapshotdb, jsonFile)



def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["snapshot_list"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
if __name__ == "__main__":
		create_file()