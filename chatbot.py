# Import the necessary libraries
import streamlit as st
import random
import webbrowser
import time







st.set_page_config(menu_items=None,page_title="Inflow Chatbot", page_icon="path/to/your/favicon.ico", initial_sidebar_state="collapsed")


# with open('/style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    

# Define a class to hold the session state variables
class SessionState:
    
#    def cursorr(text):
       
#      cursor_char = "_"
#      text_placeholder = st.empty()

#      for char in text:
#         text_placeholder.text(char + cursor_char)
#         time.sleep(0.2)  # Adjust the sleep duration to control the typing speed

#      text_placeholder.text(text)
    def __init__(self):
        
        self.current_state = "start" 
        self.previous_state = "start" # Set the initial state to "start"
        # self.yesintstate = ""         # Initialize variables for different states
        # self.aboutusstate = ""
        # self.servstate = ""
        # self.lol = ""
        # self.contactus = ""
        # self.testgostate = ""
        # self.benefits = ""
        # self.whoisitfor = ""
        # self.isitaccurate = ""
        # self.benefits = ""
        
def greeting():
    if "state" not in st.session_state:   # Check if the session state has been initialized
        st.session_state.state = SessionState()   # Initialize the session state
    state = st.session_state.state        # Get the current state from the session state object
    
    greetings = ["Hello", "Hi", "Sup", "Hey there"]
    greeting_text = random.choice(greetings)
    
    greetingss = ["How can I assist you today?", "How can I help you today?", "What can i do for you today?", "Hope you are doing fine, How can i help u?"]
    greetings_text = random.choice(greetingss)
    
    st.title("Welcome to Inflow Chatbot!")
    st.write("I'm an ai model here to help you with whatever you need.")
    name = st.text_input("Before we get started, may I know your name?")
    if name:
        
        st.write(f"{greeting_text}, {name}!, {greetings_text}") 
        state.current_state = "yesintstate"       
        
        
