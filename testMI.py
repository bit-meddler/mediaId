from pyMediaInfo import MediaInfo, Track
#fix DLL path
MediaInfo.PATH_TO_DLL = r"C:\libs\mediaInfo"

        
def report( data ):
    ret = ""
    data = data.to_data()
    for i, t in enumerate( data["tracks"] ) :
        type = t["track_type"]
        ret += "Stream:{}, Type:{}, Kind:{}\n".format( i, type, t["kind_of_stream"] )
        keys = []
        if type == "General":
            keys = [ "complete_name", "writing_application", "encoded_application_name", "count_of_video_streams", "frame_rate", "othercount", "other_format_list",
                     "frame_count", "codec", "file_creation_date", "duration", "audio_codecs", "audio_format_list", "count_of_audio_streams",
                     "track_id", "stream_identifier", "count", "type"
            ]
        elif type == "Video":
            keys = [ "track_id", "stream_identifier", "other_delay", "sampled_width", "width", "sampled_height", "height", "frame_count",
                     "count_of_stream_of_this_kind", "other_stream_identifier", "streamorder", "other_track_id", "frame_rate", "count",
                     "other_delay", "other_kind_of_stream", "count", "format", "type"
            ]
        elif type == "Audio":
            keys = [ "track_id", "stream_identifier", "other_delay", "other_channel_s", "frame_count", "other_video0_delay",
                     "count_of_stream_of_this_kind", "other_stream_identifier", "streamorder", "other_track_id", "frame_rate", "count",
                     "other_delay", "delay_relative_to_video", "count", "format", "type", "count_of_stream_of_this_kind"
            ]
        elif type == "Other":
            keys = [ "track_id, ""count", "stream_identifier", "format", "type", "count_of_stream_of_this_kind", "time_code_of_first_frame",
                     
            ]
        elif type == "Text":
            print t
        else:
            ret += "Unknown type of stream '{}'".format( type )
            
        for k in keys:
            v = "Not found"
            if k in t:
                v = t[k]
            ret += "\t{: >32}:{}\n".format( k, v )
            
    return ret

# Examine the RAW video from various Camcorders        
tasks = {   "FX100" : r"C:\temp\xf100_tests\CLIPS001\AA0005\AA000501.MXF",
            "7D"    : r"E:\resources\Richs_Stuff\media\deskTrackData\MVI_0637.MOV",
            "NX5"   : r"E:\resources\Richs_Stuff\MoCap_stuff\refCams\Cam1\00013.MTS",
}    
for k,v in tasks.iteritems():
    mio = MediaInfo.parse( v, library_file=r"C:\libs\mediaInfo\MediaInfo.dll" )
    print report( mio )
    with open( r"C:\temp\{}".format(k), 'w' ) as fh:
        fh.write( mio.to_json() )

v = r"E:\resources\Richs_Stuff\MoCap_stuff\refCams\Cam1\00013.MTS"
mio = MediaInfo.parse( v, library_file=r"C:\libs\mediaInfo\MediaInfo.dll" )


"""
The ultimate idea is to develop a series of 'filters' that are tuned for a specific camera type,
and will present clip data in a standardized way to consumers of video clips.

the general case will be combining camcorders for a 4-up quad split, and trimming the takes to
conform to 'action - cut' points.
"""
