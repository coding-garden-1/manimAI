import json
import requests
import openai
import os
import sounddevice as sd
import scipy.io.wavfile as wav
from openai import OpenAI
import subprocess
import webbrowser
import time
import os

import os

def play_video(video_file):
    # Convert the video file path to an absolute path
    full_video_path = os.path.abspath(video_file)
    
    # Ensure the video file path is correct
    if os.path.exists(full_video_path):
        # Open the video file with the default media player
        os.startfile(full_video_path)
    else:
        print(f"Video file '{full_video_path}' not found.")

def llm_call(actions_list,  user_prompt):
    openai.api_key = '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'
    class ChatCompletionMessage:
        def __init__(self, content, role, function_call=None, tool_calls=None):
            self.content = content
            self.role = role
            self.function_call = function_call
            self.tool_calls = tool_calls

        def get_text_content(self):
            # Return only the text content
            return self.content
        # Initialize the OpenAI client
    client = openai.OpenAI()

    # Your code for interacting with the OpenAI API goes here
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """note, self.time doesnt exist in manim 0.10.0 that we are using. Your job is to take in a user's math sentence and use your knowledge of Manim (gathered from this list: {actions_list}) and return fully functional Manim code with no placeholders. Please note your output will be parsed as raw code through Manim without any chance to adjust it, so do not leave anything unfinished. Also, u cannto import *, u most instead import the relevant modules or whatever u need. saying from manim import * will break the code, so u are not allowed to use asterisks in ur response. MaKE sure u have scene.render() at the end. Manim 0.10.0. Btw u cannot use self.time so find another way""" + """Here is an example of functioning manim 0.10.0 code:
            
or
from manim import *

class RotateSquareAroundCircle(Scene):
    def construct(self):
        # Create a square and a circle
        square = Square()
        circle = Circle()

        # Add the square and circle to the scene
        self.add(square, circle)

        # Define a parametric function to move the square around the circle
        def rotate_around_circle(t):
            circle_center = circle.get_center()
            circle_radius = circle.radius
            angle = t * TAU  # Using TAU for full rotation
            x = circle_center[0] + circle_radius * np.cos(angle)
            y = circle_center[1] + circle_radius * np.sin(angle)
            return [x, y, 0]

        # Move the square around the circle
        square.add_updater(lambda m, dt: m.move_to(rotate_around_circle(self.time)))
        
        # Wait for full rotation (optional)
        self.wait(2 * PI)

# Render the scene
scene = RotateSquareAroundCircle()
scene.render()


"""},   
            {"role": "user", "content": user_prompt}
        ]
    )


    # Extract the actual content generated by GPT-3.5 Turbo
    generated_message = completion.choices[0].message
    generated_message_object = ChatCompletionMessage(
        content=generated_message.content,
        role='assistant'  # Assuming the role is 'assistant'
    )

    # Print out the text that will be read
    text_content = generated_message_object.get_text_content()
    print(text_content)
    return text_content

def llm_call2(user_prompt):
    openai.api_key = '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'
    class ChatCompletionMessage:
        def __init__(self, content, role, function_call=None, tool_calls=None):
            self.content = content
            self.role = role
            self.function_call = function_call
            self.tool_calls = tool_calls

        def get_text_content(self):
            # Return only the text content
            return self.content
        # Initialize the OpenAI client
    client = openai.OpenAI()

    # Your code for interacting with the OpenAI API goes here
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Your job is to fix this ode for manim 0.10.0 and make it work perfectly. Ur response will be parsed as raw code so do not say anything else. make sure ur render is the same function as ur first scene. Note that the code must produce a vidfeo when executed, so do not hide the render in any function. The last 2 lines of the code should always be scene = ClassName() and scene.render(). Do not use ShowCreation. There is no Parabola command, generally u must make ur own using ParametricFunction. Do not use the BLUE constant, WHITE, or any other specifeid colors--let the default colors do their thing. Import numpy as np too. Do not use t_min. The ParametricFunction class is typically used to animate paths, not objects themselves. In this case, you're trying to rotate the square using Rotate, but passing a ParametricFunction as the path, which may not yield the desired result. Use t instead of self.time wheere applicable. Self check ur work by rubber duckying it to urself silently, remember u can only output raw code. The error TypeError: 'NoneType' object is not callable indicates that the rate_func parameter in the animation is set to None, causing a TypeError when trying to call it as a function. this, you need to provide a valid rate function to control the speed of the animation. You can use built-in rate functions such as linear, smooth, there_and_back, or define your own custom rate function. Use math.pi instead of Pi, import math first. Math is imported from pythons installed modules, not from manim. Or just use 3.1415926. U may not use t_min or t_max as do not exist in 0.10.0. Do not use Self.play(Create()) and do not use self.time use t instead or find another method.  Remove t_min and t_max from the code altogether."},
            {"role": "user", "content": user_prompt}
        ]
    )


    # Extract the actual content generated by GPT-3.5 Turbo
    generated_message = completion.choices[0].message
    generated_message_object = ChatCompletionMessage(
        content=generated_message.content,
        role='assistant'  # Assuming the role is 'assistant'
    )

    # Print out the text that will be read
    text_content = generated_message_object.get_text_content()
    print(text_content)
    class_name_line = text_content.split('\n')[-2]
    class_name = class_name_line.split('=')[-1].strip().split('(')[0].strip()

    return text_content, class_name 

