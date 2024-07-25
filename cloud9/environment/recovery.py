import boto3
# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # Replace with your region

def detach_volume(volume_id):
    response = ec2.detach_volume(VolumeId=volume_id)
    print(f'Volume {volume_id} detached successfully.')
    return response

def delete_volume(volume_id):
    response = ec2.delete_volume(VolumeId=volume_id)
    print(f'Volume {volume_id} deleted successfully.')
    return response

# Example usage
volume_id = 'vol-03306352f1be28d21'  # Replace with your volume ID

# Detach the volume
detach_volume(volume_id)

# Wait for the volume to detach
ec2.get_waiter('volume_available').wait(VolumeIds=[volume_id])

# Delete the volume
delete_volume(volume_id)
