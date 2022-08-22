from pytube import YouTube, exceptions
import ffmpeg

class YTinterface():
    def __init__(self):
        self.__video = None
        self.__streams = {}

    
    def submitLink(self, link: str) -> bool:
        try:
            self.__video = YouTube(link)
        except exceptions.VideoUnavailable:
            print("Video unavailable")
            return False
        except exceptions.RegexMatchError:
            print("URL not provided")
            return False
        else:
            audioITAG = self.__video.streams.get_audio_only().itag
            if audioITAG:
                self.__streams["audio"] = audioITAG 
            itag360 = self.__video.streams.filter(res='360p', file_extension='mp4', progressive=False)
            if itag360:
                self.__streams["360p"] = itag360[0].itag
            itag480 = self.__video.streams.filter(res='480p', file_extension='mp4', progressive=False)
            if itag480:
                self.__streams["480p"] = itag480[0].itag
            itag720 = self.__video.streams.filter(res='720p', file_extension='mp4', progressive=False)
            if itag720:
                self.__streams["720p"] = itag720[0].itag
            itag1080 = self.__video.streams.filter(res='1080p', file_extension='mp4', progressive=False)
            if itag1080:
                self.__streams["1080p"] = itag1080[0].itag
            return True


    def getThumbURL(self) -> str:
        if self.__video == None:
            print("Video not set yet")
            return None
        return self.__video.thumbnail_url
    

    def getTitle(self) -> str:
        if self.__video == None:
            print("Video not set yet")
            return None
        return self.__video.title

    def getStreams(self) -> dict:
        if self.__video == None:
            print("Video not set yet")
            return None
        return self.__streams

    
    def download(self, stream: str) -> None:
        if self.__video == None:
            print("Video not set yet")
            return None
        if stream != "audio":
            video = self.__video.streams.get_by_itag(self.__streams["audio"])
            video.download(filename="audio.mp4")
            video = self.__video.streams.get_by_itag(self.__streams[stream])
            video.download(filename="video.mp4")
            self.combine()
        else:
            video = self.__video.streams.get_by_itag(self.__streams["audio"])
            video.download()


    def combine(self) -> None:
        input_video = ffmpeg.input('audio.mp4')
        input_audio = ffmpeg.input('video.mp4')
        title = self.getTitle()
        #ffmpeg.concat(input_video, input_audio, v=1, a=1).output('combine.mp4').run()
        out = ffmpeg.output(input_video, input_audio, 'combine.mp4', vcodec='copy', acodec='aac', strict='experimental')
        out.run()