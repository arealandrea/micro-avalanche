# import packages
import streamlit as st
import pandas as pd
import re
import os
import openai   
from dotenv import load_dotenv
import plotly.express as px

load_dotenv()

client = openai.OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input = [{"role": "user", "content": "Suggest a parallel to holography in other unrelated fields in 2 sentences."}],
    temperature=0.5,
    max_output_tokens=300
)

print(response.output[0].content[0].text)