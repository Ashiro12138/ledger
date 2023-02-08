# To run pocketbase locally with docker
Build the image  
`$ docker build -t pocketbase .`  
Run the container  
`$ docker run -dp 8080:8080 --name pb pocketbase`  
Open it in local browser  
`http://localhost:8080/_/`  
Teardown  
`$ docker stop pb`  
`$ docker rm pb`  
