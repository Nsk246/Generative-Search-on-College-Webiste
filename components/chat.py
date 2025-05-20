import reflex as rx

from webui import styles
from webui.components import loading_icon
from webui.state import q, QA
from webui.state import Statex as stn
from openai import OpenAI
from webui.state import news


def message(qa: QA) -> rx.Component:
    """A single question/answer message.

    Args:
        qa: The question/answer pair.

    Returns:
        A component displaying the question/answer pair.
    """
    return rx.chakra.box(
        rx.chakra.box(
            rx.chakra.text(
                qa.question,
                bg="#474C5F",
                color='#fff',
                shadow=styles.shadow_light,
                **styles.message_style,
            ),
            text_align="right",
            margin_top="2em",
            opacity=0.7
        ),
        rx.chakra.box(
            rx.chakra.text(
                qa.answer,
                bg="#d7dbe1",
                shadow=styles.shadow_light,
                **styles.message_style,
            ),
            text_align="left",
            padding_top="2em",
            opacity=0.85
        ),
        width="100%",
    )


def chat() -> rx.Component:
    """List all the messages in a single conversation."""
    return rx.chakra.vstack(
        rx.chakra.box(rx.foreach(stn.chats[stn.current_chat], message)),
        
        py="8",
        flex="1",
        width="100%",
        max_w="5xl",
        padding_x="4",
        align_self="center",
        overflow="hidden",
        padding_bottom="5em",
    )

from textwrap import dedent
import reflex as rx

from typing import Dict, Any, List
import reflex as rx
from reflex.vars import Var
import base64

class AudioRecorder(rx.Component):
    """Wrapper for react-audio-voice-recorder component."""
    
    # The React library to wrap.
    library = "react-audio-voice-recorder"
    
    # The React component tag.
    tag = "AudioRecorder"

    is_default = False

    def get_event_triggers(self) -> dict[str, Any]:
        return {
            **super().get_event_triggers(),
            "on_recording_complete": _on_recording_complete_signature,
        }

audio_recorder = AudioRecorder.create

def _on_recording_complete_signature(blob: Any) :
    return [
        rx.Var.create_safe(f"extract_audio({blob})")
    ]
from openai import OpenAI
#openai.api_key = "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"
class AudioState(rx.State):
    transcriptt : str
    def recording_complete_callback(self, b64_str):
        decodedData = base64.b64decode(b64_str.split(',')[1])
        webmfile = (rx.get_upload_dir() / "audio.wav")
        client = OpenAI()
        with open(webmfile, 'wb') as file:
            file.write(decodedData)
        audio_file= open(rx.get_upload_dir() / "audio.wav", "rb")
        transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language='en',
        response_format="text")
        #print(transcript)
        file.close()
        #a=(q(str(transcript)))
        #news("Success")
        return stn.process_question1(transcript)
        
        
        
        
        
        
       
       
       
    
        
    def update_recorded_audio(self, url: any):
        return [
            rx.call_script(f"""download_blob("{url}")""", callback=AudioState.recording_complete_callback)
        ]




def action_bar() -> rx.Component:
    """The action bar to send a new message."""
    return rx.chakra.box(
        rx.chakra.vstack(
            rx.chakra.form(
                rx.chakra.form_control(
                    rx.chakra.hstack(
                        rx.chakra.input(
                            placeholder="Type something...",
                            color='#fff',
                            bg='#27252C',
                            id="question",
                             _focus={
    "box_shadow": "0 0 8px 2px rgba(0, 21, 125, 0.86)",
  },
                            _placeholder={"color": "e4e5f1"},
                            #_hover={"border_color": styles.accent_color},
                            style=styles.input_style,
                            
                        ),
                        rx.chakra.button(
                            rx.cond(
                                stn.processing,
                                loading_icon(height="1em"),
                                rx.chakra.text("Search"),
                            ),
                            border = "1px solid #1C1B20",
                            type_="submit",
                            _hover={"bg": styles.accent_color},
                            style=styles.input_style2,
                        ),
                       rx.center(rx.script("""function download_blob(url) {
                    console.log(url);
                    var xhr = new XMLHttpRequest();
                    xhr.open('GET', url, true);
                    xhr.responseType = 'blob';
                    return new Promise((resolve, reject) => {
                        xhr.onload = function(e) {
                            if (this.status == 200) {
                                var blob = this.response;
                                // console.log(blob);
                                // blob is now the blob that the object URL pointed to.
                                var reader = new window.FileReader();
                                reader.readAsDataURL(blob); 
                                reader.onloadend = function() {
                                    var base64 = reader.result;
                                    // base64 = base64.split(',')[1];
                                    // console.log(base64);
                                    resolve(base64);
                                }
                            }
                        };
                        xhr.send();
                    });
                  };
                """),
        
        rx.script("""function extract_audio(blob) {
                if (!(blob instanceof Blob)) {
                    console.error('Invalid argument type:', typeof blob);
                    throw new TypeError('Argument must be a Blob');
                }
                console.log('Extracting audio from type:', typeof blob);
                console.log('instance of Blob:', blob instanceof Blob);
                const url = URL.createObjectURL(blob);
                return url;
            };
            """),
         audio_recorder(
            id="audio_recorder",
            on_recording_complete=AudioState.update_recorded_audio,
			download_on_save_press=True,
        ), )

                    ),
                    is_disabled=stn.processing,
                ),
                on_submit=stn.process_question,
                reset_on_submit=True,
                width="100%",
            ),
            rx.chakra.text(
                "May return factually incorrect or misleading responses. Use discretion.",
                font_size="xs",
                color="#36454F",
                text_align="center",
            ),
            width="100%",
            max_w="3xl",
            mx="auto",
        ),
        box_shadow= "rgba(0, 0, 0, 0.15) 0px 2px 8px" , 
        position="sticky",
        bottom="0",
        left="0",
        py="4",
        backdrop_filter="auto",
        backdrop_blur="lg",
        border_top=f"3px solid {'#1C1B20'}",
        align_items="stretch",
        width="100%",
    )
