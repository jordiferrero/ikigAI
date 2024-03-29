# ikigAI

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ikigai.streamlit.app/)

## Overview of the App

This AI assistant helps you find your ikigai. Your ikigai is your life purpose, it’s what brings you joy and inspires you to get out of bed every day.

### Steps

1. Reflect on What You Love ❤️: Think about what makes your heart sing. Consider hobbies, activities, and moments that bring you joy and fulfillment during your **work time** and **free time**. Be as specific as you can.

1. Identify Your Strengths 👍: Reflect on what you're naturally good at. This could be anything from **technical skills** to your **softer skills**.

1. Consider What the World Needs 🌍: Think about the issues or causes that matter to you. Consider how you can contribute to making a positive impact, whether it's in your community or on a larger scale.

1. Explore What You Can Be Paid For 💰 (optional): Write down known career paths or ways to turn your passions and skills into income. Think about industries or roles that align with your strengths and interests.


This AI tool will find the intersection 🎯 where your passions, strengths, societal needs, and financial opportunities overlap. This is where your Ikigai lies. You will see those results on the `Results` page.


> Experiment and Iterate 🔄: Try different paths and opportunities to see what works best for you. Stay open-minded and be willing to adapt as you discover what truly fulfills you.

### Get an OpenAI API key

For the app to work, you should get your own OpenAI API key by following the following instructions:

1. Go to https://platform.openai.com/account/api-keys.
2. Click on the `+ Create new secret key` button.
3. Next, enter an identifier name (optional) and click on the `Create secret key` button.

### Enter the OpenAI API key in Streamlit Community Cloud

To set the OpenAI API key as an environment variable in Streamlit apps, do the following:

1. At the lower right corner, click on `< Manage app` then click on the vertical "..." followed by clicking on `Settings`.
2. This brings the **App settings**, next click on the `Secrets` tab and paste the API key into the text box as follows:

```sh
OPENAI_API_KEY='xxxxxxxxxx'
```

## Run it locally

```sh
.venv\Scripts\activate.bat
pip install -r requirements.txt
streamlit run Home_page.py
```
