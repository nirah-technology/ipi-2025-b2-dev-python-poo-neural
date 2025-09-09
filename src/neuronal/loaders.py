import csv
import json
import pickle

class Loader:

    @staticmethod
    def backup_as_csv(file_destination: str, data: list[list]):
        with open(file_destination, "w") as file:
            writer = csv.writer(file)
            writer.writerows(data)
    
    @staticmethod
    def restore_as_csv(file_destination: str) -> list[list]:
        lines: list[list] = []
        with open(file_destination, "r") as file:
            reader = csv.reader(file)
            for line in reader:
                lines.append(line)
        return lines

    @staticmethod
    def backup_as_json(file_destination: str, data: any):
        with open(file_destination, "w") as file:
            json_content: str = json.dumps(data)
            file.write(json_content)
    
    @staticmethod
    def restore_as_json(file_destination: str) -> any:
        with open(file_destination, "r") as file:
            file_content: str = file.read()
            data: any = json.loads(file_content)
            return data

    @staticmethod
    def backup_as_pickle(file_destination: str, data: any):
        with open(file_destination, "w") as file:
            pickle.dump(data, file)
    
    @staticmethod
    def restore_as_pickle(file_destination: str) -> any:
        with open(file_destination, "r") as file:
            data: any = pickle.loads(file)
            return data
