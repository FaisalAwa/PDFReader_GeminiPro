# from dotenv import load_dotenv
# load_dotenv() ##  load all the environment variables  from .env

# import streamlit as st
# import os
# from PIL import Image
# import google.generativeai as genai

# genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# ## Function to load Gemini Pro Vision ( Gemini-1.5-flash )

# model = genai.GenerativeModel("gemini-1.5-flash")

# def get_gemini_response(input,image,prompt):
#     response = model.generate_content([input,image[0],prompt])
#     return response.text

# def input_image_details(uploaded_file):
#     if uploaded_file is not None:
#         # Read the file into bytes
#         bytes_data = uploaded_file.getvalue()

#         image_parts = [
#             {
#                 "mime_type": uploaded_file.type, # Ge the mime type of the uploaded file
#                 "data":bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# ## Initiliza our streamlit app

# st.set_page_config(page_title = "MultiLangague Invoice Extractor")
# st.header("MultiLanguage Invoice Extractor")
# input = st.text_input("Input Prompt: ",key="input")
# uploaded_file = st.file_uploader("Choose an image of the invoice.....", type=["jpg","jpeg","png"])
# image = ""
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image,caption="Uploaded Image.", use_column_width = True)

# submit = st.button("Tell me about the invoice")

# input_prompt = """
# You are an expert in understanding invoices. We will upload an image as invoice and you will have to answer any wuestions based on the uploaded invoice image
# """
# ## If submit button is clicked

# if submit:
#     image_data = input_image_details(uploaded_file)
#     response = get_gemini_response(input_prompt, image_data,input)
#     st.subheader("The Response is ")
#     st.write(response)


from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Vision (Gemini-1.5-flash)
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text, image, prompt):
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Function to add custom CSS for styling
def add_custom_css():
    st.markdown(
        """
        <style>
        .blinking {
            animation: blinker 1.5s linear infinite;
        }
        @keyframes blinker {
            50% {
                opacity: 0;
            }
        }
        .header {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #FFFFFF;
        }
        .description {
            font-size: 18px;
            color: #AAAAAA;
        }
        body {
            background-color: #001f3f;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_css()

# Initialize our Streamlit app
# st.set_page_config(page_title="MultiLanguage Invoice Extractor", layout="wide")

# SVG Animation
st.markdown("""
<svg width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <g>
    <title>Invoice Expert</title>
    <rect width="100%" height="200" fill="#001f3f" />
    <circle cx="150" cy="100" r="80" fill="#AAAAAA" />
    <text x="150" y="115" font-size="35" font-family="Arial" fill="#000000" text-anchor="middle">📄</text>
    <text x="50%" y="180" font-size="24" font-family="Arial" fill="#FFFFFF" text-anchor="middle">
      <animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite" />
      Multi Voice Text Extractor
    </text>
  </g>
</svg>
""", unsafe_allow_html=True)

st.markdown('<div class="header">MultiLanguage Invoice Extractor 🌐📄</div>', unsafe_allow_html=True)
st.markdown('<div class="description blinking">Upload an invoice image and get detailed information instantly!</div>', unsafe_allow_html=True)

st.write("""
### Project Description:
This project leverages the power of the Gemini Pro Vision model to extract and understand text from invoice images in multiple languages. Simply upload an invoice image and provide any specific prompts or questions you have about the invoice, and our AI will provide detailed responses. This tool is perfect for businesses and individuals who need quick and accurate invoice processing and analysis.
""")

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding invoices. We will upload an image as an invoice and you will have to answer any questions based on the uploaded invoice image.
"""

# If submit button is clicked
if submit:
    if uploaded_file is not None:
        image_data = input_image_details(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input_text)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.error("Please upload an invoice image.")
