import streamlit as st
import base64

def enter_key_widget():
    st.set_page_config(page_title="Testplan Generator powered by Gemini Pro",page_icon="📝")
    st.write("Welcome to the Test Plan Generator. You can proceed by providing your Google API Key")
    with st.expander("Provide Your Google API Key or Type No"):
        google_api_key = st.text_input("Google API Key", key="google_api_key", type="password")
        
    st.divider()
    if "No" in google_api_key :
        return st.secrets["API_KEY"]
        
    if not google_api_key:
        st.info("Enter your Google API Key or Type No")
        st.stop()
        
    return google_api_key

def check_values(input_text, uploaded_file):
    if not input_text:
        raise ValueError("Input text is empty. Please enter a value.")
    if not uploaded_file:
        raise ValueError("No document uploaded. Please upload a document.")

def disable_button():
    st.session_state.disabled = True

def enable_button():
    if "disabled" not in st.session_state:
        st.session_state.disabled=False

def get_fsdocument():
    with st.sidebar:
        st.title("Test Plan Generator")
        st.markdown("<span ><font size=1>Powered by Google Gemini ♊ </font></span>", unsafe_allow_html=True)
        st.divider()
        st.markdown("<span ><font size=3>Author: Lakshmanan Kuppan</font></span>", unsafe_allow_html=True)
        st.markdown("[Linkedin](https://www.linkedin.com/in/lakshmanankuppan/)")
        st.markdown("[GitHub](https://github.com/lkuppancodebox/Public_testplangenerator.git)")
        st.divider()

        disable_button()
        title = st.text_input(label="Enter Functional Specification Title", on_change=None, key="user_input",
                              help="Ex: RFC-979 PSN END-TO-END FUNCTIONAL SPECIFICATION")

        fs_document = st.file_uploader(label='Upload Functional Specification', type='.docx', accept_multiple_files=False,
                                       key=str,
                                       help="Browse and upload FS document in word format (.docx)")

        if title and fs_document:
            enable_button()
            submit_button = st.button("Submit", key="submit_button_key", on_click=disable_button())

            if submit_button:
                try:
                    check_values(title, fs_document)
                    st.success("Don't Submit again, Test Plan writing is in progress..")
                    return title, fs_document
                except ValueError as e:
                    st.error(str(e))
        else:
            st.stop()

def display_output(filename):
    with open(filename, 'r', encoding='utf-8') as fid :
        html_content = fid.read()

    html_content_b64 = base64.b64encode(html_content.encode()).decode()

    st.success("Test Plan is generated in html format")
    st.download_button(label="Download", file_name=filename, data=html_content)
    st.markdown("<span style='font-size:25px;'>Preview : </span>", unsafe_allow_html=True)

    # Wrap HTML content inside a div with overflow style
    scrollable_html = f'<div style="overflow-y: scroll; height: 400px;">{html_content}</div>'

    # Display HTML content with scroll bar
    st.components.v1.html(scrollable_html, height= 400)



