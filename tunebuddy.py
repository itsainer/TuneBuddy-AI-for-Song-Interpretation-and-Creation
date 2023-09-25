
#%%
import os
import openai
import streamlit as st
#from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from streamlit_option_menu import option_menu
# %%
#load_dotenv()
openai_api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = openai_api_key
# %%
example1 = """
Summarize the meaning of 'Perfect' song by Ed Sheeran in 50 words length.
"""

answer1 = """
"Perfect" by Ed Sheeran:
A romantic song that celebrates the beauty of love. It describes a perfect moment between two people in a relationship, highlighting their deep connection and the idea that they are meant to be together. The song exudes warmth, affection, and a sense of completeness in love.
"""

example2 = """
Interpret line-by-line for the meaning of 'Perfect' song by Ed Sheeran. Do this for chorus part only.
"""

answer2 = """
Certainly, let's break down the meaning of the chorus of "Perfect" by Ed Sheeran line by line:

1. "Baby, I'm dancing in the dark": This line suggests a sense of spontaneity and joy, as if the speaker and their partner are dancing together in a dimly lit room. It symbolizes the intimacy and closeness they share.

2. "With you between my arms": The speaker cherishes the feeling of holding their loved one close, signifying a strong emotional connection and a desire for physical closeness.

3. "Barefoot on the grass": Being barefoot on the grass implies a carefree, natural, and unguarded state. It reflects the simplicity and purity of their love, free from pretenses.

4. "Listening to our favorite song": This line emphasizes the personal and intimate nature of their relationship, as they share a special song that holds significance for both of them.

5. "When you said you looked a mess": The speaker finds their partner beautiful even in moments of vulnerability, highlighting unconditional love and acceptance.

6. "I whispered underneath my breath": This suggests a secret or private declaration of love, a heartfelt sentiment not meant for anyone else to hear.

7. "But you heard it, darling, you look perfect tonight": Despite the quiet and private nature of the speaker's words, their partner hears and understands the depth of their affection, feeling cherished and loved in that moment.

Overall, the chorus of "Perfect" conveys a deep and heartfelt connection between two people who find beauty, joy, and perfection in each other's presence.
"""

example3 = """
I want to compose a song about family love in 2 paragraphs, nostalgic-tone. Help me to enhance my existing lyrics:
In our family's embrace, 
love's warmth fills every space, 
a bond that time can't erase, 
our hearts forever interlace.
"""

answer3 = """
Certainly, here's an enhanced version of your lyrics:

"In our family's warm embrace,
Love's tender touch, a timeless grace,
Through all life's trials we'll face,
Our hearts forever find their place.

In the stories of our past,
Nostalgia's sweet, gentle cast,
Memories cherished, built to last,
In family's love, we're steadfast."

These lines aim to evoke a stronger sense of nostalgia and the enduring nature of family love. Feel free to adapt them as needed for your song.
"""

example4 = """
Write me 50-words lyrics in Bahasa about the journey of two people finding harmony in their relationship. Describe the ups and downs, the compromises made.
"""

answer4 = """
TAJUK: ABADI
Dalam perjalanan cinta, berdua kita melewati berliku,
Terjalin harmoni di antara senyum dan tangis,
dengan cinta yang mengukuhkan,

Saat badai datang, kita temukan kedamaian di pelukan,
Kompromi dan pengertian mengukir kisah kita,
Dalam perbedaan, kita menemukan keutuhan,
Bersama, kita menari dalam harmoni, cinta yang abadi.
"""
#%%
def generate_pdf(lyrics):
    # Create a PDF canvas
    c = canvas.Canvas("new_lyrics.pdf", pagesize=letter)

    # Define font and font size
    c.setFont("Helvetica", 12)

    # Write the lyrics content to the PDF
    c.drawString(100, 650, "Generated Lyrics:")
    y_position = 620  # Initial Y position for lyrics
    for line in lyrics.split('\n'):
        c.drawString(100, y_position, line)
        y_position -= 20  # Adjust the Y position for the next line

    # Save the PDF
    c.save()