def llm_call3(user_prompt):
    openai.api_key = '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'
    class ChatCompletionMessage:
        def __init__(self, content, role, function_call=None, tool_calls=None):
            self.content = content
            self.role = role
            self.function_call = function_call
            self.tool_calls = tool_calls

        def get_text_content(self):
            # Return only the text content
            return self.content
        # Initialize the OpenAI client
    client = openai.OpenAI()

    # Your code for interacting with the OpenAI API goes here
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ur job is to return a very direct description of what the user is talking about mathematically, specifically in terms of animation. U may not exlpain anything or provide any resources or code, u may only return one to two brief sentences that describe the mathematical event the uer is describing (without using any math symbols, so this is pronouncable). The intention here is to take a math teacher talking about something and return a direct command in natural language for a student or machine to animate that something."},
            {"role": "user", "content": user_prompt}
        ]
    )


    # Extract the actual content generated by GPT-3.5 Turbo
    generated_message = completion.choices[0].message
    generated_message_object = ChatCompletionMessage(
        content=generated_message.content,
        role='assistant'  # Assuming the role is 'assistant'
    )

    # Print out the text that will be read
    text_content = generated_message_object.get_text_content()
    print(text_content)

    return text_content

def llm_call_4(user_prompt):
    openai.api_key = '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'
    class ChatCompletionMessage:
        def __init__(self, content, role, function_call=None, tool_calls=None):
            self.content = content
            self.role = role
            self.function_call = function_call
            self.tool_calls = tool_calls

        def get_text_content(self):
            # Return only the text content
            return self.content
        # Initialize the OpenAI client
    client = openai.OpenAI()

    # Your code for interacting with the OpenAI API goes here
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Ur job is to make this code work on manim 0.10.0 by removing t_min and t_max from the equation and anything else that seems like it should be removed or reworked."""},
            {"role": "user", "content": user_prompt}
        ]
    )


    # Extract the actual content generated by GPT-3.5 Turbo
    generated_message = completion.choices[0].message
    generated_message_object = ChatCompletionMessage(
        content=generated_message.content,
        role='assistant'  # Assuming the role is 'assistant'
    )

    # Print out the text that will be read
    text_content = generated_message_object.get_text_content()
    print(text_content)

    return text_content
def record_audio(duration=6, fs=44100, filename='recorded_audio.wav'):
    print("Recording audio...")
    # Record audio for the specified duration and at the specified sampling frequency
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()  # Wait for recording to finish
    print("Recording finished.")

    # Save the recorded audio to a WAV file
    wav.write(filename, fs, audio_data)
    print(f"Audio saved as {filename}")

    return filename

# Example usage:
# record_audio()

def whisper(audio):

    client = OpenAI()

    audio_file= open(audio, "rb")
    transcription = client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file
    )
    return transcription.text 
def output_maker(code):
    import os
    import datetime

    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create the output directory if it doesn't exist
    output_folder = os.path.join('output', timestamp)
    os.makedirs(output_folder, exist_ok=True)

    # Define the file path
    file_path = os.path.join(output_folder, 'generated_code.py')

    # Write the variable to the file with timestamp
    with open(file_path, 'w') as file:
        # Indent the provided code properly
        file.write(code)

    print(f'Variable has been written to {file_path} with timestamp.')
    return file_path, output_folder


def main():
    while True:
        record_audio()
        math_prompt = whisper("recorded_audio.wav")
        with open(r'C:\Users\Rose-\Desktop\Projects\Current\ManimAI\AIactionslist\output_1.txt', 'r') as file:
            actions_list = file.read()
        manim_output, class_name = llm_call2(llm_call(actions_list,llm_call3(math_prompt)))
        manim_output, class_name = llm_call_4(manim_output)
        manim_output_stripped = manim_output.strip().strip('`').replace('python', '')

    # Assuming output_maker() function takes two arguments and returns file_path and output_folder
        file_path, output_folder = output_maker(manim_output_stripped)

        try:
            subprocess.run(['python', file_path])
            print("Subprocess executed successfully.")
        except Exception as e:
            print("Error executing subprocess:", e)

        # Play the generated video file
        video_file = os.path.join('media', 'videos', '1080p60.0', f'{class_name}.mp4')
        play_video(video_file)

        time.sleep(10)  
main()