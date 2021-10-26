from django.shortcuts import render

from .mixins import YouTube

'''
Basic view for displaying videos 
'''
def videos(request):

	videos = YouTube().get_data()

	context = {"videos": videos}
	return render(request, 'livestream/videos.html', context)


'''
Basic view for showing a video in an iframe 
'''
def play_video(request):

	vid_id = request.GET.get("vid_id")
	vid_data = YouTube(vid_id = vid_id).get_video()
	context = {
		"vid_data": vid_data,
	}
	return render(request, 'livestream/play_video.html', context)