#%%
#Create a request to ChatCompletion endpoint
def tunebuddy(text_input):
  tb_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You excel as a premier song analyst, adept at succinctly summarizing song meanings, meticulously interpreting lyrics line by line, elevating users' existing lyrics, and ingeniously generating fresh lyrics and suggesting a song title from their unique descriptions."
      },
      {
        "role": "user",
        "content": example1
      },
      {
          "role":"assistant",       
          "content": answer1
      },
      {
        "role": "user",
        "content": example2
      },
      {
          "role":"assistant",       
          "content": answer2
      },
      {
        "role": "user",
        "content": example3
      },
      {
          "role":"assistant",       
          "content": answer3
      },
      {
        "role": "user",
        "content": example4
      },
      {
          "role":"assistant",       
          "content": answer4
      },
      {
          "role":"user",
          "content": text_input
      }
    ],
    temperature=0.5,
    max_tokens=1000,
  )

  return tb_response.choices[0].message.content


#%%
def homepage():
    header = st.container()
    description = st.container()
    
    #background
    bg_pic = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/v1059-037e-x.jpg?w=1200&h=1200&dpr=1&fit=clip&crop=default&fm=jpg&q=75&vib=3&con=3&usm=15&cs=srgb&bg=F4F4F3&ixlib=js-2.2.1&s=93ad94c303f396b12a568da0d93af606");
    background-size: cover;
    background-repeat: no-repeat;
    }
    </style>

    <style>
    [data-testid="stHeader"] {
    background-image: url("https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/v1059-037e-x.jpg?w=1200&h=1200&dpr=1&fit=clip&crop=default&fm=jpg&q=75&vib=3&con=3&usm=15&cs=srgb&bg=F4F4F3&ixlib=js-2.2.1&s=93ad94c303f396b12a568da0d93af606");
    background-size: cover;
    background-repeat: no-repeat;
    }
    </style>
    """
    st.markdown(bg_pic, unsafe_allow_html=True)
    
    h1_style = """
    <style>
        .app-title {
            font-size: 60px;
            font-family: 'Roboto', sans-serif;
            text-align: center;
            color: #2B3A67;
            margin-top: 150px;
            margin-bottom: 20px;
            white-space: nowrap;
        }
    </style>
    """
    h2_style = """
    <style>
        .subh-title {
            font-size: 35px;
            font-family: 'Roboto', sans-serif;
            text-align: justify;
            color: #2B3A67;
        }
    </style>
    """
    #header
    with header:
       st.markdown(h1_style, unsafe_allow_html=True)
       st.markdown("""<h1 class="app-title"><strong>Get tuned in with TuneBuddy!</strong></h1>""", unsafe_allow_html=True)
    
    #subheader
    with description:
       st.markdown(h2_style, unsafe_allow_html=True)
       st.markdown("""<h2 class="subh-title">Let AI summarize song meanings, interpret lyrics line-by-line, enhance and even generate new lyrics for you!</h2>""", unsafe_allow_html=True)

#%%
def summarize_page():
   
   s1_style = """
    <style>
        .title {
            font-size: 50px;
            font-family: 'Roboto', sans-serif;
            text-align: center;
            color: #2B3A67;
            margin-bottom: 20px;
        }
    </style>
    """
   st.markdown(s1_style, unsafe_allow_html=True)
   st.markdown("""<h1 class="title"><strong>Let TuneBuddy summarizes song for you!</strong></h1>""", unsafe_allow_html=True)
 
   col1, col2 = st.columns(2, gap="large")
   answer = " "

   with col1:
    with st.form('input_form'):
        song_title = st.text_input("Enter title of song:")
        singer = st.text_input("Enter name of singer:")
        st.markdown("Specify your output:")
        language = st.text_input("Language:")
        word_len = st.slider("Length of words:", 1,300,1)
        submit = st.form_submit_button('Submit')

   user_input = f'Summarize {song_title} by {singer} in {language} and {word_len} length of words'

   if submit:
    answer = tunebuddy(user_input)
       
   with col2:
      if answer is not None:
         st.text_area("TuneBuddy interprets this for you:", answer, height= 350)
#%%
def interpret_page():
   
   s1_style = """
    <style>
        .title {
            font-size: 50px;
            font-family: 'Roboto', sans-serif;
            text-align: center;
            color: #2B3A67;
            margin-bottom: 20px;
        }
    </style>
    """
   st.markdown(s1_style, unsafe_allow_html=True)
   st.markdown("""<h1 class="title"><strong>Let TuneBuddy interprets any line of song for you!</strong></h1>""", unsafe_allow_html=True)
   
   col1, col2 = st.columns(2, gap="large")
   answer = " "

   with col1:
    with st.form('input_form'):
        song_title = st.text_input("Enter title of song:")
        singer = st.text_input("Enter name of singer:")
        line = st.text_input("Which line? e.g. chorus, 7-8")
        st.markdown("Specify your output:")
        language = st.text_input("Language:")
        word_len = st.slider("Length of words:", 1,300,1)
        submit = st.form_submit_button('Submit')

    user_input = f'Interpret {song_title} by {singer} at line {line} in {language} and {word_len} length of words'

    if submit:
        answer = tunebuddy(user_input)
  
   with col2:
      if answer is not None:
         st.text_area("TuneBuddy interprets this for you:", answer, height= 350)
#%%
def enhance_page():
   
   s1_style = """
    <style>
        .title {
            font-size: 50px;
            font-family: 'Roboto', sans-serif;
            text-align: center;
            color: #2B3A67;
            margin-bottom: 20px;
        }
    </style>
    """
   st.markdown(s1_style, unsafe_allow_html=True)
   st.markdown("""<h1 class="title"><strong>Let TuneBuddy uplifts your original lyrics!</strong></h1>""", unsafe_allow_html=True)
   col1, col2 = st.columns(2, gap="large")
   answer = " "

   with col1:
    with st.form('input_form'):
        song_lyric = st.text_input("Enter your existing lyrics:")
        st.markdown("Specify your output:")
        language = st.text_input("Language:")
        word_len = st.slider("Length of words:", 1,300,1)
        submit = st.form_submit_button('Submit')

    user_input = f'Enhance my lyrics {song_lyric} and make it into {language} and {word_len} length of words'

    if submit:
        answer = tunebuddy(user_input)
  
   with col2:
      if answer is not None:
         st.text_area("TuneBuddy improves your lyrics:", answer, height= 350)
#%%
def generate_new_page():
   
   s1_style = """
    <style>
        .title {
            font-size: 50px;
            font-family: 'Roboto', sans-serif;
            text-align: center;
            color: #2B3A67;
            margin-bottom: 20px;
        }
    </style>
    """
   st.markdown(s1_style, unsafe_allow_html=True)
   st.markdown("""<h1 class="title"><strong>Let TuneBuddy generates lyrics for your new song!</strong></h1>""", unsafe_allow_html=True)
   col1, col2 = st.columns(2, gap="large")
   answer = " "
   pdf_gen = False

   with col1:
    with st.form('input_form'):
        song_info = st.text_input("Describe what type of song (theme):")
        st.markdown("Specify your output:")
        language = st.text_input("Language:")
        word_len = st.slider("Length of words:", 1,300,1)
        tone_options = ["Happy", "Sad", "Relaxed", "Angry", "Romantic", "Excited"]
        tone = st.selectbox("Tone:", tone_options)
        submit = st.form_submit_button('Submit')

    user_input = f'Generate me a song about {song_info} with {tone} tone and make it into {language} and {word_len} length of words'

    if submit:
        answer = tunebuddy(user_input)
        pdf_gen = True

    with col2:
        if answer is not None:
            result = st.text_area("TuneBuddy creates a song for you:", answer, height=350)

            if pdf_gen:  # Check if the PDF should be generated and displayed
                generate_pdf(result)
                st.download_button(
                    "Download PDF",
                    "new_lyrics.pdf",
                    key="download-pdf-button",
                    help="Click to download the generated lyrics as a PDF."
                )
#%%
def main():
    st.set_page_config(
       page_title="TuneBuddy",
       page_icon=":musical_score:",
    )
    
    #sidebar
    sb_style = """
    <style>
        .sidebar-title {
            font-size: 24px;
            font-family: 'Baskerville', sans-serif;
            text-align: center;
            color: #2B3A67;
        }
    </style>
    """
    st.sidebar.markdown(sb_style, unsafe_allow_html=True)
    st.sidebar.markdown('<span class="sidebar-title"><strong>Explore TuneBuddy! 🤖</strong></span>', unsafe_allow_html=True)

    page_functions = {
       "Home": homepage,
       "Summarize song": summarize_page,
       "Interpret line-by-line": interpret_page,
       "Enhance original lyrics": enhance_page,
       "Generate new song": generate_new_page
    }

    with st.sidebar:
        selected_page = option_menu(menu_title="Choose task", options=list(page_functions.keys()), icons=['house', 'headphones','headphones','headphones','headphones'], default_index=0)

    if selected_page in page_functions:
       page_functions[selected_page]()
# %%
if __name__ == "__main__":
    main()
# %%
