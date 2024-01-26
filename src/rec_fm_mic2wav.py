##
# @file rec_fm_mic2wav.py
# @brief Record from a microphone and save to a WAV file.
# @author yukinagata3184

import wave
import pyaudio

FORMAT = pyaudio.paInt16

def rec_fm_mic2wav(param_dict):
    """! Record from a microphone and save to a WAV file.
    @param param_dict [dict] Set params in dict.
    @n e.g. {"CHUNK": 1024, "CHANNELS": 1, "SAMP_RATE": 16000, "RECORD_SECONDS": 10}
    """
    with wave.open('record.wav', 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(param_dict["CHANNELS"])
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(param_dict["SAMP_RATE"])
    
        stream = p.open(format=FORMAT, channels=param_dict["CHANNELS"], 
                        rate=param_dict["SAMP_RATE"], input=True)
    
        print('Recording...')
        # floor division
        for _ in range(0, param_dict["SAMP_RATE"] // 
                       param_dict["CHUNK"] * param_dict["RECORD_SECONDS"]):
            wf.writeframes(stream.read(param_dict["CHUNK"]))
        print('Done')
    
        stream.close()
        p.terminate()