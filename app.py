import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load the trained model
model = load_model('emotion_recognition_model.h5')

# Define emotions
emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Streamlit app
st.title('Facial Emotion Recognition')
st.markdown("""
    Made by Pratik.S
    
    Welcome to the Facial Emotion Recognition App!  
    Upload an image of a face, and the model will predict the emotion.  
    Supported emotions: **Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise**
""")

# Option to upload an image or use the camera
option = st.radio("Choose an option:", ("Upload an Image", "Use Camera"))

if option == "Upload an Image":
    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Load and preprocess the image
        image = Image.open(uploaded_file).convert('L')  # Convert to grayscale
        image = image.resize((48, 48))  # Resize to 48x48
        img_array = np.array(image).reshape(1, 48, 48, 1) / 255.0  # Normalize

        # Display the uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Predict the emotion
        prediction = model.predict(img_array)
        predicted_emotion = emotions[np.argmax(prediction)]

        # Display the predicted emotion
        st.write(f"Predicted Emotion: **{predicted_emotion}**")
        st.write("Prediction Probabilities:")
        for i, emotion in enumerate(emotions):
            st.write(f"{emotion}: {prediction[0][i]:.4f}")

        # Feedback mechanism
        st.write("Was the prediction correct?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes"):
                st.write("Thank you for your feedback! 😊")
        with col2:
            if st.button("No"):
                st.write("We’ll work on improving the model! 🙏")

else:
    # Camera input
    picture = st.camera_input("Take a picture")

    if picture:
        # Load and preprocess the image
        image = Image.open(picture).convert('L')  # Convert to grayscale
        image = image.resize((48, 48))  # Resize to 48x48
        img_array = np.array(image).reshape(1, 48, 48, 1) / 255.0  # Normalize

        # Display the captured image
        st.image(image, caption='Captured Image', use_column_width=True)

        # Predict the emotion
        prediction = model.predict(img_array)
        predicted_emotion = emotions[np.argmax(prediction)]

        # Display the predicted emotion
        st.write(f"Predicted Emotion: **{predicted_emotion}**")
        st.write("Prediction Probabilities:")
        for i, emotion in enumerate(emotions):
            st.write(f"{emotion}: {prediction[0][i]:.4f}")

        # Feedback mechanism
        st.write("Was the prediction correct?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes"):
                st.write("Thank you for your feedback! 😊")
        with col2:
            if st.button("No"):
                st.write("We’ll work on improving the model! 🙏")