# Define the main chat function
def chat():
      # Set the width and height of the chat panel
    panel_width = 600
    panel_height = 400

    # Calculate the necessary CSS styles
    css_code = f"""
        <style>
        /* Center the chat panel */
        .element-container:nth-child(1) {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 00vh;
        }}
        
        /* Set the panel width and height */
        .element-container:nth-child(1) .stApp {{
            width: {panel_width}px;
            height: {panel_height}px;
            overflow-y: auto;
        }}
        </style>
    """

    # Render the CSS code using st.markdown
    st.markdown(css_code, unsafe_allow_html=True)

    # JavaScript code to scroll to the bottom of the chat panel
    scroll_js = """
        <script>
        const chatPanel = document.querySelector(".element-container:nth-child(1) .stApp");
        chatPanel.scrollTop = chatPanel.scrollHeight;
        </script>
    """
    
    # st.title("Welcome to the Chatbot!")   # Set the title of the app
    if "state" not in st.session_state:   # Check if the session state has been initialized
        st.session_state.state = SessionState()   # Initialize the session state
    state = st.session_state.state        # Get the current state from the session state object
    if state.current_state == "start":    # If the current state is "start"
        if __name__ == "__main__":
            greeting()
        # st.write("Hey there, how can I help you? Are you interested to know more about our Website?? ")
            # if st.button("Yes am interested"):   # If the "Yes" button is clicked
            #     state.current_state = "yesintstate"   # Change the current state to "yesintstate"    
    if state.current_state == "yesintstate":   # If the current state is "yesintstate"
        st.write("<h5><b>Select one:</b></h5>" , unsafe_allow_html=True)
        if st.button(" About us "):         # If the "About us" button is clicked
            state.current_state = "aboutusstate"
            st.session_state.answer = "yes"# Change the current state to "aboutusstate"
        if st.button(" What is luscher color test ? "):   # If the "What we service" button is clicked
            state.current_state = "servstate"
            st.session_state.answer = "yes"# Change the current state to "servstate"
        if st.button("How to Make a Appointment"):                # If the "Test" button is clicked
            state.current_state = "howtomakeappo"
            # st.session_state.answer = "yes"# Change the current state to "lol"
        if st.button("Contact us"):                # If the "Test" button is clicked
            state.current_state = "contactus"
            # st.session_state.answer = "yes"   
    if state.current_state== "contactus":
        st.write("""
                 We value open communication and are readily available to address any questions, concerns, or inquiries you may have. Feel free to reach out to us through any of the following channels:

                1) WhatsApp: For quick and convenient communication, you can contact us via WhatsApp. Our dedicated WhatsApp number allows you to send messages, ask questions, and receive prompt responses from our team. We strive to provide excellent customer service and support through this channel.

                2) Instagram: Connect with us on Instagram, where we share valuable insights, updates, and information about the Luscher Color Test. Follow our official Instagram page to stay connected, engage in discussions, and reach out through direct messages. We value the vibrant Instagram community and are eager to engage with you there.

                3) Facebook: Join our Facebook community and stay informed about the latest developments in color psychology and the Luscher Color Test. Like our Facebook page to receive updates, participate in conversations, and send us direct messages with your inquiries or feedback. We are committed to fostering an interactive and supportive environment on Facebook.

                4) Email: If you prefer traditional email communication, you can send us a message at our designated email address. Whether you have detailed questions, partnership inquiries, or specific requests, our team will promptly respond to your email and provide the assistance you need.

                Please note that our contact channels are monitored during business hours, and we strive to respond to all inquiries as soon as possible. Depending on the nature of your query, it may be helpful to provide relevant details or context to ensure a more accurate and tailored response.

                Choose the contact channel that suits you best and reach out to us. We look forward to connecting with you and providing the support you need.

                 
                 
                 """)  
        if st.button("Contact Us Now"): 
            # If the "Yes" button is clicked
            webbrowser.open_new_tab("http://localhost:3000/contactus")
            
        if st.button("Return to main menu"): 
            
            state.current_state = "yesintstate"
    if state.current_state == "aboutusstate" :
        st.write("""
        Our mission is to provide a comprehensive understanding of the Luscher Color Test and its benefits to individuals seeking self-discovery, personal growth, and emotional well-being. We are dedicated to helping people explore the fascinating world of color psychology and leverage its power to gain valuable insights into their personality, emotions, and decision-making processes.

        Key information about us includes:

        1) Expertise and Experience:
        Our team consists of experienced psychologists, color psychology experts, and professionals well-versed in the Luscher Color Test. We have in-depth knowledge of color psychology theories, assessment techniques, and the practical application of the Luscher Color Test in various contexts.

        2) Client-Centered Approach:
        We prioritize the needs and well-being of our clients. Our services are designed to provide a supportive and empowering experience, enabling individuals to navigate their personal journeys of self-discovery and personal growth. We are committed to creating a safe and inclusive environment for everyone seeking our assistance.

        3)Comprehensive Resources and Information:
        We offer a wealth of resources and information about the Luscher Color Test. Our website, articles, and materials provide a comprehensive understanding of the test, its history, and the underlying principles of color psychology. We strive to present information in a clear, accessible manner to facilitate learning and engagement.

        4)Ethics and Confidentiality:
        Ethical principles guide our work. We uphold the importance of confidentiality, privacy, and the responsible use of the information shared with us. We respect the sensitive nature of the personal insights gained through the Luscher Color Test and ensure that client confidentiality is maintained at all times.

        5)Customized Services:
        We recognize that every individual is unique, and their journey of self-discovery is personal. As such, we offer customized services tailored to the specific needs and goals of our clients. Our range of services includes individual assessments, couple assessments, workshops, and guidance for personal and professional development.

        6)Continuous Support and Follow-up:
        Our commitment to our clients goes beyond the initial assessment. We provide ongoing support and follow-up to ensure that individuals can effectively apply the insights gained from the Luscher Color Test in their lives. We offer guidance, resources, and tools to facilitate personal growth and help individuals make meaningful changes.

        
        
        
            """)
        if st.button("Contact Us"): 
            # If the "Yes" button is clicked
            webbrowser.open_new_tab("http://localhost:3000/contactus")  # Change the current state to "testgostate"
        if st.button("Read More About us"): 
            
            webbrowser.open_new_tab("http://localhost:3000/")
            
        if st.button("Return to main menu"): 
            
            state.current_state = "yesintstate"
            
          
            
    if state.current_state == "howtomakeappo" :
        st.write("""
        Making an appointment with our company to take the Luscher Color Test is a simple process. We offer both offline and online meetings to accommodate your preferences and convenience. Follow the steps below to schedule your appointment:

        1) Select Appointment Type:
        Next, determine whether you prefer an offline or online meeting. Offline meetings require you to physically visit our location, while online meetings offer the convenience of remote communication via video conferencing. Consider your location, availability, and personal preferences when selecting the appointment type.

        
        2) Choose the Preferred Doctor:
        As a first step, you have the option to choose the doctor or practitioner you prefer. Each doctor has their own expertise and style, so selecting someone you feel comfortable with can enhance your experience. You can review their profiles or seek recommendations to make an informed decision.

       
        3) Offline Appointment:
        If you choose an offline appointment, you will need to select a suitable date and time from the available slots provided by the selected doctor. This can be done through our appointment booking system or by contacting our receptionist. They will assist you in finding an available slot that fits your schedule.

        4) Online Appointment:
        For online appointments, you can select a date and time that works best for you. Our appointment booking system will display the available slots for the chosen doctor, and you can easily book your preferred time. You will also receive instructions on how to connect for the online meeting.

        5) Payment and Confirmation:
        Once you have selected the doctor and appointment type, you will be directed to the payment form. Complete the payment process using the provided payment options. After the payment is successful, you will receive a confirmation email with the details of your appointment.

        6) Prepare for the Appointment:
        Before your appointment, make sure to familiarize yourself with any instructions or preparations provided by the doctor. This may include specific guidelines for offline meetings or technical requirements for online meetings. Being prepared will ensure a smooth and productive appointment.

        7) Confirmation and Reminders:
        As the appointment approaches, you will receive reminder emails or notifications to ensure you don't miss the scheduled time. These reminders will include any additional instructions or information you need to know before the appointment.

        8) Attend the Appointment:
        On the scheduled date and time, attend the appointment according to the chosen format. If it's an offline meeting, arrive at our location on time and check-in with our receptionist. For online meetings, follow the instructions provided to join the video conference at the scheduled time.
                
        
            """)  
        if st.button("Book Now"): 
            # If the "Yes" button is clicked
            webbrowser.open_new_tab("http://localhost:3000/bookmeeting")
            
        if st.button("Return to main menu"): 
            # If the "Yes" button is clicked
            state.current_state = "yesintstate"
                    
    if state.current_state == "servstate":
        # st.markdown("<h3 style='text-align: left; color: white;'>What is <b>Lüscher Color Test</b>?</h3>", unsafe_allow_html=True)# If the current state is "aboutusstate"
        st.write("""                 
                 It could seem a too simple and quick tool due to its immediacy and rapidity. However, the “Lüscher Color Test” (LCT) is a psychological test developed for psychiatrists and psychologists who deal with people’s conscious and unconscious characteristics and motivations.
                    It has gained popularity as a tool to identify the emotional and characterological features of personality and the subtle nuances of people current state. This is the reason why, nowadays, this tool is also used in the recruitment stage by some employers, in order to assess and evaluate candidates for certain positions.""")
        if st.button("Benefits of Luscher test"):
            state.current_state = "benefits"
        if st.button("Who is it for?"): 
            
            state.current_state = "whoisitfor"
        if st.button("Is it accurate?"):  
           
            state.current_state = "isitaccurate"
            
        # if st.button("Return to main menu"): 
            
        #     state.current_state = "yesintstate"
            
            
    if state.current_state == "benefits": 
        st.write("""
                     Exploring the psychological aspects of color, gaining insights into personality and emotions, and facilitating self-discovery and personal growth are some of the key benefits of the Luscher color test. Here's more information on each benefit:
                     
                 """)# If the "Test" button is clicked
        if st.button("Exploring the psychological aspects of color"):
            
            # st.write("""
            #          The Luscher color test allows individuals to delve into the fascinating world of color psychology. Colors have the power to evoke emotions, influence mood, and impact behavior. By understanding the psychological significance of different colors, individuals can gain insights into how color choices reflect their personality and emotional state.
                     
            #          """)
            
            state.current_state = "exploringbenefits"
        if st.button("Gaining insights into personality and emotions"): 
            #  st.write("""
            #          Through the Luscher color test, individuals can gain valuable insights into their own personality traits and emotional tendencies. The test analyzes color preferences and interpretations to reveal patterns and themes that provide a deeper understanding of one's self. It can uncover hidden aspects of one's personality and shed light on how emotions are expressed and experienced.
                     
            #          """)  
             state.current_state = "gainingbenefits"
        if st.button("Facilitating self-discovery and personal growth"):  
            # st.write("""
            #          The Luscher color test serves as a powerful tool for self-reflection and personal growth. By exploring one's color preferences and the associated interpretations, individuals can uncover new perspectives about themselves. This increased self-awareness can lead to personal insights, providing a starting point for personal growth, decision-making, and self-improvement.
                     
            #          """)
            state.current_state = "faciliatingbenefits"
        if st.button("Enhancing communication and relationships"):  
            # st.write("""
            #          Understanding the psychological effects of colors can also be beneficial for improving communication and relationships. By recognizing how different colors impact individuals differently, one can adapt their communication style to effectively connect with others. It can also help in understanding the emotions and preferences of loved ones, fostering better relationships and empathy.
                     
            #          """)
            state.current_state = "enhancebenefits"
            
        if st.button("Supporting creative expression and decision-making"):  
            # st.write("""
            #          The Luscher color test can spark creativity and aid in decision-making processes. Colors can evoke specific feelings and associations, enabling individuals to tap into their intuition and make choices that align with their emotions and values. It can be used as a tool to explore creative outlets and inspire innovative thinking.
            #          """)
            state.current_state = "supportbenefits"
            
            
        # if st.button("Return to main menu"): 
            
        #     state.current_state = "yesintstate" 
    
    
           
    if state.current_state == "exploringbenefits": 
        st.write("""
                     The Luscher color test allows individuals to delve into the fascinating world of color psychology. Colors have the power to evoke emotions, influence mood, and impact behavior. By understanding the psychological significance of different colors, individuals can gain insights into how color choices reflect their personality and emotional state.
                     
                     """)# If the "Test" button is clicked
        if st.button("How do colors influence our emotions and behaviors"):
            
            # st.write("""
            #           Colors have the ability to evoke specific emotions and impact our mood and behavior. For example, warm colors like red can evoke feelings of excitement or passion, while cool colors like blue can create a sense of calmness or serenity.
                      
            #          """)  
            
            state.current_state = "howcolors"
            
        if st.button("Can color preferences reveal insights about our personality?"):
            
            # st.write("""
            #          Yes, color preferences can provide clues about our personality traits and characteristics. For instance, someone who prefers vibrant and bold colors may be more extroverted and energetic, while those who gravitate towards softer and muted tones may have a more introverted or reserved nature.
                     
                     
            #          """)  
            
            state.current_state = "cancolors"  
            
        if st.button("What are some examples of color symbolism in psychology?"):
            
            # st.write("""
                     
            #           Color symbolism can vary across cultures, but certain associations are widely recognized. For instance, red is often associated with passion, power, or danger, while blue is commonly associated with tranquility, trust, or sadness. Understanding these symbolic meanings can help interpret the psychological impact of colors.
                      
                      
            #          """)  
            
            state.current_state = "someexamples"
            
        # if st.button("Return to main menu"): 
            
        #     state.current_state = "yesintstate" 
            
            
    if state.current_state == "howcolors":
        st.write("""
                      Colors have the ability to evoke specific emotions and impact our mood and behavior. For example, warm colors like red can evoke feelings of excitement or passion, while cool colors like blue can create a sense of calmness or serenity.
                      
                     """)  
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
    if state.current_state == "cancolors":
        st.write("""
                     Yes, color preferences can provide clues about our personality traits and characteristics. For instance, someone who prefers vibrant and bold colors may be more extroverted and energetic, while those who gravitate towards softer and muted tones may have a more introverted or reserved nature.
                     
                     
                     """) 
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
    if state.current_state == "someexamples":
        st.write("""
                     
                      Color symbolism can vary across cultures, but certain associations are widely recognized. For instance, red is often associated with passion, power, or danger, while blue is commonly associated with tranquility, trust, or sadness. Understanding these symbolic meanings can help interpret the psychological impact of colors.
                      
                      
                     """)  
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")  # lolllllllllllllllllllllllllll
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
            
    if state.current_state == "gainingbenefits": 
        st.write("""
                     Through the Luscher color test, individuals can gain valuable insights into their own personality traits and emotional tendencies. The test analyzes color preferences and interpretations to reveal patterns and themes that provide a deeper understanding of one's self. It can uncover hidden aspects of one's personality and shed light on how emotions are expressed and experienced.
                     
                     """)  
        if st.button("How does the Luscher color test analyze color preferences?"):
            
            # st.write("""
            #           Colors have the ability to evoke specific emotions and impact our mood and behavior. For example, warm colors like red can evoke feelings of excitement or passion, while cool colors like blue can create a sense of calmness or serenity.
                      
            #          """)  
            
            state.current_state = "howdoesluscher"
            
        if st.button("What patterns or themes can be identified through color interpretations?"):
            
            # st.write("""
            #          Yes, color preferences can provide clues about our personality traits and characteristics. For instance, someone who prefers vibrant and bold colors may be more extroverted and energetic, while those who gravitate towards softer and muted tones may have a more introverted or reserved nature.
                     
                     
            #          """)  
            
            state.current_state = "whatpatterns"  
            
        if st.button("In what ways can understanding our emotional tendencies be beneficial?"):
            
            # st.write("""
                     
            #           Color symbolism can vary across cultures, but certain associations are widely recognized. For instance, red is often associated with passion, power, or danger, while blue is commonly associated with tranquility, trust, or sadness. Understanding these symbolic meanings can help interpret the psychological impact of colors.
                      
                      
            #          """)  
            
            state.current_state = "inwhatways"
            
        # if st.button("Return to main menu"): 
            
        #     state.current_state = "yesintstate"
            
            
            
            
    if state.current_state == "howdoesluscher":
        st.write("""
                      The Luscher color test presents individuals with a series of color choices and asks them to select the colors they are most and least drawn to. These color preferences are then analyzed based on the Luscher color theory, which assigns specific psychological interpretations to different color combinations and choices.
                      
                      
                     """)  
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
    if state.current_state == "whatpatterns":
        st.write("""
                     By examining the patterns and themes in an individual's color preferences, the Luscher color test can reveal underlying aspects of their personality and emotional tendencies. For example, consistent preferences for bold and vibrant colors may suggest an outgoing and adventurous nature, while a preference for earthy tones may indicate a grounded and practical personality.
                     
                     """) 
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
    if state.current_state == "inwhatways":
        st.write("""
                     
                     Understanding our emotional tendencies can provide insights into how we experience and express emotions. It can help us become more self-aware, allowing us to better manage our emotions, make informed decisions, and improve our overall well-being.
                     
                      
                     """)  
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")  # heheheeeeeeeeeeeeee
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
    if state.current_state == "faciliatingbenefits": 
        st.write("""
                     The Luscher color test serves as a powerful tool for self-reflection and personal growth. By exploring one's color preferences and the associated interpretations, individuals can uncover new perspectives about themselves. This increased self-awareness can lead to personal insights, providing a starting point for personal growth, decision-making, and self-improvement.
                     
                     """)
        if st.button("How can the Luscher color test help in self-reflection?"):
            
            # st.write("""
            #           Colors have the ability to evoke specific emotions and impact our mood and behavior. For example, warm colors like red can evoke feelings of excitement or passion, while cool colors like blue can create a sense of calmness or serenity.
                      
            #          """)  
            
            state.current_state = "testhelp"
            
        if st.button("What are some practical steps to take after receiving test results?"):
            
            # st.write("""
            #          Yes, color preferences can provide clues about our personality traits and characteristics. For instance, someone who prefers vibrant and bold colors may be more extroverted and energetic, while those who gravitate towards softer and muted tones may have a more introverted or reserved nature.
                     
                     
            #          """)  
            
            state.current_state = "practicalsteps"  
            
        if st.button("Can the test assist in identifying areas for personal development?"):
            
            # st.write("""
                     
            #           Color symbolism can vary across cultures, but certain associations are widely recognized. For instance, red is often associated with passion, power, or danger, while blue is commonly associated with tranquility, trust, or sadness. Understanding these symbolic meanings can help interpret the psychological impact of colors.
                      
                      
            #          """)  
            
            state.current_state = "testassist"
            
        # if st.button("Return to main menu"): 
            
        #     state.current_state = "yesintstate" 
            
        # if st.button("Return to main menu"): 
            
        #     state.current_state = "yesintstate"
            
            
            
            
            
    if state.current_state == "testhelp":
        st.write("""
                      The Luscher color test prompts individuals to reflect on their color choices and interpretations, which can lead to a deeper understanding of themselves. It encourages introspection, allowing individuals to explore their preferences, values, and emotional responses associated with different colors.
                      
                     """)  
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
    if state.current_state == "practicalsteps":
        st.write("""
                     After receiving test results, individuals can engage in self-reflection and introspection. They can explore the provided interpretations, identify any patterns or themes that resonate with them, and consider how this newfound self-awareness can be applied to personal growth, decision-making, and self-improvement.
                     
                     
                     """) 
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
            
    if state.current_state == "testassist":
        st.write("""
                     
                     Yes, the Luscher color test can highlight areas for personal development by revealing certain personality traits or emotional tendencies. For example, if the test indicates a preference for colors associated with stress or anxiety, it can serve as a signal to focus on stress management techniques or seek professional support if necessary.
                     
                      
                     """)  
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")  # weweeweweweweweeeeeeeeeeeeeeeeeeeeee
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
            
                                       
    if state.current_state == "enhancebenefits": 
        st.write("""
                     Understanding the psychological effects of colors can also be beneficial for improving communication and relationships. By recognizing how different colors impact individuals differently, one can adapt their communication style to effectively connect with others. It can also help in understanding the emotions and preferences of loved ones, fostering better relationships and empathy.
                     
                     """)
        if st.button("How can understanding color psychology improve communication?"):
            
            # st.write("""
            #           Colors have the ability to evoke specific emotions and impact our mood and behavior. For example, warm colors like red can evoke feelings of excitement or passion, while cool colors like blue can create a sense of calmness or serenity.
                      
            #          """)  
            
            state.current_state = "understandcolor"
            
        if st.button("What role does empathy play in building better relationships?"):
            
            # st.write("""
            #          Yes, color preferences can provide clues about our personality traits and characteristics. For instance, someone who prefers vibrant and bold colors may be more extroverted and energetic, while those who gravitate towards softer and muted tones may have a more introverted or reserved nature.
                     
                     
            #          """)  
            
            state.current_state = "empathyplay"  
            
        if st.button("Are there any tips for effectively utilizing color knowledge in social interactions?"):
            
            # st.write("""
                     
            #           Color symbolism can vary across cultures, but certain associations are widely recognized. For instance, red is often associated with passion, power, or danger, while blue is commonly associated with tranquility, trust, or sadness. Understanding these symbolic meanings can help interpret the psychological impact of colors.
                      
                      
            #          """)  
            
            state.current_state = "tipscolor"
            
        # if st.button("Return to main menu"): 
            
        #     state.current_state = "yesintstate"
            
            
            
            
    if state.current_state == "understandcolor":
        st.write("""
                      Understanding color psychology can enhance communication by allowing individuals to consider how different colors may impact others. It enables us to adapt our communication style, environment, or visual aids to create a more conducive and effective interaction based on the emotional associations colors evoke.
                      
                      
                     """)  
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
    if state.current_state == "empathyplay":
        st.write("""
                     Empathy plays a crucial role in building better relationships. Understanding color psychology can help develop empathy by providing insights into how color preferences may reflect someone's emotional state or personality. This understanding allows for more empathetic connections, as we can better appreciate and respond to others' emotional experiences.
                     
                     """) 
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
            
    if state.current_state == "tipscolor":
        st.write("""
                     
                     When utilizing color knowledge in social interactions, it's important to consider individual differences and cultural context. Pay attention to non-verbal cues, be open to dialogue, and seek to understand the personal meaning and associations individuals have with different colors.
                     
                      
                     """)  
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")  # kokokokooooooooooooooo
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
            
    if state.current_state == "supportbenefits": 
        st.write("""
                     The Luscher color test can spark creativity and aid in decision-making processes. Colors can evoke specific feelings and associations, enabling individuals to tap into their intuition and make choices that align with their emotions and values. It can be used as a tool to explore creative outlets and inspire innovative thinking.
                     """)
        
        
        if st.button("How can colors inspire creative thinking and expression?"):
            
            # st.write("""
            #           Colors have the ability to evoke specific emotions and impact our mood and behavior. For example, warm colors like red can evoke feelings of excitement or passion, while cool colors like blue can create a sense of calmness or serenity.
                      
            #          """)  
            
            state.current_state = "colorsinspire"
            
        if st.button("Are there any notable examples of color influence in decision-making?"):
            
            # st.write("""
            #          Yes, color preferences can provide clues about our personality traits and characteristics. For instance, someone who prefers vibrant and bold colors may be more extroverted and energetic, while those who gravitate towards softer and muted tones may have a more introverted or reserved nature.
                     
                     
            #          """)  
            
            state.current_state = "notableexamples"  
            
        if st.button("Can the Luscher color test help in aligning choices with personal values?"):
            
            # st.write("""
                     
            #           Color symbolism can vary across cultures, but certain associations are widely recognized. For instance, red is often associated with passion, power, or danger, while blue is commonly associated with tranquility, trust, or sadness. Understanding these symbolic meanings can help interpret the psychological impact of colors.
                      
                      
            #          """)  
            
            state.current_state = "canhelp?"
            
        # if st.button("Return to main menu"): 
            
        #     state.current_state = "yesintstate"
            
            
            
            
            
            
    if state.current_state == "colorsinspire":
        st.write("""
                      Colors can stimulate creativity by evoking emotions, setting a specific mood, or creating visual interest. They can inspire new ideas, stimulate imagination, and influence artistic expression across various mediums such as visual arts, design, and marketing.
                      
                      
                     """)  
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
    if state.current_state == "notableexamples":
        st.write("""
                     Color can influence decision-making processes by invoking certain psychological responses. For instance, businesses often use specific colors in branding or marketing to elicit desired consumer behaviors or convey brand values. Understanding color psychology can help individuals make decisions that align with their emotions, values, and intentions.
                     
                     
                     """) 
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
            
    if state.current_state == "canhelp?":
        st.write("""
                     
                     Yes, the Luscher color test can provide individuals with insights into their color preferences, which can guide them in aligning choices with their personal values. By understanding the emotional associations of colors, individuals can make conscious decisions that resonate with their authentic selves.
                     
                      
                     """)  
        st.write("Ok you are now Ready for test would u like to try??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")  # ba77777777777
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
                                     
    if state.current_state == "whoisitfor": 
        st.write("""
                 
                   The Luscher Color Test is designed to cater to the needs of adults, children over 5 years old, and couples. It offers distinct services tailored to each group, providing valuable insights into their personality, emotions, and relationships.

                    Adult Service:
                    The adult service of the Luscher Color Test is specifically designed for individuals seeking self-awareness, personal growth, and decision-making support. It offers a comprehensive exploration of color preferences, interpretations, and emotional associations, helping individuals gain insights into their personality traits, emotional tendencies, and decision-making processes. By understanding their unique color choices, adults can make more informed decisions, enhance self-awareness, and foster personal growth.

                    Couple Service:
                    The couple service of the Luscher Color Test aims to strengthen and deepen relationships by providing couples with a shared experience and a tool for better understanding each other's emotional responses and preferences. Through the test, couples can explore their individual color choices, interpretations, and emotional associations. This exploration can foster empathy, improve communication, and enhance their emotional connection. By gaining insights into each other's color preferences, couples can create a more harmonious and supportive relationship.

                    Children Over 5 Service:
                    The Luscher Color Test also offers a service specifically designed for children over 5 years old. This service provides a child-friendly and age-appropriate approach to exploring color preferences and emotional responses. By engaging children in the world of colors, the test helps them understand and express their emotions, encourages self-reflection, and supports their personal development. It can be a valuable tool for parents, educators, and therapists in helping children navigate their emotions and enhance their self-awareness.

                    To learn more about each service, you can select one of the options below:


                 """)
        if st.button("Read more about the Adult Service"):
            
            
            state.current_state = "adultservice"
            
        if st.button("Read more about the Couple Service"):
            
                
            state.current_state = "coupleservice"  
            
        if st.button("Read more about the Child Service"):
            
          
            
            state.current_state = "childservice"
            
        # if st.button("Return to main menu"): 
            
        #     state.current_state = "yesintstate"
            
            
            
            
            
    if state.current_state == "adultservice":
        st.write("""
                    The Adult Service of the Luscher Color Test is designed to provide adults with valuable insights into their personality, emotions, and decision-making processes. By exploring their color preferences, interpretations, and emotional associations, individuals can gain a deeper understanding of themselves and make more informed choices.

                    The Adult Service includes:

                    Comprehensive Color Assessment: Participants are presented with a series of color choices and asked to interpret their emotional responses to each color. This assessment provides a detailed analysis of the participant's color preferences and the underlying psychological meanings associated with those choices.

                    Personality Profiling: Based on the color preferences and interpretations, the Luscher Color Test generates a personalized profile that highlights the individual's personality traits, emotional tendencies, and areas of strength or growth. This profile can serve as a powerful tool for self-reflection, personal growth, and decision-making.

                    Emotional Insights: The test also provides insights into the participant's emotional responses to different colors. It helps individuals understand how specific colors may evoke certain emotions and how those emotions can influence their behavior and well-being. This knowledge can be applied in various areas of life, such as managing stress, improving relationships, and enhancing overall emotional well-being.

                    Decision-Making Guidance: By considering the emotional associations of colors and the participant's interpretations, the Luscher Color Test offers guidance in the decision-making process. It helps individuals align their choices with their authentic selves, values, and emotions, leading to more satisfying and fulfilling outcomes.
                                        
                     """)  
        st.write("Would u like to try the Test Now??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
            
    if state.current_state == "coupleservice":
        st.write("""
                    The Couple Service of the Luscher Color Test is designed to strengthen and deepen relationships by providing couples with a shared experience and a tool for better understanding each other's emotional responses and preferences.

                    The Couple Service includes:

                    Joint Color Assessment: Both partners participate in a shared color assessment, where they express their individual color preferences and interpretations. This assessment allows couples to explore and discuss their emotional responses to different colors, facilitating mutual understanding and empathy.

                    Relationship Insights: The Luscher Color Test provides insights into the dynamics of the couple's relationship based on their color choices and interpretations. It highlights areas of compatibility, potential sources of conflict, and opportunities for growth. This understanding can foster more effective communication, strengthen emotional bonds, and enhance overall relationship satisfaction.

                    Emotional Connection: By gaining insights into each other's color preferences and emotional associations, couples can deepen their emotional connection. They can better understand how specific colors may evoke different emotions in their partner and learn to respond in a supportive and empathetic manner. This promotes a more harmonious and fulfilling relationship.

                    Shared Decision-Making: The Luscher Color Test can also assist couples in making joint decisions. By considering the emotional significance of colors and their interpretations, couples can align their choices with their shared values, desires, and aspirations. This collaborative decision-making process can enhance mutual understanding, reduce conflicts, and strengthen the bond between partners.
                                        
                     """) 
        st.write("Would u like to try Test Now??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
            
            
    if state.current_state == "childservice":
        st.write("""
                     
                    The Luscher Color Test offers a service specifically designed for children over 5 years old. This service provides a child-friendly and age-appropriate approach to exploring color preferences and emotional responses.

                    The Children Over 5 Service includes:

                    Engaging Color Activities: The Luscher Color Test for children includes interactive and engaging color activities that make the experience enjoyable and accessible to young minds. These activities may involve selecting colors, drawing, or expressing emotions through colors, allowing children to explore and express their emotions in a creative and age-appropriate manner.

                    Emotional Awareness: Through the color activities, children develop an increased awareness of their emotions and learn to recognize and express them through color choices. This helps children develop emotional intelligence and self-awareness, which are essential skills for their overall well-being and social development.

                    Self-Expression and Communication: The Luscher Color Test encourages children to express their thoughts, feelings, and experiences through colors. This process enhances their ability to communicate their emotions effectively, promoting healthy self-expression and facilitating better communication with parents, teachers, and peers.

                    Support for Parents and Educators: The Children Over 5 Service provides valuable insights for parents and educators into children's emotional responses and preferences. This knowledge can help them understand and support children's emotional well-being, tailor educational approaches, and create a nurturing environment that fosters children's holistic development.

                      
                     """)  
        st.write("Would u like to try Test Now??") 
        if st.button("yes"):
            webbrowser.open_new_tab("http://localhost:3000/test-information")  # ba77777777777
        if st.button("Return to main menu"):
            state.current_state = "yesintstate"
            
            
            
                         
                   
    if state.current_state == "isitaccurate": 
        st.write("""
                    
                    The accuracy of the Luscher Color Test is an important consideration for individuals seeking to gain insights into their personality and emotions. While the test provides valuable information, it's essential to understand its limitations and the factors that can influence its accuracy. Here are some key points to consider:

                    Psychological Assessment Tool: The Luscher Color Test is primarily designed as a psychological assessment tool rather than a diagnostic instrument. It offers a unique approach to understanding one's emotional responses and personality traits through color preferences and interpretations.

                    Subjectivity and Individual Differences: It's important to recognize that the Luscher Color Test relies on subjective interpretations and individual differences in perceiving and responding to colors. Results can vary depending on personal experiences, cultural background, and individual associations with specific colors.

                    Self-Reflection and Insight: The accuracy of the Luscher Color Test lies in the insights and self-reflection it promotes. It serves as a catalyst for introspection and personal exploration, allowing individuals to gain a deeper understanding of their own emotions, behaviors, and decision-making processes. The value of the test lies in the personal meaning and significance individuals attribute to their color choices.

                    Supportive Tool, Not Definitive Diagnosis: The Luscher Color Test should be seen as a supportive tool rather than a definitive diagnosis of one's personality or emotional state. It provides a starting point for self-awareness, personal growth, and decision-making, but should not replace professional advice or evaluation by qualified psychologists or therapists.

                    Integration with Other Assessment Methods: For a more comprehensive understanding, the Luscher Color Test can be integrated with other psychological assessment methods, such as interviews, questionnaires, and clinical evaluations. This multi-modal approach enhances the accuracy and validity of the overall assessment.

                    Context and Interpretation: The accuracy of the Luscher Color Test also depends on the context in which it is administered and the interpretation of the results. Professional guidance and expertise in interpreting the test outcomes can ensure a more accurate understanding of the individual's psychological profile.

                    
                    
                    
                    
                 """)# If the "Test" button is clicked
        st.write("Would u like to Try test Now?")
        if st.button("yes"):
         webbrowser.open_new_tab("http://localhost:3000/test-information")
        if st.button("Return to main menu"): 
            
            state.current_state = state.previous_state
                        
            
        
    # st.write(state.current_state)    # Display the current state
    
    
    
 # Scroll to the bottom of the chat panel using JavaScript
    st.markdown(scroll_js, unsafe_allow_html=True)
# Call the chat function to start the app
chat()                          
   