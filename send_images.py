import pyrebase
config = {
    "apiKey": "AIzaSyAyhbRzkR7qm5IMy_Kn4_GQPDSH6kW-f7A",
    "authDomain": "edgetensor2.firebaseapp.com",
    "databaseURL": "https://edgetensor2.firebaseio.com",
    "projectId": "edgetensor2",
    "storageBucket": "edgetensor2.appspot.com",
    "messagingSenderId": "445288793959",
    "appId": "1:445288793959:web:06873f3e674ba69b4d91c2",
    "measurementId": "G-X3MNRBGYM7"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "images/foo.jpg"
path_local = "eagle.jpg"

storage.child(path_on_cloud).put(path_local) # send eagle.jpg to firebae cloud storage

# storage.child(path_on_cloud).download("test_download.jpg")# retribve images from cloud
