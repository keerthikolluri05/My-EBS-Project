import os

# Path to the mounted volume
mount_path = '/mnt/mydata'  # Replace with your mount path

def write_data_to_file(file_name, data):
    file_path = os.path.join(mount_path, file_name)
    with open(file_path, 'w') as file:
        file.write(data)
    print(f'Data written to {file_path}')
# Example usage
file_name = 'example.txt'
data = 'ISHIP Data'
write_data_to_file(file_name, data)
