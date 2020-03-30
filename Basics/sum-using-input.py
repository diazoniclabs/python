'''
print('Hello World')
input('Whaat is your channel name?')

#One Liner
Format specifiers
print('My Channel name is %s' %input('What is your channel name?'))

# What are variables?    [Reserved memory location to store values]
GO back to shell and first talk about  variables , then id as well'''

channel_name = input('What is your channel name? ')
#print('My channel name is %s' %channel_name)
print('My channel name is ' ,channel_name)
'''
Talk about constants and sum in shell
'''
python_videos = int(input("How many videos in Python Playlist? "))
arduino_videos = int(input("How many videos in Arduino Playlist?"))
print( "In ",channel_name, "youtube channel , there are ",python_videos," videos in Python playlist,"
                            ,arduino_videos," videos in Arduino playlist and hence has "
                            ,python_videos+arduino_videos,"total videos")
       

