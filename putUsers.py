import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('Doulos_1.png','Doulos htet2'),
      ('Mihir_1.png','Mihir Parekh'),
      ('Vishal_1.png','Vishal Patel'),
      ('Cristian_1.png','Cristian Restrepo')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('serverless-team-4-s3uploadbucket-8qgj3onpd8i7','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})