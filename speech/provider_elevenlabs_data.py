import credentials
import constants
from typing import Optional
from tts_wrapper import ElevenLabsTTS, ElevenLabsClient
from provider_base import BaseProvider


class ElevenLabsDataProvider(BaseProvider):
    def __init__(self):
        client = ElevenLabsClient(credentials=(credentials.ELEVENLABS_KEY,))
        tts = ElevenLabsTTS(client)
        super().__init__("elevenlabs_data", constants.VOICE_TYPE_EXTERNAL_DATA, tts)

    def getSpeakData(self, text: str, voiceId: Optional[str] = None) -> bytes:
        if voiceId:
            self.tts.set_voice(voiceId)
        return self.tts.synth_to_bytes(text)


# Create a singleton instance
provider = ElevenLabsDataProvider()

# Export the interface functions
getProviderId = provider.getProviderId
getVoiceType = provider.getVoiceType
getVoices = provider.getVoices
getSpeakData = provider.getSpeakData
