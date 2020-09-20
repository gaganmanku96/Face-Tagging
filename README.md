# Face Tagging

<p>This project is about</p>

## Team Members
[Gagandeep Singh]()<br>
[Sreetihi]()<br>
[Shatakshi Pauchari]()<br>
[Nilesh Bhosle]()

## How to run
### 1. Clone the repo
```
$ git clone https://github.com/gaganmanku96/Face-Tagging
$ cd Face-Tagging
```
### 2. Setup the Facical Landmark Encoding API (Optional)
> To be able to train model on new images you would need the API to work.

You can setup it by using any of the mentioned method
#### a) Docker
```
$ docker pull gaganmanku96/facial_landmarks_api
$ docker run -p 5000:5000 gaganmanku96/facial_landmarks_api
```
### b) Docker Compose
```
$ docker-compose up
```
### 3. Run the application
```
$ jupyter notebook Main.ipynb
```
